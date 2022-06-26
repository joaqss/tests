name_input = input("What is your name? Type here: ")
print("Hi, " + name_input)

birthyear_input = int(input("What year are you born? "))

specifiedyear_input = int(input("Enter a year to know what your age would be on that year: "))

if birthyear_input > specifiedyear_input:
    print("You are not yet born at that time...")

else:
    result = specifiedyear_input - birthyear_input
    print("Your age at that time is " + str(result))
