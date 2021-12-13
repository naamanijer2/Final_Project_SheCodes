from UserInput import UserInput
import itertools

class SearchRecipes:
    def __init__(self):
        self.recipe1 = ""
        self.recipe2 = ""

    def readRecipesFile(self):
        with open("recipes.txt", 'r') as file:
            line = file.readlines()
            #if (line == "Ingredients"):
