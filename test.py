from faker import Faker

fake = Faker('ru_RU')


for i in range(9):
    if i % 2:
        print(fake.first_name_female() + ' ' + fake.last_name_female())
    else:
        print(fake.first_name_male() + ' ' + fake.last_name_male())
