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

        connection = pymysql.connect(host='127.0.0.1', user='root', password='196322Na!',
                                     db='recpies')  # connecting to mysql
        cur = connection.cursor()
        for rec in self.recipes_numbers:
            cur.execute("SELECT recName FROM recipes WHERE Idrecpie=(%s)", str(rec))
            self.recipe_name = self.recipe_name + cur.fetchall()
            cur.execute("SELECT directions FROM recipes WHERE Idrecpie=(%s)", str(rec))
            self.recipe_description = self.recipe_description + cur.fetchall()
            cur.execute("SELECT ingredients FROM ingredients WHERE Idrecpie=(%s)", str(rec))
            self.recipe_ingredients.append(cur.fetchall())

        i = 0
        j = 0
        while(i < len(self.recipe_name)):
            print(self.recipe_name[i][0] + ":\n" + "Ingredients:")
            k = 0
            while (len(self.recipe_ingredients[j]) > k):
                print(self.recipe_ingredients[j][k][0])
                k += 1
            print("Directions:\n " + self.recipe_description[i][0])
            i += 1
            j += 1
            print("\n")


