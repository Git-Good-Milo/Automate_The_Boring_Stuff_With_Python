# def div42by(divideby):
#     try:
#         return 42 / divideby
#     except ZeroDivisionError:
#         print("Error: You tried to divide by zero.")
#
# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))

print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("Thats a lot of cats!")
    else:
        print("Thats not that many cats...")
except ValueError:
    print("You did not enter a number dipshit")