name = input().strip()
name2 = name.split()

initials = ''.join(word[0].upper()for word in name2) + '.'

print(f"ФИО: {name}")
print(f"Инициалы: {initials}")
print(f"Длина: {len(name)}")


