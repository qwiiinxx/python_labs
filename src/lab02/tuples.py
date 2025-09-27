def format_record(rec: tuple[str, str, float]):
    fio, group, gpa = rec

    if not isinstance(rec, tuple) or len(rec) != 3:           # ошибки на данные
        raise ValueError("нужен кортеж из 3-х элементов")

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("данные должны быть строкой")
    
    if not isinstance(gpa, float):
        raise TypeError("данные должны быть вещественным числом")



    if not fio:                                              # ошибки на пустоту
        raise ValueError("нельзя оставлять пустым")

    if not group:
        raise ValueError("нельзя оставлять пустым")
    
    if not gpa:
        raise ValueError("нельзя оставлять пустым")
    
    parts = fio.strip().split()                        # ['иванов', 'иван', 'иванович']
    if len(parts) < 2:
        raise ValueError("должны быть хотя бы фамилия и имя")

    surname = parts[0].title()                                      # [Иванов]
    initials = "".join(p[0].upper() + '.' for p in parts[1:])       # "Иванов И.И."

    group = group.strip()

    gpa = f"{float(gpa):.2f}"
    return f"{surname} {initials}, гр. {group}, GPA {gpa}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4)))







# print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
# print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))