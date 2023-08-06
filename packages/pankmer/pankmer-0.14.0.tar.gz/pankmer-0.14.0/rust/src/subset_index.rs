use std::fs;
use std::io::{Read, Write, BufReader, BufWriter, ErrorKind};
use std::path::{Path, PathBuf};
use std::iter::zip;
use niffler;
use pyo3::prelude::*;
use crate::helpers::score_byte_to_blist;
use crate::{K, PKGenomes, GZIP_LEVELS, Score};
use crate::metadata::{PKMeta, load_metadata};
use crate::get_kmers::genome_index_to_byte_idx_and_bit_mask;

fn compress_score(superset_score: Score, n_superset_genomes: usize, n_subset_bytes: usize, memberships: &Vec<usize>, exclusions: &Vec<usize>, exclusive: bool) -> Score {
    let expanded_score: Vec<usize> = score_byte_to_blist(&superset_score, n_superset_genomes).expect("could not expand score");
    if exclusive {
        for j in exclusions.iter() {
            if expanded_score[*j] == 1 {
                return vec![0u8; n_subset_bytes]
            }
        }
    }
    let mut compressed_score: Score = vec![0; n_subset_bytes];
    for (i, j) in memberships.iter().enumerate() {
        if expanded_score[*j] == 1 {
            let (byte_idx, bit_mask) = genome_index_to_byte_idx_and_bit_mask(i, n_subset_bytes);
            compressed_score[byte_idx] = compressed_score[byte_idx] | bit_mask;
        }
    }
    return compressed_score
}


#[pyfunction]
pub fn subset(idx_dir: &str, tar_file: &str, subset_genomes: PKGenomes,
              outdir: &str, gzip_level: usize, exclusive: bool) -> PyResult<()> {
    let mut metadata = PKMeta::new();
    let mut subset_genomes_ordered = Vec::new();
    let output_is_tar: bool = outdir.ends_with(".tar");
    match fs::create_dir(outdir) {
        Ok(_) => (),
        Err(_) => match Path::new(outdir).is_dir() {
            true => (),
            false => panic!("Could not create dir and dir does not exist")
        }
    };
    let superset_meta: PKMeta = load_metadata(idx_dir, tar_file)?;
    metadata.mem_blocks = superset_meta.mem_blocks;
    let n_superset_genomes = superset_meta.genomes.len();
    let mut superset_genomes: PKGenomes = Vec::new();
    for i in 0..n_superset_genomes {
        let genome = superset_meta.genomes.get(&i).expect("could not get genome name");
        superset_genomes.push(genome.to_string());
        if subset_genomes.contains(genome) {
            subset_genomes_ordered.push(genome.to_string());
        }
    }
    for (i, g) in subset_genomes_ordered.iter().enumerate() {
        let size = superset_meta.genome_sizes.get(g).expect("could not get genome size");
        metadata.genome_sizes.insert(g.to_string(), *size);
        metadata.genomes.insert(i, g.to_string());
    }
    let n_superset_genomes = superset_genomes.len();
    let n_subset_genomes = superset_genomes.len();
    let n_subset_bytes = (n_subset_genomes + 7) / 8;
    const KMER_BITSIZE: usize =  (K * 2 + 7) / 8;
    let superset_score_bitsize: usize = (n_superset_genomes + 7) / 8;
    let subset_score_bitsize: usize = (n_subset_genomes + 7) / 8;
    let mut memberships: Vec<usize> = Vec::new();
    let mut exclusions: Vec<usize> = Vec::new();
    for (i, genome) in superset_genomes.iter().enumerate() {
        if subset_genomes.contains(&genome) {
            memberships.push(i);
        } else {
            exclusions.push(i);
        }
    }
    let mut kmers_out_path = PathBuf::from(&outdir);
    kmers_out_path.push("kmers.bgz");
    let mut scores_out_path = PathBuf::from(&outdir);
    scores_out_path.push("scores.bgz");
    const KMER_BUFSIZE: usize = 1000*KMER_BITSIZE;
    let superset_score_bufsize: usize = 1000*superset_score_bitsize;
    let subset_score_bufsize: usize = 1000*subset_score_bitsize;
    let mut kmers_out = BufWriter::with_capacity(KMER_BUFSIZE, niffler::to_path(kmers_out_path, niffler::compression::Format::Gzip, GZIP_LEVELS[gzip_level]).expect("Can't open file for writing"));
    let mut scores_out = BufWriter::with_capacity(subset_score_bufsize, niffler::to_path(scores_out_path, niffler::compression::Format::Gzip, GZIP_LEVELS[gzip_level]).expect("Can't open file for writing"));
    let mut count = 0;
    let mut kmer_buf = [0; KMER_BITSIZE];
    let mut score_buf = vec![0; superset_score_bitsize];
    let mut kmers_in_path: PathBuf = PathBuf::from(&idx_dir);
    kmers_in_path.push("kmers.bgz");
    let mut scores_in_path: PathBuf = PathBuf::from(&idx_dir);
    scores_in_path.push("scores.bgz");
    let (kmers_reader, _format) = niffler::from_path(&kmers_in_path).expect("File not found");
    let (scores_reader, _format) = niffler::from_path(&scores_in_path).expect("File not found");
    let mut kmers_in = BufReader::with_capacity(KMER_BUFSIZE, kmers_reader);
    let mut scores_in = BufReader::with_capacity(superset_score_bufsize, scores_reader);
    loop {
        let kmers = match kmers_in.read_exact(&mut kmer_buf) {
            Ok(_) => kmer_buf.chunks(KMER_BITSIZE).map(|bytes| u64::from_be_bytes(bytes.try_into().unwrap())).collect::<Vec<u64>>(),
            Err(ref e) if e.kind() == ErrorKind::UnexpectedEof => break,
            // Err(ref e) if e.kind() == ErrorKind::Interrupted => continue,
            Err(e) => panic!("{:?}", e),
        };
        let scores = match scores_in.read_exact(&mut score_buf) {
            Ok(_) => score_buf.chunks(superset_score_bitsize).map(
                |bytes| compress_score(bytes.to_vec(), n_superset_genomes, n_subset_bytes, &memberships, &exclusions, exclusive)).collect::<Vec<Score>>(),
            Err(ref e) if e.kind() == ErrorKind::UnexpectedEof => break,
            // Err(ref e) if e.kind() == ErrorKind::Interrupted => continue,
            Err(e) => panic!("{:?}", e),
        };
        let iter = zip(kmers, scores);
        for (kmer, score) in iter {
            match score.iter().any(|&i| i>0u8) {
                true => {
                    kmers_out.write(&kmer.to_be_bytes()[8-KMER_BITSIZE..]).unwrap();
                    scores_out.write(&score).unwrap();
                },
                false => { continue; }
            };
            if count % 10000000 == 0 && count != 0 {
                metadata.positions.insert(kmer.to_string(), count);
                count = 0;
            }
            count += 1;
        }
    }
    kmers_out.flush().unwrap();
    scores_out.flush().unwrap();
    let mut meta_out_path = PathBuf::from(&outdir);
    meta_out_path.push("metadata.json");
    let meta_out = fs::File::create(&meta_out_path).expect(
        "Can't open file for writing"
    );
    serde_json::to_writer(&meta_out, &metadata).expect(
        "Couldn't write PKMeta to file"
    );
    Ok(())
}
