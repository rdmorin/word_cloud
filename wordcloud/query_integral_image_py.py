# Pure-python fallback for query_integral_image (slower than the Cython version).


def query_integral_image(integral_image, size_x, size_y, random_state):
    x, y = integral_image.shape
    hits = []
    max_i = x - size_x
    max_j = y - size_y
    if max_i <= 0 or max_j <= 0:
        return None
    for i in range(max_i):
        row_i = integral_image[i]
        row_isx = integral_image[i + size_x]
        for j in range(max_j):
            area = (row_i[j] + row_isx[j + size_y]
                    - row_isx[j] - row_i[j + size_y])
            if area == 0:
                hits.append((i, j))
    if not hits:
        return None
    idx = random_state.randint(0, len(hits) - 1)
    return hits[idx]
