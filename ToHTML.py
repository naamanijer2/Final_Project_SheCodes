from flask import Flask, render_template, request, url_for, flash, redirect
from RecipesOutput import RecipesOutput
from Restriction import Restriction
from SearchRecipes import SearchRecipes

#class ToHTML:

app = Flask(__name__)

#app.config['SECRET_KEY'] = 'your secret key'
#messages = [{'restriction': 'Message One',
#             'favIngredients': 'Message One Content'},
#            {'restriction': 'Message Two',
#             'favIngredients': 'Message Two Content'}
#           ]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/select', methods=['GET', 'POST'])
def chooseRes():
    if request.method == 'POST':
        restriction = request.form['restriction']
        #favIngredients = request.form['favIngredients']
        #a1 = redirect(url_for('restriction', res = restriction))
        #a2 = redirect(url_for('favIngredients', fav = favIngredients))
        #return a1,a2
        return redirect(url_for('recipes', res = restriction))
    else:
        return render_template('select.html')

#@app.route('/selectF', methods=['GET', 'POST'])
#def chooseFav():
#    if request.method == 'POST':
#        favIngredients = request.form['favIngredients']
#        return redirect(url_for('favIngredients', fav = favIngredients))
#    else:
#        return render_template('select.html')


@app.route('/recipes/<res>')
def recipes(res):
    fav = 'egg'
    restrictions = Restriction(res, fav)
    restrictions.set_med_res_name()
    restrictions.set_fav_ing_list()
    searchRecipes = SearchRecipes(restrictions.med_res_name, restrictions.fav_ingredients_list)
    searchRecipes.searchFromTable()
    recipesOutput = RecipesOutput(searchRecipes.final_recipes_num_to_return)
    recipesOutput.connect_to_mysql()
    op = recipesOutput.print_recipes()
    print (op)
    rec = '<br>'.join(op)
    return f"<p>{rec}</p>"



#@app.route('/', methods = ['GET', 'POST'] )
#def chooseInput():
    #restriction = ''
    #favIngredients = ''
    #if request.method == 'POST':
        #restriction = request.form['restriction']
        #favIngredients = request.form['favIngredients']
        #if not restriction:
            #flash('Restriction is required!')
        #elif not favIngredients:
            #flash('Favorite ingredient is required!')
        #else:
            #messages.append({'Restriction': restriction, 'Favorite Ingredients': favIngredients})

            #restrictions = Restriction(restriction, favIngredients)
            #restrictions.set_med_res_name()
            #restrictions.set_fav_ing_list()
            #searchRecipes = SearchRecipes(restrictions.med_res_name, restrictions.fav_ingredients_list)
            #searchRecipes.searchFromTable()
            #recipesOutput = RecipesOutput(searchRecipes.final_recipes_num_to_return)
            #recipesOutput.connect_to_mysql()


            #return redirect(url_for('home'))
    #return render_template('select.html', restriction = restriction, favIngredients = favIngredients)


if __name__ == '__main__':
    app.run()