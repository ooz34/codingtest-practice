def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    idx_stack = []
    for i, n in enumerate(numbers):
        while idx_stack and n > numbers[idx_stack[-1]]:
            top_idx = idx_stack.pop()
            answer[top_idx] = n
        idx_stack.append(i)
    return answer