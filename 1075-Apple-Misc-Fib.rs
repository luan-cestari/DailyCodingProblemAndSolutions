use std::io;

fn given_n_calculate_fib_space_o_1(n: i32) -> Result<i32, &'static str> {
    let mut t1 = 0;
    let mut t2 = 1;

    if n == 1 {
        return Ok(t1);
    }

    if n == 2 {
        return Ok(t2);
    }

    let mut counter = n - 2;
    let mut t3 = 0;
    while counter > 0 {
        t3 = t1 + t2;
        t1 = t2;
        t2 = t3;
        counter -= 1;
    }

    Ok(t3)
}

fn main() {
    let mut input_line = String::new();
    io::stdin()
        .read_line(&mut input_line)
        .expect("Failed to read line");
    let n: i32 = input_line.trim().parse().expect("Input not an integer");

    match given_n_calculate_fib_space_o_1(n) {
        Ok(r) => println!("result: {r:?}"),
        Err(e) => println!("error: {e:?}"),
    }
}
