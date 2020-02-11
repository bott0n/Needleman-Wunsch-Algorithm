class ScoreParam:
    
    def __init__(self, gap, mismatch):
        self.gap = gap
        self.mismatch = mismatch
    def match(self, chr):
        if chr == 'A':
            return 3
        elif chr == 'C' or chr == 'T':
            return 2
        else:
            return 1

def global_align(x, y, score=ScoreParam(-4, -3)):
   
    A = []
    for i in range(len(y) + 1):
        A.append([0] * (len(x) +1))
    for i in range(len(y)+1):
        A[i][0] = score.gap * i
    for i in range(len(x)+1):
        A[0][i] = score.gap * i
    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):
           
            A[i][j] = max(
            A[i][j-1] + score.gap,
            A[i-1][j] + score.gap,
            A[i-1][j-1] + (score.match(y[i-1]) if y[i-1] == x[j-1] else score.mismatch)
            )

    align_X = ""
    align_Y = ""
    i = len(x)
    j = len(y)

    while i > 0 or j > 0:
         
        current_score = A[j][i]

        if i > 0 and j > 0 and x[i - 1] == y[j - 1]:
            align_X = x[i - 1] + align_X
            align_Y = y[j - 1] + align_Y
            i = i - 1
            j = j - 1
         
        elif i > 0 and (current_score == A[j][i - 1] + score.mismatch or current_score == A[j][i - 1] + score.gap):
            align_X = x[i - 1] + align_X
            align_Y = "-" + align_Y
            i = i - 1
             
        else:
            align_X = "-" + align_X
            align_Y = y[j - 1] + align_Y
            j = j - 1
   
    return (align_X, align_Y)


# x = 'GAATTCAATACTCCACTTTCCATTCTGTTCAAAGGTCACGTATAGTCCTGGGAATACTCAGGGTTCTCACTTCATGGCTATGCAGGTATTTGTTCCCACA'
# y = 'GAATTATACTCCACTTTCCAATGTGTAAAGGTCACTATATCCTGGCATAC'

# a = global_align(x, y, score=ScoreParam(-4, -3))
# print(a)