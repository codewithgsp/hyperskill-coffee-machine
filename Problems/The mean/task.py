total = 0
count = 0
while True:
    num = input()
    if num == '.':
        break
    total += int(num)
    count += 1
print(total / count)
