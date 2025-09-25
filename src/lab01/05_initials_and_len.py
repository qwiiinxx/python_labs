name = input().strip()
name = ' '.join(name.split())
name2 = name.split()


tab_counter = name.count(' ')
initials = ''.join(word[0].upper()for word in name2) + '.'


print(f"ФИО: {name}")
print(f"Инициалы: {initials}")
print(f"Длина: {len(name)}")
