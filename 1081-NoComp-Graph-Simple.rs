fn given_graph_and_position_and_new_color_change_graph(
    graph: &mut [Box<[char]>],
    position: [usize; 2],
    new_color: char,
) -> Result<i32, &'static str> {
    let old_color = graph[position[0]][position[1]];
    if old_color == new_color {
        return Ok(1);
    }
    let mut visited: Vec<Vec<bool>> = vec![];
    for i in 0..graph.len() {
        visited.push(vec![false; graph[i].len()]);
    }

    let mut list_to_visit = vec![position];
    let mut first_adjacent_positions =
        generate_possible_adjacent_positions(graph, position, old_color);
    list_to_visit.append(&mut first_adjacent_positions);
    for i in 0..list_to_visit.len() {
        visited[list_to_visit[i][0]][list_to_visit[i][1]] = true;
    }

    while list_to_visit.len() > 0 {
        let current_position = list_to_visit.pop().unwrap();
        graph[current_position[0]][current_position[1]] = new_color;

        let mut nth_adjacent_positions: Vec<[usize; 2]> =
            generate_possible_adjacent_positions(graph, current_position, old_color)
                .into_iter()
                .filter(|i| visited[i[0]][i[1]] == false)
                .collect();
        for i in 0..nth_adjacent_positions.len() {
            visited[nth_adjacent_positions[i][0]][nth_adjacent_positions[i][1]] = true;
        }
        list_to_visit.append(&mut nth_adjacent_positions);
    }

    Ok(1)
}

fn generate_possible_adjacent_positions(
    graph: &mut [Box<[char]>],
    position: [usize; 2],
    target_color: char,
) -> Vec<[usize; 2]> {
    let mut result = vec![];
    let mut adjacent_positions = generate_adjacent_positions(position);
    result.append(&mut adjacent_positions);

    return result
        .into_iter()
        .filter(|i| {
            (i[0] >= 0 && i[0] < graph.len() as i32)
                && (i[1] >= 0
                    && i[1] < graph[i[0] as usize].len() as i32
                    && (graph[i[0] as usize][i[1] as usize] == target_color))
        })
        .map(|x| [x[0] as usize, x[1] as usize])
        .collect();
}

fn generate_adjacent_positions(position: [usize; 2]) -> Vec<[i32; 2]> {
    return vec![
        [position[0] as i32 - 1, position[1] as i32 - 1],
        [position[0] as i32 - 1, position[1] as i32],
        [position[0] as i32 - 1, position[1] as i32 + 1],
        [position[0] as i32, position[1] as i32 - 1],
        [position[0] as i32, position[1] as i32 + 1],
        [position[0] as i32 + 1, position[1] as i32 - 1],
        [position[0] as i32 + 1, position[1] as i32],
        [position[0] as i32 + 1, position[1] as i32 + 1],
    ];
}

fn main() {
    let mut graph: [Box<[char]>; 4] = [
        Box::new(['B', 'B', 'W']),
        Box::new(['W', 'W', 'W']),
        Box::new(['W', 'W', 'W']),
        Box::new(['B', 'B', 'B']),
    ];

    let position = [2, 2];
    let new_color = 'G';
    match given_graph_and_position_and_new_color_change_graph(&mut graph, position, new_color) {
        Ok(_) => println!("result: {graph:?}"),
        Err(e) => println!("error: {e:?}"),
    }
}
