class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map_ = defaultdict(list)
        n_ = len(board)

        for i in range(n_):
            for j in range(n_):
                value = board[i][j]
                if value != ".": #find a number
                    for loc_ in map_[value]:
                        if (loc_[0] == i) or (loc_[1] == j) or (loc_[0] // 3 == i //3 and loc_[1] // 3 == j // 3):
                            return False
                    map_[value].append([i,j])
        

        return True