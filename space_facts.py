print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print("Mars occures " + str(temperatures.count("Mars")) + " times")
print("Moon occures " + str(temperatures.count("Moon")) + " times")


# case insensitive uper case and lower case:
print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())
#

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)