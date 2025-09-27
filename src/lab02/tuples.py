def format_record(rec):                     # ','.join()
    fio, group, gpa = rec

    if not isinstance(rec, tuple) or len(rec) != 3:
        raise ValueError("нужен кортеж из 3-х элементов")

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("данные должны быть строкой")
    
    if not fio:
        raise ValueError("нельзя оставлять пустым")
    
    group = group.strip()
    if not group:
        raise ValueError("нельзя оставлять пустым")
    
    if not gpa:
        raise ValueError("нельзя оставлять пустым")
    
    if not isinstance(gpa, float):
        raise TypeError("данные должны быть вещественным числом")
    
    parts = fio.strip().split()
    if len(parts) < 2:
        raise ValueError("должны быть хотя бы фамилия и имя")
    

    surname = parts[0].title()
    initials = "".join(p[0].upper() + '.' for p in parts[1:])

    
    
    return parts, group, gpa
    

print(format_record("    иванов иван иванович   ", "BIVT-25", 4.6))