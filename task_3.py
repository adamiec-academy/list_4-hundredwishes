def min_max(data):
    if data[0] < data[1]:
        smol = data[0]
        big = data[1]
    else:
        smol = data[1]
        big = data[0]
    for i in range(2,len(data)):
        elem = data[i]
        if elem >= big:
            big = elem
        elif elem <= smol:
            smol = elem
    return smol, big
