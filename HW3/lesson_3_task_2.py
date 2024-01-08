from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79123456789"),
    Smartphone("Apple", "iPhone 12", "+79234567890"),
    Smartphone("Google", "Pixel 5", "+79345678901"),
    Smartphone("Huawei", "P40 Pro", "+79456789012"),
    Smartphone("OnePlus", "8T", "+79567890123"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
