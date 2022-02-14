from Restriction import Restriction
from SearchRecipes import SearchRecipes
from RecipesOutput import RecipesOutput

class MainClass(object):

    def __init__(self):
        self.medical_restriction = 0
        self.favorite_ingredients = ""
        self.rec_choose = ""
        self.rec_rate = ""

    def main(self):

        self.medical_restriction = input("Please choose restriction number: 1 - Sugar-Free, 2 - Gluten-Free, 3 - Dairy-Free ")
        while ((self.medical_restriction != '1') ^ (self.medical_restriction != '2') ^ (self.medical_restriction != '3')):
            print("Wrong input! please try again...")
            self.medical_restriction = input( "Please choose restriction number: 1 - Sugar-Free, 2 - Gluten-Free, 3 - Dairy-Free ")

        self.favorite_ingredients = input("Please Enter up to 2 favorite ingredients: (for example - egg, tomato) ")
        while (self.favorite_ingredients.isdigit()):
            print("Wrong input! please try again..")
            self.favorite_ingredients = input("Please Enter up to 2 favorite ingredients: (for example - egg, tomato) ")


        restrictions = Restriction(self.medical_restriction, self.favorite_ingredients)
        restrictions.set_med_res_name()
        restrictions.set_fav_ing_list()
        searchRecipes = SearchRecipes(restrictions.med_res_name, restrictions.fav_ingredients_list)
        searchRecipes.searchFromTable()
        recipesOutput = RecipesOutput(searchRecipes.final_recipes_num_to_return)
        recipesOutput.connect_to_mysql()
        recipesOutput.print_recipes()

        rec2 = "None"
        rec1 = recipesOutput.recipe_name[0][0]
        if len(recipesOutput.recipe_name) > 1:
            rec2 = recipesOutput.recipe_name[1][0]
        rec_choose = input(f"Please select the recipe that you choose: 1-{rec1}, 2-{rec2}")
        if rec_choose == 1:
            self.rec_choose = rec1
        else:
            self.rec_choose = rec2
        self.rec_rate = input("Please rate the recipe between 1 to 5: ")



if __name__ == '__main__':
    MainClass().main()