use crossbeam_channel::{bounded, Receiver};
use log::info;
use pyo3::prelude::*;
use std::cmp::min;
use std::sync::Arc;
use std::thread;

fn compare_characters(chr1: char, chr2: char, seq1_n: bool, seq2_n: bool) -> usize {
    if chr1 == chr2 || (chr1 == 'N' && seq1_n == true) || (chr2 == 'N' && seq2_n == true) {
        0
    } else {
        1
    }
}

#[pyfunction]
fn distance(seq1: &str, seq2: &str, seq1_n: bool, seq2_n: bool) -> PyResult<usize> {
    let seq1 = seq1.to_uppercase();
    let seq2 = seq2.to_uppercase();
    let len1 = seq1.len();
    let len2 = seq2.len();
    let mut matrix: Vec<Vec<usize>> = vec![];
    for m in 0..len1 + 1 {
        matrix.push(vec![0; len2 + 1]);
        matrix[m][0] = m;
    }
    for n in 0..len2 + 1 {
        matrix[0][n] = n;
    }
    seq1.chars().enumerate().into_iter().for_each(|(m, chr1)| {
        seq2.chars().enumerate().into_iter().for_each(|(n, chr2)| {
            matrix[m + 1][n + 1] = min(
                min(matrix[m + 1][n] + 1, matrix[m][n + 1] + 1),
                matrix[m][n] + compare_characters(chr1, chr2, seq1_n, seq2_n),
            )
        });
    });
    Ok(matrix[len1][len2])
}

#[pyfunction]
fn dual_index_distance(
    i7: &str,
    i5: &str,
    b7: &str,
    b5: &str,
    seq1_n: bool,
    seq2_n: bool,
) -> PyResult<(usize, usize)> {
    Ok((
        distance(i7, b7, seq1_n, seq2_n).unwrap(),
        distance(i5, b5, seq1_n, seq2_n).unwrap(),
    ))
}

fn list_distance(
    seq1: &str,
    seq2_list: &Vec<String>,
    mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
) -> PyResult<Vec<(String, usize)>> {
    let mut distance_list: Vec<(String, usize)> = Vec::new();
    let contain_n = seq1.to_uppercase().contains('N');
    if mismatch == 0 && !(contain_n) {
        seq2_list.into_iter().for_each(|seq2| {
            if seq1 == seq2 {
                distance_list.push((seq2.to_string(), 0));
            }
        });
    } else {
        seq2_list.into_iter().for_each(|seq2| {
            let d = distance(seq1, seq2, seq1_n, seq2_n).unwrap();
            if d <= mismatch {
                distance_list.push((seq2.to_string(), d));
            }
        });
    }
    Ok(distance_list)
}

fn list_consumer(
    seq1_receiver: Receiver<String>,
    seq2_list: Arc<Vec<String>>,
    mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
) -> PyResult<Vec<(String, Vec<(String, usize)>)>> {
    let mut distance_list: Vec<(String, Vec<(String, usize)>)> = Vec::new();
    for seq1 in seq1_receiver {
        let d = list_distance(&seq1, &seq2_list, mismatch, seq1_n, seq2_n).unwrap();
        distance_list.push((seq1, d))
    }
    Ok(distance_list)
}

#[pyfunction]
fn list_to_list_distance(
    seq1_list: Vec<String>,
    seq2_list: Vec<String>,
    mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
    thread: usize,
) -> PyResult<Vec<(String, Vec<(String, usize)>)>> {
    let (barcode_sender, barcode_receiver) = bounded::<String>(100);
    let seq2_list_arc = Arc::new(seq2_list);
    let mut thread_list = Vec::new();
    for num in 0..thread {
        let thread_receiver = barcode_receiver.clone();
        let thread_seq2_list = seq2_list_arc.clone();
        thread_list.push(
            thread::Builder::new()
                .name(format!("Barcode_distance_{num}"))
                .spawn(move || {
                    list_consumer(thread_receiver, thread_seq2_list, mismatch, seq1_n, seq2_n)
                })
                .unwrap(),
        )
    }
    for barcode in seq1_list {
        barcode_sender.send(barcode).unwrap();
    }
    drop(barcode_sender);
    info!("All barcode sended.");
    let mut distance_list: Vec<(String, Vec<(String, usize)>)> = Vec::new();
    for thread in thread_list {
        let thread_distance_list = thread.join().unwrap().unwrap();
        distance_list.extend_from_slice(&thread_distance_list);
    }
    Ok(distance_list)
}

fn cal_barcode_distance(
    seq1: &str,
    seq2: &str,
    mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
) -> usize {
    let contain_n = seq1.to_uppercase().contains('N');
    if mismatch == 0 && !(contain_n) {
        if seq1 == seq2 {
            return 0;
        } else {
            return seq1.len();
        }
    } else {
        return distance(seq1, seq2, seq1_n, seq2_n).unwrap();
    };
}

