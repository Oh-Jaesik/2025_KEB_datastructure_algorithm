def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n

n, k = map(int, input().split())
result = []
people = list(range(1, n + 1))

idx = 0
while people:
    idx = (idx + k - 1) % len(people)
    result.append(str(people.pop(idx)))

print(f"<{', '.join(result)}>")
