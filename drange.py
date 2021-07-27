def drange(start, stop, step):
    """[summary]

    Args:
        start ([any]): [loop start]
        stop ([any]): [loop end]
        step ([any]): [loop step]

    Yields:
        [any]: [description]
    """
    r = start
    while r < stop:
        yield r
        r += step