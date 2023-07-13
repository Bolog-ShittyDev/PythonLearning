planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)
number_of_planets = len(planets)
print("There are currently:",number_of_planets,"Planets in our Solar System. What was that about Yugoth?")
planets.append("Yugoth/Pluto")
real_number_of_planets = len(planets)
print("The government doesn't want you to know that there are really",real_number_of_planets,"planets in our solar system")
print(planets[-1],"is the last Planet")