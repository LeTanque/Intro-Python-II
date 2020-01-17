# Implement a class to hold room information. This should have name and
# description attributes.


class Cave:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # directional definitions
        self.north_to = None
        self.south_to = None
        self.east_to = None
        self.west_to = None

    def __str__(self):
        display_string = ""
        display_string += f"\n --- --- --- \n"
        display_string += f"\n{self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"\n{self.get_exit_string()}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        return None

    def get_exits(self):
        exits = []
        if self.north_to:
            exits.append("north")
        if self.south_to:
            exits.append("south")
        if self.east_to:
            exits.append("east")
        if self.west_to:
            exits.append("west")
        return exits

    def get_exit_string(self):
        return f"Exits to: {', '.join(self.get_exits())}"
