J = 50;
K = 5;
B = 20;
name = 'Ashley';

print (J + K)

if J > 25:
    print('J is the winner!')

if (B == 20):
    print('20 is equal to B')

print(name.upper())
print(name.lower())
print (name[0])
print (name[2])

listA = ['mother', 'father', '1970', '1965'];
print (listA[3]);

tupA = ("brother", "sister", "1990", "1992", "1993", "1995")
print (tupA[1:4])

date = "3/13/2021"
split_the_date = date.split('/')
print(split_the_date)
print(split_the_date[0])
print(split_the_date[1])
print(split_the_date[2])

print("Month: " + split_the_date[0])
print("Day: " + split_the_date[1])
print("Year: " + split_the_date[2])

date = "12/25/2025"
full_date = date.split('/')
print('Month: ' + full_date[0] + ' Day: ' + full_date[1] + ' Year: ' + full_date[2])

Name = "Jack"
print(Name.swapcase())

Color1 = '  red  ';
Color2 = '  blue  ';
print('My favorite colors are ' + Color1 + ' and ' + Color2)
print('Let\'s fix formatting...')
print('My favorite colors are ' + Color1.strip() + ' and ' + Color2.strip())


