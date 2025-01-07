import numpy as np
import pandas as pd

### Part 1: OOP ###
class HikingTrail():
    def __init__(self, name, length_km, difficulty_rating):
        self.name = name
        self.length_km = length_km
        self.difficulty_rating = difficulty_rating

        self.all_ratings = []

    def update_difficulty(self, new_difficulty):
        # add to list of ratings
        self.all_ratings.append(new_difficulty)

        # update trail difficulty as mean of list
        self.difficulty_rating = np.mean(self.all_ratings).round()

    def print_summary(self):
        print(f"{self.name}: {self.length_km} km, difficulty {self.difficulty_rating}")

class Park():
    def __init__(self, name, location):
        self.name = name
        self.location = location

        self.trails = {}

    def add_trail(self, trail):
        if trail not in self.trails:
            self.trails[trail.name] = trail
            print(f"{trail.name} added.")
        else:
            print(f"Error: {trail.name} already exists.")

    def remove_trail(self, trail_name):
        try:
            del self.trails[trail_name]
            print(f"{trail_name} removed.")
        except KeyError:
            print(f"{trail_name} does not exist.")

    def average_difficulty(self):
        all_difficulties = []

        for key, trail in self.trails.items():
            all_difficulties.append(trail.difficulty_rating)

        if len(all_difficulties) > 0:
            return np.mean(all_difficulties).round(2)
        else:
            return 0

    def print_summary(self):
        print(f"{self.name} in {self.location} (avg difficulty: {self.average_difficulty()}) has the following trails:")
        for trail in self.trails:
            trail.print_summary()

if __name__ == "__main__":
    print("\n=== Part 1: OOP ===")
    trail_a = HikingTrail("Eagle Peak", 5.3, 7)
    trail_b = HikingTrail("Sunset Loop", 2.0, 4)
    trail_c = HikingTrail("Pine Ridge", 10.0, 9)

    park = Park("Green Valley National Park", "California")

    # Print initial average difficulty (should be "0" as we have no trails yet)
    print(f"Average difficulty before adding trails: {park.average_difficulty()}")

    # Add the trails to the park
    park.add_trail(trail_a)
    park.add_trail(trail_b)
    park.add_trail(trail_c)

    # This should print 3, as we've added 3 trails
    print(f"The park now has {len(park.trails)} trails.\n")

    # # Adding a trail with the same name twice should print an error
    # park.add_trail(trail_a)
    #
    # # Print average difficulty after adding trails
    # print(f"Average difficulty after adding trails: {park.average_difficulty()}\n")
    #
    # # Print a summary of the park
    # park.print_summary()
    #
    # # Update the difficulty of one trail
    # trail_b.update_difficulty(5)
    # print(f"\nAfter updating '{trail_b.name}' difficulty:")
    # park.print_summary()
    #
    # # Remove a trail without an error
    # park.remove_trail("Eagle Peak")
    #
    # # This one should give an error
    # park.remove_trail("Does Not Exist")
    #
    # # Print a summary of the park after removals
    # print("\nAfter removals:")
    # park.print_summary()