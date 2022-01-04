from Restriction import Restriction
from SearchRecipes import SearchRecipes
from RecipesOutput import RecipesOutput

class MainClass(object):

    def __init__(self):
        self.medical_restriction = 0
        self.favorite_ingredients = ""

    def main(self):
        self.medical_restriction = input("Please choose restriction number: 1 - Sugar-Free, 2 - Gluten-Free, 3 - Dairy-Free ")
        self.favorite_ingredients = input("Please Enter up to 2 favorite ingredients: (for example - egg, tomato) ")
        restrictions = Restriction(self.medical_restriction, self.favorite_ingredients)
        restrictions.set_med_res_name()
        restrictions.set_fav_ing_list()
        searchRecipes = SearchRecipes(restrictions.med_res_name, restrictions.fav_ingredients_list)
        searchRecipes.searchFromTable()
        recipesOutput = RecipesOutput(searchRecipes.final_recipes_num_to_return)
        recipesOutput.connect_to_mysql()

        #print(restrictions.fav_ingredients_list)
        #print(restrictions.med_res_name)




if __name__ == '__main__':
    MainClass().main()