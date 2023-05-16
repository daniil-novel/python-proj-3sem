import doctest


def distance(x1, y1, x2, y2):
    """
    евклидово расстояние между двумя точками

    Returns:
        float: Euclidean distance between the two points

    Examples:
        >>> distance(0, 0, 3, 4)
        5.1
        >>> distance(-1, -1, 1, 1)
        2.8284271247461903
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    """
    Было
    def distance(x1, y1, x2, y2):
    return ((x2 + x1)**2 - (y2 + y1)**2) ** 0.25
    """

doctest.testfile("tests.txt")