#[pyfunction]
fn dual_index_list_distance(
    i7: &str,
    i5: &str,
    barcode_list: Vec<(String, String)>,
    i7_mismatch: usize,
    i5_mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
) -> PyResult<Vec<(String, String, usize, usize)>> {
    let mut distance_list: Vec<(String, String, usize, usize)> = Vec::new();
    barcode_list.into_iter().for_each(|(b7, b5)| {
        let d7 = cal_barcode_distance(i7, &b7, i7_mismatch, seq1_n, seq2_n);
        let d5 = cal_barcode_distance(i5, &b5, i5_mismatch, seq1_n, seq2_n);
        if d7 <= i7_mismatch && d5 <= i5_mismatch {
            distance_list.push((b7.to_string(), b5.to_string(), d7, d5));
        }
    });
    Ok(distance_list)
}

fn dual_index_list_distance_for_consumer(
    i7: &str,
    i5: &str,
    barcode_list: &Vec<(String, String)>,
    i7_mismatch: usize,
    i5_mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
) -> PyResult<Vec<(String, String, usize, usize)>> {
    let mut distance_list: Vec<(String, String, usize, usize)> = Vec::new();
    barcode_list.into_iter().for_each(|(b7, b5)| {
        let d7 = cal_barcode_distance(i7, b7, i7_mismatch, seq1_n, seq2_n);
        let d5 = cal_barcode_distance(i5, b5, i5_mismatch, seq1_n, seq2_n);
        if d7 <= i7_mismatch && d5 <= i5_mismatch {
            distance_list.push((b7.to_string(), b5.to_string(), d7, d5));
        }
    });
    Ok(distance_list)
}

fn dual_index_list_consumer(
    barcode_receiver: Receiver<(String, String)>,
    barcode_list: Arc<Vec<(String, String)>>,
    i7_mismatch: usize,
    i5_mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
) -> PyResult<Vec<(String, String, Vec<(String, String, usize, usize)>)>> {
    let mut distance_list: Vec<(String, String, Vec<(String, String, usize, usize)>)> = Vec::new();
    for (i7, i5) in barcode_receiver {
        let d = dual_index_list_distance_for_consumer(
            &i7,
            &i5,
            &barcode_list,
            i7_mismatch,
            i5_mismatch,
            seq1_n,
            seq2_n,
        )
        .unwrap();
        distance_list.push((i7, i5, d))
    }
    Ok(distance_list)
}

#[pyfunction]
fn dual_index_list_to_list_distance(
    barcode1_list: Vec<(String, String)>,
    barcode2_list: Vec<(String, String)>,
    i7_mismatch: usize,
    i5_mismatch: usize,
    seq1_n: bool,
    seq2_n: bool,
    thread: usize,
) -> PyResult<Vec<(String, String, Vec<(String, String, usize, usize)>)>> {
    info!("Program start.");
    let (barcode_sender, barcode_receiver) = bounded::<(String, String)>(100);
    let barcode2_list_arc = Arc::new(barcode2_list);
    let mut thread_list = Vec::new();
    for num in 0..thread {
        let thread_receiver = barcode_receiver.clone();
        let thread_barcode2_list = barcode2_list_arc.clone();
        thread_list.push(
            thread::Builder::new()
                .name(format!("Barcode_distance_{num}"))
                .spawn(move || {
                    dual_index_list_consumer(
                        thread_receiver,
                        thread_barcode2_list,
                        i7_mismatch,
                        i5_mismatch,
                        seq1_n,
                        seq2_n,
                    )
                })
                .unwrap(),
        )
    }
    info!("All thread started.");
    for barcode in barcode1_list {
        barcode_sender.send(barcode).unwrap();
    }
    drop(barcode_sender);
    info!("All barcode sended.");
    let mut distance_list: Vec<(String, String, Vec<(String, String, usize, usize)>)> = Vec::new();
    for thread in thread_list {
        let thread_distance_list = thread.join().unwrap().unwrap();
        distance_list.extend_from_slice(&thread_distance_list);
    }
    info!("Program finished.");
    Ok(distance_list)
}

/// A Python module implemented in Rust.
#[pymodule]
fn barcode_distance(_py: Python, m: &PyModule) -> PyResult<()> {
    env_logger::init();
    m.add_function(wrap_pyfunction!(distance, m)?)?;
    m.add_function(wrap_pyfunction!(dual_index_distance, m)?)?;
    m.add_function(wrap_pyfunction!(list_to_list_distance, m)?)?;
    m.add_function(wrap_pyfunction!(dual_index_list_distance, m)?)?;
    m.add_function(wrap_pyfunction!(dual_index_list_to_list_distance, m)?)?;
    Ok(())
}
