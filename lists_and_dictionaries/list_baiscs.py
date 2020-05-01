# Learning about lists

spam = ["cat", "bat", "rat", "elephant"]

print(spam)

print(spam[1])

print(f"the {spam[0]} ate the {spam[1]} and made friends with a {spam[2]}, while dancing with an {spam[3]}")


spam1 = [["car", "bike"], ["duck", "cheese"], [1, 2, 3, 4, 5, 6]]

print(spam1[0][1])
print(spam1[1][1])
print(spam[1:3]) # This slices the list up and displays the values inbetween the two indexes

spam2 = [10, 20, 30]
spam2[1] = "Hello"

print(spam2)

spam2[0:3] = ["Pill", "Cap", "Mouth"]
print(spam2)

del spam2[0]
print(spam2)

# you can do to lists, what you can do to strings pretty much
mylist = list("Hello")
print(mylist)
name = "Milo"
print(name[2])

# lets write a function
def eggs(someParameter):
    someParameter.append("Hello")

spam3 = [1, 2, 3, 4]

eggs(spam3)

print(spam3)
