from faker import Faker
import random

fake = Faker('en_US')

domain_list=['protonmail.com','gmail.com','protonmail.com','gmail.com','icloud.com','gmail.com','protonmail.com','icloud.com','yahoo.com']
num=random.randrange(50,500)
birthyear=random.randrange(1970, 2000)
for i in range(random.randrange(5,30)):
    gender=random.randrange(0,1)
    num=random.randrange(50,500)
    birthyear=random.randrange(1970, 2000)
    birthdate=str(fake.day_of_week()+', '+fake.month_name()+' '+fake.day_of_month()+', '+str(birthyear))
    city=fake.city()
    state=fake.state_abbr()
    postcode=fake.postcode_in_state(state_abbr=state)
    if gender == 1:
        first=fake.first_name_male()
        last=fake.last_name_male()
        gender="Male"
    else:
        first=fake.first_name_female()
        last=fake.last_name_female()
        gender="Female"
    username = first[0] + last + str(num)
    age=str(2021-birthyear)
    address=fake.street_address()
    email = first[0].lower() + last.lower() + str(num) + str('@') + domain_list[random.randrange(0,8)]
    password=fake.password(length=random.randrange(8,16), special_chars=True, upper_case=True)
    cardnum=fake.credit_card_number()
    cardcode=fake.credit_card_security_code()
    filepath=('/Users/admin/Documents/profiles/')
    with open(username +'.txt','w') as f:
        f.write('First: '+ first)
        f.write('\nLast: '+last)
        f.write('\nGender: '+gender)
        f.write('\nBirthdate: '+birthdate)
        f.write('\nAge: '+age)
        f.write('\nAddress: '+address)
        f.write('\n'+'City: '+city)
        f.write('\nState: '+state)
        f.write('\nCountry: United States')
        f.write('\nPostal: '+ postcode)
        f.write('\nUsername: '+username)
        f.write('\nEmail: '+email)
        f.write('\nPassword: '+password)
        f.write('\nCard Number: '+cardnum)
        f.write('\nCard Security Code: '+cardcode)


