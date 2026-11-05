class Planet:
    # Initialize each planet with its name, classification, and host star.
    def __init__(self, name, planet_type, star):
        # Check that every supplied value is a string before storing it.
        if not all(isinstance(value, str) for value in (name, planet_type, star)):
            raise TypeError("name, planet type, and star must be strings")

        # Reject empty strings so every planet has complete identifying details.
        if any(value == "" for value in (name, planet_type, star)):
            raise ValueError(
                "name, planet_type, and star must be non-empty strings"
            )

        # Store each validated value on this Planet instance.
        self.name = name
        self.planet_type = planet_type
        self.star = star

    # Return a sentence describing the planet's orbit around its star.
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}."

    # Format the planet's details for display when print() receives the object.
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# Create three Planet objects with example names, types, and stars.
planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Neptune", "Ice Giant", "Sun")

# Print each object to show the formatted text returned by __str__.
print(planet_1)
print(planet_2)
print(planet_3)

# Print the orbital description returned by each object's orbit method.
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

