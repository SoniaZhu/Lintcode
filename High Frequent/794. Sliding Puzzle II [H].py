from collections import deque
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)

        queue = deque([source])
        visited = set([source])
        step = -1

        while queue:
            step += 1
            for _ in range(len(queue)):
                now = queue.popleft()
                if now == target:
                    return step
                for neighbor in self.get_neighbors(now):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
        return -1

    def matrix_to_string(self, matrix):
        res = []
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                res.append(str(matrix[x][y]))
        return "".join(res)

    def get_neighbors(self, seq):
        neighbors = []
        index = seq.find('0')
        x, y = index // 3, index % 3
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > 2 or ny < 0 or ny > 2:
                continue
            neighbor = list(seq)
            neighbor[nx * 3 + ny], neighbor[index] = neighbor[index], neighbor[nx * 3 + ny]
            neighbors.append(''.join(neighbor))
        return neighbors
