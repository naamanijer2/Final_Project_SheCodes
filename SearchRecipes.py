import pymysql
import pymysql.cursors
import pymysql.connections
import random

class SearchRecipes:
    def __init__(self, med_res_name="", fav_ingredients_list=[]):
        self.suitable_recipes_num = [] #list of all the suitable recipes
        self.final_recipes_num_to_return = [] #list of the two final chosen recipes that we will print
        self.keyWord1 = ''
        self.keyWord2 = ''
        self.keyWord3 = ''
        self.med_res_name = med_res_name
        self.fav_ingredients_list = fav_ingredients_list
        self.connection = None

    def connectToMysql(self):
        password = input('Enter password: ')
        self.connection = pymysql.connect(host='127.0.0.1', user='root', password=password, db='recpies')
        cur = self.connection.cursor()
        return cur

    #search the sutable recipes
    def searchFromTable(self):
        if self.med_res_name == 'sugar-free':
            self.keyWord1 = 'sugar'
            self.keyWord2 = ['substitute']
        if self.med_res_name == 'gluten-free':
            self.keyWord1 = 'flour'
            self.keyWord2 = ['corn flour', 'almond flour', 'potato flour']
        if self.med_res_name == 'dairy-free':
            self.keyWord1 = 'milk'
            self.keyWord2 = ['non-dairy']
            self.keyWord3 = 'cheese'

        cur = self.connectToMysql()
        query1 = "SELECT * FROM ingredients WHERE ingredients LIKE %s" #sql query to find medical restrictions
        cur.execute(query1, ('%' + self.keyWord1 + '%'))
        problematic_rec = cur.fetchall()
        #add to problematic recipes the recipes that contain cheese if selected dairy-free
        if self.keyWord3 != '':
            cur.execute(query1, ('%' + self.keyWord3 + '%'))
        problematic_rec = problematic_rec + cur.fetchall()

        favourite_rec = () #define tuple
        favourite_rec_num = []
        for ingredient in self.fav_ingredients_list: #sql query to find the favorite ingredients
            query2 = "SELECT * FROM ingredients WHERE ingredients LIKE %s"
            cur.execute(query2, ('%' + ingredient + '%'))
            favourite_rec = favourite_rec + cur.fetchall()
        for i in favourite_rec:
            favourite_rec_num.append(i[0])

        #Ignoring exceptional cases where there are substitutes like sugar substitute
        temp = []
        for list in problematic_rec:
            for i in self.keyWord2:
                if i in list[2] and i != '':
                    pass
                else:
                    temp.append(list[0])

        forbidden_recipes_num = self.deleting_unnecessary(temp)

        favourite_rec_num = self.deleting_unnecessary(favourite_rec_num)

        self.set_suitable_rec_list(favourite_rec_num, forbidden_recipes_num)
        self.select_popular_random_recipes()

        if self.final_recipes_num_to_return == []:
            print("Sorry! No suitable recipes found...")

    #set duplicates (if one recipe has 2 favorit ingridients
    def deleting_unnecessary(self, l1):
        l2 = []
        for i in l1:
            if i not in l2:
                l2.append(i)
        return l2

    #remove the forbidden recipes from the favorit recipes
    def set_suitable_rec_list(self, favorite_rec_num, forbidden_recipes_num):
        for i in favorite_rec_num:
            if i not in forbidden_recipes_num:
                self.suitable_recipes_num.append(i)

    #select the most popular recipe in the list, and get the other recipe from random function
    def select_popular_random_recipes(self):
        max_rate = 0 #max rate in the table
        max_rate_idrecipe = 0 #the IDnumber of the recipe that has the max rate
        cur = self.connectToMysql()
        if len(self.suitable_recipes_num) > 2:
            for i in self.suitable_recipes_num:
                cur.execute("SELECT rate FROM recipes WHERE Idrecpie = (%s)",i) #sql query to find the most popular recipe
                j = cur.fetchall()[0][0]
                if j >= max_rate:
                    max_rate = j
                    max_rate_idrecipe = i

            self.final_recipes_num_to_return.append(max_rate_idrecipe)
            self.suitable_recipes_num.remove(max_rate_idrecipe)

            #final recipes numbers that will be the output
            self.final_recipes_num_to_return = self.final_recipes_num_to_return + random.sample(self.suitable_recipes_num,1)

        else:
            self.final_recipes_num_to_return = self.suitable_recipes_num

    #appdate the recipe rate to the database
    def addRateRecipe(self, rate, recName):
        cur = self.connectToMysql()
        query = "UPDATE recipes SET rate = rate + %s WHERE recName = %s"
        cur.execute(query,(rate, recName))
        self.connection.commit()
