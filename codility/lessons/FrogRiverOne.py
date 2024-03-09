def solution(X, A):
  if len(set(A)) != X:
    return -1

  leaves = set()

  for sec, x in enumerate(A):
    leaves.add(x)

    if len(leaves) == X:
      return sec

#
# O(N)