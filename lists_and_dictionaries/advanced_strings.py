# We know tha twe can use both single quotes and double quotes for strings
string1 = 'Hello there!'
string2 = "General Kenobi"

# We can also use escape charaters to specify strings. This is useful
# for example when you need to include double quotes in your text.
string3 = 'Say hi to Bob\'s mother'
print(string3)
string4 = 'Mike said, \"Say hi to bob\'s mother\"'
print(string4)

# If you dont want backslashes clutering up your code, you can use a raw string
# A raw string just uses an r before the string, r''
string5 = r'Hello there! I am Carol\'s cat'

# You can use multi-line strings if you dont fancy using multiple \n for new lines
# These use a triple quote set up """
# triple quote allows you to enter new lines without having to use \n
string6 = """Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary and extortion.

Sincerly,

Mad Milo"""

print(string6)