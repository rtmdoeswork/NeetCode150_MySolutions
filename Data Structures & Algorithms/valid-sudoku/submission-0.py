class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                num = board[r][c]
                
                if num in rows[r] or num in columns[c] or num in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(num)
                columns[c].add(num)
                squares[(r // 3, c // 3)].add(num)
        return True