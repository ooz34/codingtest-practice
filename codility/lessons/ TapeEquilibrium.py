def solution(A):
  sum1 = 0
  sum2 = sum(A)
  min = 100000000

  for p in range(1, len(A)):
    sum1 += A[p-1]
    sum2 -= A[p-1]
    diff = abs(sum1 - sum2)
    if diff < min:
      min = diff

  return min

# O(N)