import sys


class User (object):
    def __init__(self):
        self.recipes = {}

#class Recipe():      #creates recipe and allows users to add a recipe item or multiple recipe items to the recipe
    def create_recipe(self,name, *items):
        items = list(items)
        if name not in self.recipes.keys():
            self.recipes[name] = [item for item in items]
        elif name in self.recipes.keys():
            return 'Recipe exists!'
        return self.recipes
        #pass
    def read_recipe(self, name):  #Returns items in a recipe
        items = []
        if name in self.recipes.keys():
            items = [item for item in self.recipes[name]]
        return items
        #pass
    def add_recipe(self, recipe_name, new_name):  #    creates new recipe
        if recipe_name in self.recipes.keys():
            self.recipes[new_name] = self.recipes.pop(recipe_name)
        else:
            return "Recipe name does not exist here"
        return self.recipes
        #pass
    def update_recipe(self, recipe_name, item_name, new_name):   #updates a recipe
        if recipe_name in self.recipes.keys():
            for item in self.recipes[recipe_name]:
                if item == item_name:
                    self.recipes[recipe_name].remove(item)
                    self.recipes[recipe_name].append(new_name)
                else:
                    return 'Recipe Item not in the recipe list'
        else:
            return "Recipe name doesn't exist"
        return self.recipes
        #pass
    def delete_recipe(self, recipe_name):   #deletes recipe
        if recipe_name in self.recipes.keys():
            del self.recipes[recipe_name]
        else:
            return 'Recipe name does not exist in the system'
        return self.recipes
        #pass
    def update_recipeItem(self, recipe_name, *items):      #method adds recipe list items
        items = list(items)
        if recipe_name in self.recipes.keys():
            for item in items:
                if item not in self.recipes[recipe_name]:
                    self.recipes[recipe_name].append(item)
        else:
            if recipe_name not in self.recipes:
                for item in items:
                    self.recipes[recipe_name] = [item for item in items]
        #pass
    def delete_recipeItem(self, recipe_name, item):       #method deletes  recipe item in a recipe

        if item in self.recipes[recipe_name]:
            self.recipes[recipe_name].remove(item)
        else:
            return ' Recipe item not in list'
        return self.recipes
        #pass

    def __repr__(self):
        return 'Your recipes are: ' + ', '.join(name for name in self.recipes)
