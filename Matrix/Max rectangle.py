'''
Max rectangle

    Time Complexity:
    - The function largestRectangleArea runs in O(m) time for each row, where m is the number of columns.
      - Each index is pushed and popped from the stack at most once.
    - The function maxRectangle iterates over n rows, and for each row, calls largestRectangleArea.
      - So overall time complexity is O(n * m), where n is the number of rows and m is the number of columns.
    
    Space Complexity:
    - The space used is O(m) for the heights array and O(m) for the stack in largestRectangleArea.
    - So overall space complexity is O(m).
    
    Reasoning:
    - The algorithm builds a histogram for each row and computes the largest rectangle in a histogram efficiently using a stack.
    - No extra space is used except for arrays proportional to the number of columns.
'''
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