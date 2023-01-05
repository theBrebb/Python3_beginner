def fizz_buzz(input1):
    if input1 % 3 == 0 and input1 % 5 == 0:
        return "FizzBuzz"

    elif input1 % 5 == 0:
        return "buzz"
    elif input1 % 3 == 0:
        return "fizz"
    else:
        return input1


# print(fizz_buzz(13))


# def fizz_buzz(number):
#     (if number % 3 == 0) and (number % 5 == 0):
#         return fizz_buzz
#     if number % 3 == 0:
#         return "Fizz"
#     if number % 5 == 0:
#         return "Buzz"
#     return number


print(fizz_buzz(1298543010))
