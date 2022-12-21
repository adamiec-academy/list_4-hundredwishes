def info(data):
    for row in data:
        for element in row:
            print(element, end="")
        print()

def border_map(a,b):
    mapa = []
    for i in range(b):
        if (i == 0) or ((i+1) == b):
            row = ["X" for _ in range(a)]
            mapa.append(row)
        else:
             row = ["." for _ in range(a-2)]
             row.insert(0,"X")
             row.append("X")
             mapa.append(row)
    return mapa
