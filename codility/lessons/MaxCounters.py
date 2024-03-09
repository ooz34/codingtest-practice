def solution(N, A):
  counter = [0 for i in range(N)]
  cur_max = 0
  max_cnt = 0

  for k in A:
    if k == N + 1:
      max_cnt = cur_max
    else:
      if counter[k-1] < max_cnt:
        counter[k-1] = max_cnt
      counter[k-1] += 1
      if cur_max < counter[k-1]:
        cur_max = counter[k-1]

  for i, cnt in enumerate(counter):
    if cnt < max_cnt:
      counter[i] = max_cnt

  return counter

# O(N + M)