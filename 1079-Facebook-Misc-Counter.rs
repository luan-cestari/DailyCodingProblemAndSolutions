#![feature(option_result_contains)]

use std::collections::HashMap;

fn given_int_list_return_unique_elements(vec: Vec<i32>) -> Result<Vec<i32>, &'static str> {
    if vec.len() == 0 {
        return Err("invalid length");
    }

    let mut counter = HashMap::new();

    vec.iter().enumerate().for_each(|(_pos, value)| {
        *counter.entry(value).or_insert(0) += 1;
    });

    let mut uniques = Vec::new();
    vec.iter().enumerate().for_each(|(_pos, value)| {
        if *counter.get(value).unwrap() == 1 {
            uniques.push(*value)
        }
    });

    Ok(uniques)
}

fn main() {
    let vec = vec![2, 4, 6, 8, 10, 2, 6, 10];

    match given_int_list_return_unique_elements(vec) {
        Ok(vector) => println!("result: {vector:?}"),
        Err(e) => println!("error: {e:?}"),
    }
}
