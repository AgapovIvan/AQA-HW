from address import Address
from mailing import Mailing

to_address = Address("123456", "City1", "Street1", "1", "A")
from_address = Address("654321", "City2", "Street2", "2", "B")

mailing_instance = Mailing(to_address, from_address, 100.0, "ABC123")

print(f"Отправление {mailing_instance.track} из "
      f"{to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} "
      f"в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. "
      f"Стоимость {mailing_instance.cost} рублей.")
