

def given_graph_and_position_and_new_color_change_graph(graph, position, new_color):
    old_color = graph[position[0]][position[1]]
    if old_color is new_color:
        return
    visited = [[False for j in range(len(graph[i]))]
               for i in range(len(graph))]
    list_to_visit = [position]
    list_to_visit.extend(
        generate_possible_adjacent_positions(graph, position, old_color))
    for v in list_to_visit:
        visited[v[0]][v[1]] = True

    while list_to_visit:
        current_position = list_to_visit.pop()
        graph[current_position[0]][current_position[1]] = new_color

        new_list_to_visit = list(filter(lambda v: visited[v[0]][v[1]] is False, generate_possible_adjacent_positions(
            graph, current_position, old_color)))
        for v in new_list_to_visit:
            visited[v[0]][v[1]] = True
        list_to_visit.extend(new_list_to_visit)


def generate_possible_adjacent_positions(graph, position, target_color):
    return list(filter(lambda index: (index[0] >= 0 and index[0] < len(graph)) and (
        index[1] >= 0 and index[1] < len(graph[index[0]]) and (graph[index[0]][index[1]] is target_color)), generate_adjacent_positions(position)))


def generate_adjacent_positions(position):
    return [[position[0]-1, position[1]-1],
            [position[0]-1, position[1]],
            [position[0]-1, position[1]+1],
            [position[0], position[1]-1],
            [position[0], position[1]+1],
            [position[0]+1, position[1]-1],
            [position[0]+1, position[1]],
            [position[0]+1, position[1]+1], ]


graph = [['B', 'B', 'W'],
         ['W', 'W', 'W'],
         ['W', 'W', 'W'],
         ['B', 'B', 'B']]
position = [2, 2]
new_color = 'G'

given_graph_and_position_and_new_color_change_graph(graph, position, new_color)
for i in graph:
    print('\t'.join(map(str, i)))
