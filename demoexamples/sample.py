def OddEven(n):
    ans = n%2
    if ans == 0:
        return print("The remainder is " + str(ans) + "and it is EVEN")
    else:
        return print("The remainder is" + str(ans) + " and it is Odd")
while True:
    number = int(input("Enter a number:"))
    OddEven(number)