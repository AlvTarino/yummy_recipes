import unittest
from yummy_classes import User

class TestYummy(unittest.TestCase):

    def setUp(self):
        self.recipe = Recipe()

        #test to see if recipelist has been created
    def test_create(self):
        self.assertEqual(self.create_recipe.lst,[],msg ="RecipeList has not been created")

         #Test for add item to an empty recipelist
    def test_add_recipe(self):
        self.recipe.add_recipe('omlette')
        self.assertEqual(self.recipe.lst, ['omlette'], msg="Recipe item has not been added with new item")

        #Test for updating recipelist with a new item
    def update_recipe(self):
        self.recipe.update_recipe('Rolex')
        self.assertEqual(self.recipe.lst, ['chicken soup'], msg="Recipe list has not been updated")

        #Test for removing an item from recipelist
    def delete_recipe(self):
        self.recipe.delete_recipe("Rolex")
        self.assertEqual(self.recipe.lst, ['chicken soup'], msg="Item not deleted"
