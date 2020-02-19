for num in range(1,100):
    s = ""
    if num % 3 == 0:
        s = s + "Fizz"
    elif num % 5 == 0:
        s = s + "Buzz"
    elif (num % 3 == 0 & num % 5 == 0):
        s += s + "FizzBuzz"
    elif (num % 3 != 0 & num % 5 != 0):
        s += s + str(num)
    print(s)