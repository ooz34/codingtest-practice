def solution(A):
  set_A = set(A)

  for i in range(1, 1000001):
    if i not in set_A:
      return i

  return 1000001

# O(N) or O(N * log(N))