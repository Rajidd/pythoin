# Data Type

number = 67 # int
num = 78.98 # float
greeting = "Hello there" #str
IsPythonInteresting = True #bool

# A variable storing multiple values
languages = ["Python","PHP","Java"] #list
fruits = ("banana","apple","pineapple") #tuple
countries = {"Kenya","China","North America"} #sets
# Dictionary
details = {
    "firstname": "Brain",
    "age": 17,
    "course": "MIT",
    "natinality": " USA"
}
print(number)
print(IsPythonInteresting)
print(countries)
print(details)
print(details["course"])
print(fruits)

# Determining the data type
print(type(details))
print(type(countries))
print(type(languages))

# Typecasting - converting one data type to another
print(float(number))
print(int(num))