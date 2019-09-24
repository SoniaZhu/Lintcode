## Mine. beats 67.19%Submissions
class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s):
        self.mem = dict()
        return self.canWinHelper(1, list(s))

    def canWinHelper(self, move, currentState):
        if (move % 2, ''.join(currentState)) in self.mem:
            return self.mem[(move % 2, ''.join(currentState))]
        # moveIndexes = self.possibleMoveIndexs(currentState)
        # if not moveIndexes:
        #     return move % 2 == 0

        for idx in range(len(currentState) - 1):
            if currentState[idx : idx + 2] != ['+', '+']:
                continue
            currentState[idx : idx + 2] = ['-', '-']
            canWin = self.canWinHelper(move + 1, currentState)
            self.mem[((move + 1) % 2, ''.join(currentState))] = canWin
            currentState[idx : idx + 2] = ['+', '+']

            if move % 2 == 0 and not canWin:
                return False
            if move % 2 == 1 and canWin:
                return True
        return move % 2 == 0

    # def possibleMoveIndexs(self, currentState):
    #     res = []
    #     for i in range(len(currentState) - 1):
    #         if currentState[i : i + 2] == ['+', '+']:
    #             res.append(i)
    #     return res
