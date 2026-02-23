from model import Property


def main():
    p1 = Property("Main Street 10", 75, 120000, False)

    print(p1)


    p2 = Property("Main Street 10", 75, 120000, False)
    print("p1 == p2:", p1 == p2)


    p1.price = 130000
    print("Новая цена:", p1.price)


    print("Цена с налогом:", p1.total_value_with_tax(10))


    p1.deactivate()
    print("Активность:", p1.is_active)


    try:
        p1.price = 200000
    except Exception as e:
        print("Ошибка:", e)


    try:
        bad = Property("", -50, 0, True, 100)
    except Exception as e:
        print("Ошибка создания:", e)


    print("Agency:", Property.agency_name)
    print("Agency через объект:", p1.agency_name)


if __name__ == "__main__":
    main()