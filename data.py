from faker import Faker

fake = Faker("uk_UA")


def input_data(x):
    data = {}
    for i in range(0, x):
        data[i] = [fake.name(), fake.phone_number(), fake.date_of_birth(), fake.ascii_free_email(), fake.address()]
    return data


for i in input_data(10).values():
    print(i)
