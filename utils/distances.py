def manhattan (point1, point2):
    d_x = abs(point2[0] - point1[0])
    d_y = abs(point2[1] - point1[1])
    return d_x + d_y


def euclidean(a, b):
    return ((b[0] - a[0])**2 + (b[1] - a[1])**2) ** 0.5