line = input()
real_word = []


for i in range(len(line)):
    if line[i].isupper():
        real_word.append(line[i])
        first_w = i
        break
    else:
        exit()

for i in range(len(line) -1):
    if line[i].isdight():
        second_w = i+1
        break
    else:
        exit()

interval = second_w - first_w


