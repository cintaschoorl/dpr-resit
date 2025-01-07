# Name: Cinta Schoorl
# Studentnumber: 13562045
# DPR exam - Fall 2024
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

### Part 2: pandas ###
#1
def csv_to_df(file, seperator=','):
    df = pd.read_csv(file, sep=seperator, index_col=0)
    return df
#2
def remove_Na_sex(df):
    new_df = df[df['sex'].notna()]
    return new_df
#3
def print_heaviest(df):
    idx = df['body_mass_g'].idxmax()
    max_weight = df['body_mass_g'].max()
    species = df['species'].iloc[idx]
    island = df['island'].iloc[idx]
    print(f"The heaviest penguin is a {species} from {island}, weighing {max_weight} grams.")
#4
def add_sort_bill_ratio(df):
    df['bill_ratio'] = df['bill_length_mm'] / df['bill_depth_mm']
    df = df.sort_values(by='bill_ratio', ascending=False)
    return df
#5
def avg_df(df):
    grouped = df.groupby('species')
    return grouped[['flipper_length_mm', 'body_mass_g']].mean()


### Part 3: Built-in data structures ###
music_library = {
    "The Beatles": {
        "Abbey Road": {
            "year": 1969,
            "tracks": [
                ("Come Together", 260),
                ("Something", 179),
                ("Oh! Darling", 206)
            ]
        },
        "Revolver": {
            "year": 1966,
            "tracks": [
                ("Taxman", 159),
                ("Eleanor Rigby", 128),
                ("Tomorrow Never Knows", 178)
            ]
        }
    },
    "Pink Floyd": {
        "The Dark Side of the Moon": {
            "year": 1973,
            "tracks": [
                ("Speak to Me", 67),
                ("Time", 424),
                ("Us and Them", 469)
            ]
        },
        "The Wall": {
            "year": 1979,
            "tracks": [
                ("Another Brick in the Wall Pt.2", 240),
                ("Comfortably Numb", 383)
            ]
        }
    }
}
#1
def hipster_search(music_library, artist):
    if artist not in music_library:
        print(f"{artist}? Yeah, I knew them before they were mainstream.")
    for art, albums in music_library.items():
        if art == artist:
            lowest_year = 3000
            oldest = None
            for album in albums:
                year = albums[album]['year']
                if year < lowest_year:
                    oldest = album
            print(f"{artist}? I only really like {oldest}.")
#2
def list_all_tracks(music_library):
    all_tracks = []

    for artist, albums in music_library.items():
        for album in albums:
            for track_title, track_length in albums[album]['tracks']:
                all_tracks.append((artist, album, track_title, track_length))

    return all_tracks
#3
def add_new_track(music_library, artist, album, track_title, track_length):
    if artist not in music_library:
        print(f"Artist '{artist}' does not exist.")
    else:
        if album not in music_library[artist]:
            print(f"Album '{album}' does not exist.")
        else:
            for artist, albums in music_library.items():
                for track_info in albums[album]['tracks']:
                    if track_title == track_info[0]:
                        print(f"Track '{track_title}' already exists in '{album}'.")
                    else:
                        albums[album]['tracks'].append((track_title, track_length))
                        print(f"Added '{track_title}' to the library!")


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

    print("\n=== Part 2: pandas ===")
    print("\n== Exc 1 ==")
    df = csv_to_df('penguins.csv')
    print(df.shape)
    print(df.head(5))
    print("\n== Exc 2 ==")
    df = remove_Na_sex(df)
    print(df.shape)
    print("\n== Exc 3 ==")
    print_heaviest(df)
    print("\n== Exc 4 ==")
    df = add_sort_bill_ratio(df)
    print(df.head(10))
    print("\n== Exc 5 ==")
    df_avg = avg_df(df)
    print(df_avg)

    print("\n=== Part 3: Built-in data structures ===")
    print("\n== Exc 1 ==")
    hipster_search(music_library, "ABBA")
    hipster_search(music_library, "The Beatles")
    print("\n== Exc 2 ==")
    all_tracks = list_all_tracks(music_library)
    print(f"There are {len(all_tracks)} tracks in our library:")
    for t in all_tracks:
        print(t)

    print("\n== Exc 3 ==")
    print("\nTesting adding tracks to the library:")

    # Should print an error, as artist doesn't exist
    add_new_track(music_library, "Unknown Artist", "Unknown Album", "New Track", 200)

    # We should still have 11 tracks
    print(f"There are {len(list_all_tracks(music_library))} tracks in our library:")

    # Should print an error, as album doesn't exist
    add_new_track(music_library, "The Beatles", "Unknown Album", "New Track", 200)

    # We should still have 11 tracks
    print(f"There are {len(list_all_tracks(music_library))} tracks in our library:")

    # This one should work
    add_new_track(music_library, "The Beatles", "Revolver", "Good Day Sunshine", 129)

    # We should now have 12 tracks
    print(f"There are {len(list_all_tracks(music_library))} tracks in our library:")

    # And adding the same again should print an error
    add_new_track(music_library, "The Beatles", "Revolver", "Good Day Sunshine", 129)

    # We should still have 12 tracks
    print(f"There are {len(list_all_tracks(music_library))} tracks in our library:")
