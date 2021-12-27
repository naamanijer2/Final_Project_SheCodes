import cur as cur
import pymysql
import pymysql.cursors
import _mysq
from sqlalchemy import create_engine
import itertools
import pandas as pd
from Restriction import Restriction

class SearchRecipes:
    def __init__(self):
        self.recipe_name1 = ""
        self.recipe_name2 = ""
        self.ingredients1 = ""
        self.ingredients2 = ""
        self.directions1 = ""
        self.directions2 = ""
        self.next_word = ""
        self.keyWord1 = ""

    def searchFromTable(self):
        restrictions = Restriction()
        if restrictions.med_res_name == 'sugar-free':
            self.keyWord1 = 'sugar'

        connection = pymysql.connect(host='127.0.0.1', user='root', password='196322Na!', db='recpies')
        query = """ SELECT BO_INDEX FROM recpies.ingredients.ibd
                WHERE BO_BEMERKUNG LIKE '%%%s%%' """ % self.keyWord1
        cur = connection.cursor()
        cur.execute(query)
        result_all = cur.fetchall()
        print(result_all)

        #engine = create_engine(self.keyWord1)
        #sql = "SELECT * FROM recpies.recpies "
        #sql2 = "SELECT * FROM recpies.ingredients"

        #if self.keyWord1 == sql:
          #  if self.next_word == 'substitute':
         #      pass

        #df = pd.read_sql_query(sql, engine)
        #df.head()


    #def readRecipesFile(self):
    #    with open("recipes.txt", 'r') as file:
    #        next(file)
    #        for line in file:
    #            if "Ingredients" in line:
    #                pass

    #        line = file.readlines()
    #        line2 =""
    #        if "Ingredients" in line:
     #           if self.userInput.med_res() == 1:
      #              while "Directions" not in line2 or "sugar" not in line2:
       #                 line2 = file.next()
        #            if "sugar" in line2:
         #               pass

          #      if self.userInput.med_res() == 2:
           #         while line2 != "flour" or line2 != "Directions":
            #            line2 = file.next()
             #   if self.userInput.med_res() == 3:
              #      while line2 != "milk" or line2 != "Directions":
               #         line2 = file.next()

            #if (line == "Ingredients"):
