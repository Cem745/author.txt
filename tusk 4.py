a = [int(input())for i in range (4)]
m = sorted(a)[len(a) // 2]
print(sum(abs(v - m) for v in a))
