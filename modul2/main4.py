numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    for j in range(numbers[i]):
        if (numbers[i] % numbers[j] == 0) and (numbers[i] != numbers[j]) and (numbers[j] != 1):
            not_primes.append(numbers[i])
            break
        elif (numbers[i] % numbers[j] != 0) or (numbers[j] != 1):
            primes.append(numbers[i])
            break

print(not_primes)
print(primes)
