from flask import Flask, render_template, request, url_for, flash, redirect
from RecipesOutput import RecipesOutput
from Restriction import Restriction
from SearchRecipes import SearchRecipes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chooseRes():
    if request.method == 'POST':
        restriction = request.form['restriction']
        favIngredients = request.form['favIngredients']
        if (restriction == None) or (favIngredients == None):
            flash('Please fill in all fields!')
        return redirect(url_for('recipes', res = restriction, fav = favIngredients))
    else:
        return render_template('select.html')


@app.route('/recipes/<res>/<fav>')
def recipes(res,fav):
    restrictions = Restriction(res, fav)
    restrictions.set_med_res_name()
    restrictions.set_fav_ing_list()
    searchRecipes = SearchRecipes(restrictions.med_res_name, restrictions.fav_ingredients_list)
    searchRecipes.searchFromTable()
    recipesOutput = RecipesOutput(searchRecipes.final_recipes_num_to_return)
    recipesOutput.connect_to_mysql()
    op = recipesOutput.print_recipes()
    rec = '<br>'.join(op)
    return f"<p>{rec}</p>"


if __name__ == '__main__':
    app.run()