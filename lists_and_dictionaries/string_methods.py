# String methods return new string values. Since strings are imutable, you need to save the new value to a variable if you want to keep it
spam = "Hello world!"
spamUC = spam.upper()
print(spamUC)

# You can chain together multiple methods.

spam2 = "hello".upper().isupper()
print(spam2)