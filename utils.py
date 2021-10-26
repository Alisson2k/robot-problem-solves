from matrix import Matrix

def read_matrix_by_file(filename) -> Matrix:
    my_file = open(filename, 'rb')

    content = []
    for line in my_file:
        str_line = line.decode("utf-8").replace('\n', '').replace('[', '').replace(']', '')
        values = str_line.split('  ')
        content.append(list(map(lambda x: int(x), values)))

    my_file.close()

    size = len(content)
    m = Matrix(size)
    m.content = content
    m.cans_indexed = m._create_indexed_array()

    for i in range(size):
        for j in range(size):
            if m.is_can((i, j)):
                m.cans.append((i, j))

    return m