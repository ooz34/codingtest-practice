def solution(A):
  N = len(A)

  if len(set(A)) != N:
    return 0

  A.sort()

  if A[0] == 1 and A[-1] == N:
    return 1
  return 0

# O(N) or O(N * log(N))