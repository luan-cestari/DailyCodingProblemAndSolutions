#![feature(is_some_with)]
#![feature(new_uninit)]

use std::cmp;

#[derive(Clone)]
struct Node {
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
    data: i32,
}

#[derive(Clone, Copy, Debug)]
struct IntegerHolder {
    val: i32,
}

fn recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(
    option_binary_tree: Option<Box<Node>>,
    cadidate_max_sum: &mut IntegerHolder,
) -> Result<i32, &'static str> {
    if option_binary_tree.is_none() {
        return Ok(0);
    }

    // Assuming no error, as current impl
    let node = option_binary_tree.unwrap();
    let left_max = recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(
        node.left,
        cadidate_max_sum,
    )
    .unwrap();
    let right_max = recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(
        node.right,
        cadidate_max_sum,
    )
    .unwrap();

    // Store the best alternative: Node+children OR Node alone
    let max_lef_or_right = cmp::max(left_max, right_max);
    let max_single_path = cmp::max(max_lef_or_right + node.data, node.data);

    // Only one node can have left and right path
    let max_both_path = cmp::max(max_single_path, left_max + right_max + node.data);

    // Update the best max sum path found so far
    cadidate_max_sum.val = cmp::max(cadidate_max_sum.val, max_both_path);

    return Ok(max_single_path);
}

fn main() {
    let root = Node {
        left: Option::Some(Box::new(Node {
            left: Option::Some(Box::new(Node {
                left: Option::None,
                right: Option::None,
                data: 1,
            })),
            right: Option::None,
            data: 1,
        })),
        right: Option::Some(Box::new(Node {
            left: Option::None,
            right: Option::None,
            data: 5,
        })),
        data: 4,
    };

    let mut cadidate_max_sum = IntegerHolder { val: i32::MIN };
    match recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(
        Option::Some(Box::new(root)),
        &mut cadidate_max_sum,
    ) {
        Ok(_int) => println!("result: {cadidate_max_sum:?}"),
        Err(e) => println!("error: {e:?}"),
    }
}
