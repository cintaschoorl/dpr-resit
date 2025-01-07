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

"""
het lukte eerst prima maar bij print summary ging het mis en toen werkte ik terug om
bij add trail de juiste vorm van classes in een dictionary goed te zetten, maar toen raakt ik het overzicht kwijt :((

was de bedoeling eerst om gewoon met de attributes van de trail class te werken,
maar door de dictionary structuur wilde ik het class object als value van de naam als key zetten,
hier had ik uiteindelijk te weinig tijd voor om volledig om te zetten...
"""
