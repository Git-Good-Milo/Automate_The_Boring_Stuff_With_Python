import sys, pyperclip

# print("Hello")
# sys.exit()
# # sys.exit prevents the program from completing. Hence, Hello will be printed but not Goodbye
# print("Goodbye")

# pyperclip helps you edit text by using functions such as copy and paste
statement = "Hello World"
pyperclip.copy(statement)
print(pyperclip.paste())

# Lets write a function of our own
def hello(name):
    print("Howdy! " + name)
    print("Howdy!!! " + name)
    print("Hello there. " + name)

hello("Milo")
hello("Swag daddy")