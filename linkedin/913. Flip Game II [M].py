# mem with standard answer
# cannot guarantee a win = I tried everything but the opponent can guarantee a win
# guarantee a win = there is a move that the opponent cannot guarantee a win
class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    mem = dict()
    def canWin(self, s):
        if s in self.mem:
            return self.mem[s]
        res = any(not self.canWin(s[:i]+"--"+s[i+2:]) for i in range(len(s)-1) if s[i:i+2] == "++")
        self.mem[s] = res
        return res

# mostly the same
class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s, memo = {}):
        # write your code here
        if s in memo:
            return memo[s]
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                tmp = s[:i]+'--'+s[i+2:]
                flag = self.canWin(tmp)
                memo[tmp] = flag
                if not flag:
                    return True
        return False

## Mine. beats 67.19%Submissions. I don't understand myself
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
