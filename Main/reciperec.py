import pandas as pd
import re

df = pd.read_csv('../Dataset/recipes.csv')


def getUniqueCuisine():
    # get the unique cuisines
    cuisines = df['Cuisine'].unique()
    return cuisines

def getTopRecipes(x):
    # get the top x recipes
    top_recipes = df.sort_values(by='rating', ascending=False)
    top_recipes = top_recipes[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating']][:x].values.tolist()
    return top_recipes

def getTopRecipesNoAllergen(allergen_list, x):
    # get the top x recipes without allergens
    if not allergen_list:
        top_recipes = df.sort_values(by='rating', ascending=False)
        top_recipes_lst = top_recipes[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating']][:x].values.tolist()
        return top_recipes_lst
    
    top_recipes = df[~df['Ingredients'].str.contains('|'.join(allergen_list))]
    top_recipes = top_recipes.sort_values(by='rating', ascending=False)
    top_recipes_lst = top_recipes[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating']][:x].values.tolist()
    return top_recipes_lst

def getRecipeById(id):
    recipe = df[df['rec_id'] == id].values.tolist()
    return recipe

def getTopRecipesByCuisine(cuisine, x):
    # get the top x recipes by cuisine
    top_recipes = df[df['Cuisine'] == cuisine]
    top_recipes = top_recipes.sort_values(by='rating', ascending=False)
    top_recipes = top_recipes.head(x)
    return top_recipes

def searchForRecipeNoAllergen(recipe, allergen_list):
    recipes = df[df['Name'].str.contains(recipe, case=False, na=False)]
    recipes = recipes[~recipes['Ingredients'].str.contains('|'.join(allergen_list), case=False, na=False)]
    return recipes

def getRecipeInfoById(id_list):
    # id_list is a list of individual tuples, each tuple containing a single id
    recipe_info = []
    for id in id_list:
        recipe_info.append(df[df['rec_id'] == id[0]].values.tolist())
    return recipe_info

def getRecipeByCuisine(df, cuisine=None):
    if not cuisine:
        return df
    return df[df['Cuisine'].str.contains(cuisine, case=False, na=False)]

def getRecipeByName(df, name=None):
    if not name:
        return df[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]
    return df[df['Name'].str.contains(name, case=False, na=False)]

def getRecipeByIngredientList(df, ingredients_list):
    if ingredients_list == None or ingredients_list == []:
        return df[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]
    mask = df['Ingredients'].apply(lambda x: all(re.search(r'\b' + re.escape(ingredient.lower()) + r'\b', x.lower()) for ingredient in ingredients_list))
    valid_recipes = df[mask]
    return valid_recipes[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]

def getRecipeNoAllergen(df, allergen_list=None):
    if not allergen_list:
        return df[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]
    return df[~df['Ingredients'].str.contains('|'.join(allergen_list))][['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]

def getRecipeVegOnly(df):
    return df[df['veg_nonveg'] == 'veg'][['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]

def getRecipeIncudeEgg(df):
    df1 = getRecipeVegOnly(df)
    df2 = df[df['veg_nonveg'] == 'egg'][['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]
    return pd.concat([df1, df2])

def getRecipeExcludeIngredients(df, ingredients_exclude_list):
    if ingredients_exclude_list == None or ingredients_exclude_list == []:
        return df[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]
    mask = df['Ingredients'].apply(lambda x: all(re.search(r'\b' + re.escape(ingredient.lower()) + r'\b', x.lower()) for ingredient in ingredients_exclude_list))
    valid_recipes = df[~mask]
    return valid_recipes[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating', 'veg_nonveg']]

def getRecipe(df=df, cuisine='', name='', veg = 0, ingredient_list=[], allergen_list=[], ingredients_exclude_list=[]):
    recipes = getRecipeByCuisine(df, cuisine)
    recipes = getRecipeByName(recipes, name)
    recipes = getRecipeByIngredientList(recipes, ingredient_list)
    recipes = getRecipeNoAllergen(recipes, allergen_list)
    recipes = getRecipeExcludeIngredients(recipes, ingredients_exclude_list)
    if veg == 'veg':
        recipes = getRecipeVegOnly(recipes)
    elif veg == 'egg':
        recipes = getRecipeIncudeEgg(recipes)
    recipes = recipes[['rec_id', 'Name', 'Time', 'Cuisine', 'Ingredients', 'rating']][:20]
    recipes = recipes.sort_values(by='rating', ascending=False)
    return recipes.values.tolist()