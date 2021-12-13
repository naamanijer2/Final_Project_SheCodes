from UserInput import UserInput

def main():
    medical_restriction = input("Please choose restriction number: 1 - Sugar-Free, 2 - Gluten-Free, 3 - Dairy-Free ")
    favorite_ingredients = input("Please Enter up to 2 favorite ingredients: (for example - egg, tomato) ")

    userInput = UserInput(medical_restriction, favorite_ingredients)

if __name__ == '__main__':
    main()