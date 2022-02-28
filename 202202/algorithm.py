import math

# 任意正整数转连续整数之和
N = 121
for i in range(1, int(math.sqrt(2 * N)) + 1):

    if not (2 * N) % i:
        m, n = i, int((2 * N) / i)
        # print(m, n)
        if not (m + n - 1) % 2:
            y = int((m + n - 1) / 2)
            # print("y", y)

            x = max(m, n) - y
            # print("x", x)
            start = min(x, y)
            end = max(x, y) + 1
            print(N, '=', end=' ')
            for j in range(start, end)[::-1]:
                if j == start:
                    print(j, end='')
                else:
                    print(j, end='+')
            print()

print("*"*14)
# 十进制转九进制
M = 100
H = 0
T = 0
while True:
    if not M:
        break
    s = M % 10
    if s > 4:
        s -= 1
    M = int((M-s)/10)
    H += s * (9 ** T)
    T += 1
print(H)
