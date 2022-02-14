from SearchRecipes import SearchRecipes
import pymysql
import pymysql.cursors

class RecipesOutput:
    def __init__(self, recipes_numbers):
        self.recipe_name = ()
        self.recipe_ingredients = []
        self.recipe_description = ()
        self.recipes_numbers = recipes_numbers

    def connect_to_mysql(self):
        ser = SearchRecipes("",[])

        cur = ser.connectToMysql()
        for rec in self.recipes_numbers:
            cur.execute("SELECT recName FROM recipes WHERE Idrecpie=(%s)", str(rec))
            self.recipe_name = self.recipe_name + cur.fetchall()
            cur.execute("SELECT directions FROM recipes WHERE Idrecpie=(%s)", str(rec))
            self.recipe_description = self.recipe_description + cur.fetchall()
            cur.execute("SELECT ingredients FROM ingredients WHERE Idrecpie=(%s)", str(rec))
            self.recipe_ingredients.append(cur.fetchall())

    def print_recipes(self):
        i = 0
        j = 0
        dic = []

        while(i < len(self.recipe_name)):
            print(self.recipe_name[i][0] + ":\n" + "Ingredients:")
            dic.append("<h1>"+self.recipe_name[i][0]+"</h1>")
            dic.append("<h2>Ingredients:</h2>")
            k = 0
            while (len(self.recipe_ingredients[j]) > k):
                print(self.recipe_ingredients[j][k][0])
                dic.append(self.recipe_ingredients[j][k][0])
                k += 1
            print("Directions:\n " + self.recipe_description[i][0])
            dic.append("<h2>Directions:\n</h2> " + self.recipe_description[i][0])
            i += 1
            j += 1
            print("\n")
        return dic

