def flood_fill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image

    def dfs(r, c):
        if (not (0 <= r < len(image) and 0 <= c < len(image[0])) or image[r][c] != oldColor):
            return
        image[r][c] = newColor
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    oldColor = image[sr][sc]
    dfs(sr, sc)
    return image

def main():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc = 1, 1
    newColor = 2
    result = flood_fill(image, sr, sc, newColor)
    print("Flood-filled image:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
