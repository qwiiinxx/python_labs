line = input()


for i in range(len(line)):
    if line[i].isupper():
        first_w = i
        break
else:
    exit()

for i in range(len(line) - 1):
    if line[i].isdigit():
        second_w = i + 1
        break
else:
    exit()

interval = second_w - first_w

real_word = []
pos = first_w
while pos < len(line):
    real_word.append(line[pos])
    if line[pos] == ".":
        break
    pos += interval

print("".join(real_word))
