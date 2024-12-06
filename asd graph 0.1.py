with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    array = [0] * n
    for _ in range(1,n):
        u, v = map(int, file.readline().split())
        array[v - 1] = u

with open('output.txt', 'w') as output_file:
    output_file.write(' '.join(map(str, array)) + '\n')