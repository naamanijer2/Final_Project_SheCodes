#Map the user inputs and orgenise them.
class Restriction:

    def __init__(self, medical_restriction="", favorite_ingredients=""):
        self.med_res = medical_restriction
        self.fav_ing = favorite_ingredients
        self.med_res_name = ""
        self.fav_ingredients_list = []


    def get_med_res(self):
        return self.med_res

    def get_fav_ing(self):
        return self.fav_ing

    #map restriction number to restriction name
    def set_med_res_name(self):
        if self.med_res == '1':
            self.med_res_name = "sugar-free"
        if self.med_res == '2':
            self.med_res_name = "gluten-free"
        if self.med_res == '3':
            self.med_res_name = "dairy-free"

    #set the favorite ingridients from string to list
    def set_fav_ing_list(self):
        fav_ing = self.fav_ing
        self.fav_ingredients_list = fav_ing.split(', ')
