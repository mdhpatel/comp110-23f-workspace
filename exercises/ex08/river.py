"""File to define River class."""

__author__ = "730710742"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Creates the River object and holds its methods."""

    day: int
    bears: list[str]
    fish: list[str]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """This checks the ages of bears and fishes in order to determine if they are too old and should be removed from the river."""
        young_bears: list = list()
        young_fish: list = list()
        for fishes in self.fish:
            if fishes.age <= 3:
                young_fish.append(fishes)
        for bears in self.bears:
            if bears.age <= 5:
                young_bears.append(bears)
        self.bears = young_bears
        self.fish = young_fish
        return None

    def bears_eating(self):
        """This removes fish, given that there are more than five in the river, by making the bears eat them."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                bears.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """If a bear's hunger gets too low it dies and is removed from the list of bears representing living bears at the river."""
        living_bears: list = list()
        for bears in self.bears:
            if bears.hunger_score > 0:
                living_bears.append(bears)
        self.bears = living_bears
        return None
        
    def repopulate_fish(self):
        """This represents the repopulation of fish into the river so that for every two fish they reproduce four more."""
        offspring: int = ((len(self.fish)) / 2) * 4
        offspring_index: int = 0
        while offspring_index <= offspring:
            self.fish.append(Fish) 
        return None
    
    def repopulate_bears(self):
        """This represents the repopulation of bears so that for every two bears they reproduce one more."""
        offspring: int = (len(self.bears)) / 2
        offspring_index: int = 0
        while offspring_index <= offspring:
            self.bears.append(Bear)        
        return None
    
    def view_river(self):
        """This allows us to see what day it is in the simulation, the amount of bears, and the number of fish in the river."""
        print(f"~~~ Day {self.day}: ~~~ \n Fish population: {len(self.fish)} \n Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulates one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates life in the river for a week."""
        for day in range(0, 7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes a certain amount of fish from the river."""
        removed_index: int = 0
        while removed_index <= amount:
            self.fish.pop(removed_index)
            removed_index += 1