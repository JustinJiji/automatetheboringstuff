def collatz(number):
    if number % 2==0:
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number + 1

number = int(input('Enter the number: '))
while True:
    number = collatz(number)
    if number==1:
        break

