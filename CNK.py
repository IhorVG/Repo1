import sys
sys.setrecursionlimit(2000)

def C_n_k(n,k):
    if k==0 or k == n:
        return 1
    else:
        return C_n_k(n-1,k)+C_n_k(n-1,k-1)

print(C_n_k(5,2))