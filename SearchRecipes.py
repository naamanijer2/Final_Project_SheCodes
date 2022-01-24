import cur as cur
import pymysql
import pymysql.cursors
import random
from collections import OrderedDict

from sqlalchemy import create_engine
import itertools
import pandas as pd
from Restriction import Restriction

class SearchRecipes:
    def __init__(self, med_res_name="", fav_ingredients_list=[]):
        self.suitable_recipes_num = []
        self.final_recipes_num_to_return = []
        self.keyWord1 = ''
        self.keyWord2 = ''
        self.keyWord3 = ''
        self.med_res_name = med_res_name
        self.fav_ingredients_list = fav_ingredients_list

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

        connection = pymysql.connect(host='127.0.0.1', user='root', password='196322Na!', db='recpies') #connecting to mysql
        cur = connection.cursor()
        query1 = "SELECT * FROM ingredients WHERE ingredients LIKE %s" #sql query to find medical restrictions
        cur.execute(query1, ('%' + self.keyWord1 + '%'))
        problematic_rec = cur.fetchall()
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

        print('problematic recipes: {}'.format(problematic_rec))
        print('favourite recipes: {}'.format(favourite_rec))
        print('forbidden recipes numbers: {}'.format(forbidden_recipes_num))
        print('favourite recipes numbers: {}'.format(favourite_rec_num))

        self.set_suitable_rec_list(favourite_rec_num, forbidden_recipes_num)
        print('final suitable recipes: {}'.format(self.suitable_recipes_num))
        self.select_random_recipes()
        print('final recipes num to return: {}'.format(self.final_recipes_num_to_return))
        #return (favourite_rec_num, forbidden_recipes_num)

    def deleting_unnecessary(self, l1):
        l2 = []
        for i in l1:
            if i not in l2:
                l2.append(i)
        return l2

    def set_suitable_rec_list(self, favorite_rec_num, forbidden_recipes_num):
        for i in favorite_rec_num:
            if i not in forbidden_recipes_num:
                self.suitable_recipes_num.append(i)

    def select_random_recipes(self):
        if len(self.suitable_recipes_num) > 2:
            self.final_recipes_num_to_return = random.sample(self.suitable_recipes_num,2)
        else:
            self.final_recipes_num_to_return = self.suitable_recipes_num