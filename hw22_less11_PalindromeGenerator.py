def palindrome(numb):
    for n in range(11, numb + 1):
        if str(n) == str(n)[::-1]:
            yield n


number = 122
for num in palindrome(number):
    print(num)
