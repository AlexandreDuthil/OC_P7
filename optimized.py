

def optimized_POO(actions, W):
    n = len(actions)
    mat = [[0 for x in range( W + 1 )] for x in range( n + 1 )]

    for i in range( n + 1 ):
        for j in range( W + 1 ):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif actions[i-1].price < j:
                mat[i][j] = max(actions[i-1].profitability + mat[i-1][j-actions[i-1].price], mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]
    return mat[n][W]


# TODO : enlever la notion de POO pour pouvoir comparer avec et sans
def optimized(actions, W):
    n = len(actions)
    mat = [[0 for x in range( W + 1 )] for x in range( n + 1 )]

    for i in range( n + 1 ):
        for j in range( W + 1 ):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif actions[i-1].price < j:
                mat[i][j] = max(actions[i-1].profitability + mat[i-1][j-actions[i-1].price], mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]
    return mat[n][W]
