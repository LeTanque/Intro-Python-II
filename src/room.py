# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, message):
        self.name = name
        self.description = description
        self.message = message

    def __str__(self):
        return self.name
