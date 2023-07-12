print("Moon" in "This text will describe facts about the Moon")

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print("Mars occures " + str(temperatures.count("Mars")) + " times")
print("Moon occures " + str(temperatures.count("Moon")) + " times")