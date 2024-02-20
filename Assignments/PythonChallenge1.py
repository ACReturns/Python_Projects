import time

def WriteStuff(word):
    word = 'Squiggly'
    return str(word)

Name = 'Don'
Age = 38
Height = 5.11

print('Name: ', Name)
print('Age: ', Age)
print('Height: ', Height)
time.sleep(.5)

print('38 + 2: ', Age + 2)
print('Multiply 5 * 5: ', 5 * 5)
print('2 / 20: ', 2 / 20)
print('is 9 == 9: ',9 == 9)
print('9 % 3: ', 9 % 3)
time.sleep(.5)

if Age < 40:
    print('Your still pretty young!')

if Name == 'Dan':
    print('Hi Dan!')
elif Name == 'Don':
    print('Still here!')

if Height == 4.11:
    print('Tiny tot!')
elif Height == 5.4:
    print('still a shorty')
else:
    print('Giant inbound')
time.sleep(.5)

Gundam_list = ['gundam', 'zaku', 'gouf', 'master', 'horse']
for Gundam in Gundam_list:
    print(Gundam)
    time.sleep(.5)

counter = 3
while counter > 0:
    print(counter)
    counter = counter - 1
    time.sleep(.5)

newString = ''
print(WriteStuff(newString))


    

