#![feature(is_some_with)]

#[derive(Clone)]
struct Node {
    children: Vec<Node>,
    data: i32,
}

fn recursive_given_two_n_tree_return_true_if_symmetric(
    node1: &Node,
    node2: &Node,
) -> Result<bool, &'static str> {
    if node1.data != node2.data {
        return Ok(false);
    }

    if node1.children.len() != node2.children.len() {
        return Ok(false);
    }

    let mut i = 0;
    for left_child_of_1 in &node1.children {
        let right_child_of_2 = &node2.children[node2.children.len() - i - 1];
        let r = recursive_given_two_n_tree_return_true_if_symmetric(
            &left_child_of_1.clone(),
            right_child_of_2,
        );
        if r.is_ok_and(|&x| x == false) {
            return Ok(false);
        }
        i += 1;
    }

    Ok(true)
}

fn main() {
    let mut root = Node {
        children: Vec::new(),
        data: 4,
    };
    root.children.push(Node {
        children: Vec::new(),
        data: 1,
    });
    root.children[0].children.push(Node {
        children: Vec::new(),
        data: 5,
    });
    root.children[0].children.push(Node {
        children: Vec::new(),
        data: 5,
    });

    match recursive_given_two_n_tree_return_true_if_symmetric(&root, &root) {
        Ok(int) => println!("result: {int:?}"),
        Err(e) => println!("error: {e:?}"),
    }
}
