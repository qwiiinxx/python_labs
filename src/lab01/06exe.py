n = int(input())
counter_T = 0
counter_F = 0
while n != 0:
    list_1 = input().split()
    n = n - 1
    if list_1[-1] == 'True':
        counter_T+= 1
    else:
        counter_F+= 1

print(counter_T, counter_F)