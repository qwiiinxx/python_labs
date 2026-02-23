
class Property:
    """
    Класс недвижимости
    """

    # Атрибут класса
    agency_name = "Dream Estate"

    def __init__(
        self,
        address: str,
        area: float,
        price: float,
        for_rent: bool,
        rent_term: int | None = None
    ) -> None:

        self._validate_address(address)
        self._validate_area(area)
        self._validate_price(price)
        self._validate_rent_logic(for_rent, rent_term)

        self._address = address
        self._area = float(area)
        self._price = float(price)
        self._for_rent = for_rent
        self._rent_term = rent_term
        self._is_active = True


    # Валидация
    def _validate_address(self, address: str) -> None:
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой")
        if not address.strip():
            raise ValueError("Адрес не должен быть пустой")

    def _validate_area(self, area: float) -> None:
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь должна быть числом")
        if area <= 0:
            raise ValueError("AПлощадь должна быть больше 0")

    def _validate_price(self, price: float) -> None:
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if price <= 0:
            raise ValueError("Цена должна быть больше 0")

    def _validate_rent_logic(self, for_rent: bool, rent_term: int | None) -> None:
        if not isinstance(for_rent, bool):
            raise TypeError("Параметр for_rent должен быть булевым")

        if for_rent:
            if rent_term is None:
                raise ValueError("Недвижимость должна иметь срок аренды")
            if not isinstance(rent_term, int):
                raise TypeError("Срок аренды должен быть целым числом")
            if rent_term <= 0 or rent_term > 60:
                raise ValueError("Срок аренды должен быть в диапазоне от 0 до 60 месяцев")
        else:
            if rent_term is not None:
                raise ValueError("Срок аренды должен быть None потому что объект только для продажи")


    # PROPERTIES
    @property
    def address(self) -> str:
        return self._address

    @property
    def area(self) -> float:
        return self._area

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        if not self._is_active:
            raise RuntimeError("Cannot change price of inactive property")

        self._validate_price(new_price)
        self._price = float(new_price)

    @property
    def is_active(self) -> bool:
        return self._is_active


    # Бизнес-методы
    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    def total_value_with_tax(self, tax_percent: float) -> float:
        """
        Возвращает цену с налогом.
        """
        if not isinstance(tax_percent, (int, float)):
            raise TypeError("Tax must be numeric")

        if tax_percent < 0:
            raise ValueError("Tax cannot be negative")

        return self._price * (1 + tax_percent / 100)


    # Обязательные методы
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Property):
            return False

        return (
            self._address == other._address and
            self._area == other._area and
            self._price == other._price
        )

    def __str__(self) -> str:
        status = "Active" if self._is_active else "Inactive"
        rent_info = (
            f", Rent term: {self._rent_term} months"
            if self._for_rent else ""
        )

        return (
            f"{self._address} | "
            f"{self._area:.2f} m² | "
            f"{self._price:,.2f} USD"
            f"{rent_info} | "
            f"Status: {status}"
        )

    def __repr__(self) -> str:
        return (
            f"Property("
            f"address={self._address!r}, "
            f"area={self._area}, "
            f"price={self._price}, "
            f"for_rent={self._for_rent}, "
            f"rent_term={self._rent_term}"
            f")"
        )


