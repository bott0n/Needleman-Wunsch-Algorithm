# Needleman-Wunsch-Algorithm
Usage:
```python
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
x = 'GAATTCAATACTCCACTTTCCATTCTGTTCAAAGGTCACGTATAGTCCTGGGAATACTCAGGGTTCTCACTTCATGGCTATGCAGGTATTTGTTCCCACA'
y = 'GAATTATACTCCACTTTCCAATGTGTAAAGGTCACTATATCCTGGCATAC'

local_align(x, y, score=ScoreParam(-4, -3))
# return 
# ('GAATTCAATACTCCACTTTCCAT-TC-TGTTCAAAGGTCACGTATAGTCCTGGG-AATAC', 
# GAATT--ATACTCCACTTTCCA-AT-GTG-T-AAAGGTCAC-TATA-TCCT-GGC-ATAC')
global_align(x, y, score=ScoreParam(-4, -3))
# return 
# ('GAATTCAATACTCCACTTTCCAT-TC-TGTTCAAAGGTCACGTATAGTCCTGGGAATACTCAGGGTTCTCACTTCATGGCTATGCAGGTATTTGTTCCCACA', 
# 'GAATT--ATACTCCACTTTCCA-AT-GTG-T-AAAGGT--C----A---C------TA-T-A------T--C--C-T-G----GC----A-----T---AC-')
```
