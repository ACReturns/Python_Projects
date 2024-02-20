import time

def MultiplePower(A, B):
    powerOf = A ** B
    return powerOf

X = 5
Y = 10
Z = 20

if Y > Z:
    print(MultiplePower(Y, Z))
elif Y > X:
    print(MultiplePower(Y, X))
else:
    print(MultiplePower(X, Z))
time.sleep(.5)
dictionary = {'Monitor' : 'Hardware', 'Water' : 'Liquid', 'Choco' : 'Dog'}

for item in dictionary:
    if item == dictionary['Choco']:
        print('Its bedtime buddy!')
    time.sleep(.5)

# revisit and figure out how the while loop is supposed to work
