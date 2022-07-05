#![feature(is_some_with)]
#![feature(new_uninit)]

use std::collections::VecDeque;

#[derive(Clone)]
struct Node {
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
    data: i32,
}

#[derive(Clone)]
struct NodeLevel {
    node: Node,
    level: i32,
}

fn given_binary_tree_return_level_with_minimum_sum(tree: &Node) -> Result<i32, &'static str> {
    let mut to_visit_queue: VecDeque<NodeLevel> = VecDeque::from([NodeLevel {
        node: tree.clone(),
        level: 0,
    }]);

    let mut minimum_sum = tree.data.clone();
    let mut ms_level = 0;
    let mut last_sum = 0;
    let mut last_level = 0;

    while to_visit_queue.len() > 0 {
        let current_node_level = to_visit_queue.pop_front().unwrap();
        let children_level = current_node_level.level + 1;

        if current_node_level.node.left.is_some() {
            to_visit_queue.push_back(NodeLevel {
                node: *current_node_level.node.left.unwrap(),
                level: children_level,
            })
        }
        if current_node_level.node.right.is_some() {
            to_visit_queue.push_back(NodeLevel {
                node: *current_node_level.node.right.unwrap(),
                level: children_level,
            })
        }
        if current_node_level.level != last_level {
            if last_sum < minimum_sum {
                minimum_sum = last_sum;
                ms_level = last_level
            }
            last_sum = current_node_level.node.data;
            last_level = current_node_level.level;
        } else {
            last_sum = last_sum + current_node_level.node.data
        }
    }

    if last_sum < minimum_sum {
        // minimum_sum = last_sum;
        ms_level = last_level;
    }

    Ok(ms_level)
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

    match given_binary_tree_return_level_with_minimum_sum(&root) {
        Ok(int) => println!("result: {int:?}"),
        Err(e) => println!("error: {e:?}"),
    }
}
