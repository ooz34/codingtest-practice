def solution(A):
  if not A:
    return 1

  return sum(range(1, len(A) + 2)) - sum(A)

# O(N) or O(N * log(N))