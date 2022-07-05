fn add_subtract(vec: Vec<i32>) -> Result<i32, &'static str> {
    if vec.len() == 0 {
        return Err("invalid length");
    }

    let mut sum = 0;
    let mut is_subtraction = false;
    vec.iter().enumerate().for_each(|(pos, value)| {
        if pos == 0 {
            sum = value.clone();
        } else {
            if is_subtraction {
                is_subtraction = false;
                sum -= value
            } else {
                is_subtraction = true;
                sum += value
            }
        }
        //println!("Item {} = {}", pos, value);
    });

    Ok(sum)
}

fn main() {
    let vec = vec![-5, 10, 3, 9];

    match add_subtract(vec) {
        Ok(int) => println!("result: {int:?}"),
        Err(e) => println!("error: {e:?}"),
    }
}
