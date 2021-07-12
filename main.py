import random
import string
import sys
from faker import Faker

numberOfRecords = int(sys.argv[1])
fake = Faker()
car_makes = ["Abarth",
  "Alfa Romeo",
  "Aston Martin",
  "Audi",
  "Bentley",
  "BMW",
  "Bugatti",
  "Cadillac",
  "Chevrolet",
  "Chrysler",
  "Citroën",
  "Dacia",
  "Daewoo",
  "Daihatsu",
  "Dodge",
  "Donkervoort",
  "DS",
  "Ferrari",
  "Fiat",
  "Fisker",
  "Ford",
  "Honda",
  "Hummer",
  "Hyundai",
  "Infiniti",
  "Iveco",
  "Jaguar",
  "Jeep",
  "Kia",
  "KTM",
  "Lada",
  "Lamborghini",
  "Lancia",
  "Land Rover",
  "Landwind",
  "Lexus",
  "Lotus",
  "McLaren",
  "Mercedes-Benz",
  "MG",
  "Mini",
  "Mitsubishi",
  "Morgan",
  "Nissan",
  "Opel",
  "Peugeot",
  "Porsche",
  "Renault",
  "Rolls-Royce",
  "Rover",
  "Saab",
  "Seat",
  "Skoda",
  "Smart",
  "SsangYong",
  "Subaru",
  "Suzuki",
  "Tesla",
  "Toyota",
  "Volkswagen",
  "Volvo"]

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

for i in range(numberOfRecords):
#    n = random.randint(0, 22)
    customer_name = fake.name()
    vehicle_make = random.choice(car_makes)
    vehicle_model = random_string(10)
    vehicle_vin = random.randint(100000, 999999)
    vehicle_year = random.randint(1985, 2021)
    invoice_price = round(random.uniform(00.00, 999.99), 2)
    invoice_date = random_string(10)
    invoice_payment_method = random_string(10)
    invoice_order_number = random.randint(10000000, 99999999)

    print(customer_name + " , " + vehicle_make + " , " + vehicle_model + " , " + str(vehicle_vin) + " , " + str(vehicle_year) + " , " + str(invoice_price) + " , " + invoice_date + " , " + invoice_payment_method + " , " + str(invoice_order_number))
