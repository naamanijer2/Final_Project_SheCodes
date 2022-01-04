from SearchRecipes import SearchRecipes
import pymysql
import pymysql.cursors

class RecipesOutput:
    def __init__(self, recipes_numbers):
        self.recipe_name1 = ''
        self.recipe_name2 = ''
        self.recipe_ingredients1 = ''
        self.recipe_ingredients2 = ''
        self.recipe_description1 = ''
        self.recipe_description2 = ''
        self.recipes_numbers = recipes_numbers

    def connect_to_mysql(self):
        connection = pymysql.connect(host='127.0.0.1', user='root', password='196322Na!',
                                     db='recpies')  # connecting to mysql
        cur = connection.cursor()

        query1 = "SELECT recName FROM recipes WHERE Idrecpie = %s"  # sql query to find medical restrictions
        cur.execute(query1, ('%' + str(self.recipes_numbers) + '%'))
        self.recipe_name1 = cur.fetchall()
        print(self.recipe_name1)


