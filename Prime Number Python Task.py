prime_number = []
prime_number.append(2)
prime_number.append(3)
prime_number.append(5)
prime_number.append(7)
for i in range(10,100):
    if(i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
        prime_number.append(i)
print(prime_number);
