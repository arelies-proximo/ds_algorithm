

INF = 9999
#printing the solution
def print_solution(num_vertices, distance):
    print('\nSolution with Floyd Warshall Algorithm:\n\n')
    for i in range(num_vertices):
        for j in range(num_vertices):
            if distance[i][j] == INF:
                print('INF', end=' ')
            else:
                print(distance[i][j], end = ' ')
        print(' ')
    print('\n\n')


def floyd_warshall(num_vertices, G):
    distance = G
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    print_solution(num_vertices, distance)


custom_graph = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 0]
]

floyd_warshall(4, custom_graph)
