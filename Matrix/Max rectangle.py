# Max rectangle

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    heights.pop()
    return max_area


def maxRectangle(mat):
    if not mat:
        return 0

    n = len(mat)
    m = len(mat[0])
    heights = [0] * m
    max_area = 0

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        max_area = max(max_area, largestRectangleArea(heights))

    return max_area

mat = [[0, 1, 1, 0],[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 0, 0]]
print("Maximum rectangle area is:", maxRectangle(mat))