import unittest
import sys
from yummy_classes import User

class TestYummy(unittest.TestCase):

    def setUp(self):
        self.user = User()
        #self.recipes=Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")

    #test to see if recipe has been created
    def test_recipe_initialy_empty(self):
        self.assertEqual(self.user.recipes, {})

    def test_create_recipe_successfully(self):
        initial_room_count = len(self.user.recipes)
        Rolex_recipe = self.user.create_recipe('Rolex')
        self.assertTrue(Rolex_recipe)
        new_room_count = len(self.user.recipes)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_recipe_when_list_already_exists(self):
        self.user.recipes = {'Rolex': ['eggs']}
        self.assertEqual(self.user.create_recipe('Rolex', 'eggs'),'Recipe exists!', msg='Recipe exists!')

    def test_create_recipe(self):
        self.user.recipes = {}
        self.assertEqual(self.user.create_recipe('Rolex', 'eggs'),{'Rolex': ['eggs']})
    """
    def test_update_recipe(self):
        self.user.recipes = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_recipe('Rolex', 'Water'), {'Water': ['eggs']})

    def test_updating_non_existing_recipe(self):
        self.user.recipes = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_recipe('Omlette', 'eggs'),'list name does not exist here', msg='list name does not exist here')
    
    def test_updating_non_existing_recipeItem(self):
        self.user.recipes = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_recipeItem('Rolex', 'oil', 'chapatti'),'Item not in list', msg='Item not in list')
    
    def test_update_recipeItem(self):
        self.user.recipes = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_recipeItem('Rolex', 'egg', 'eggs'), {'Rolex': ['egg']})
    """
    def test_delete_recipe(self):
        self.user.recipes = {'Rolex': ['eggs', 'highs'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_recipe('Rolex'), {'grocery': ['onions', 'tomatoes']})

    def test_delete_recipeItem(self):
        self.user.recipes = {'Rolex': ['eggs', 'flour'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_recipeItem('Rolex', 'eggs'), {'Rolex': ['flour'], 'grocery': ['onions', 'tomatoes']})
"""

import sys
from models.user import User
sys.path.append('/home/arthur/Desktop/ShoppingList/shop/bin/python')



class ShopTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_shopping_list_initialy_empty(self):
        self.assertEqual(self.user.shopping_lists, {})

    def test_create_shopping_list_successfully(self):
        initial_room_count = len(self.user.shopping_lists)
        cuttlery_list = self.user.create_shopping_list('Cuttlery')
        self.assertTrue(cuttlery_list)
        new_room_count = len(self.user.shopping_lists)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_shopping_list(self):
        self.user.shopping_lists = {}
        self.assertEqual(self.user.create_shopping_list('Rolex', 'eggs'),{'Rolex': ['eggs']})

    def test_create_shopping_list_when_list_already_exists(self):
        self.user.shopping_lists = {'Rolex': ['eggs']}
        self.assertEqual(self.user.create_shopping_list('Rolex', 'eggs'),'Shopping List already exists!', msg='Shopping List already exists!')

    def test_update_shopping_list(self):
        self.user.shopping_lists = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_shopping_list(
            'Rolex', 'flat_Rolex'), {'flat_Rolex': ['eggs']})

    def test_updating_non_existing_shopping_list(self):
        self.user.shopping_lists = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_shopping_list('Shoe', 'eggs'),
                         'list name does not exist here', msg='list name does not exist here')

    def test_update_shopping_list_item(self):
        self.user.shopping_lists = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_shopping_list_item(
            'Rolex', 'eggs', 'flat'), {'Rolex': ['flat']})

    def test_updating_non_existing_shopping_list_item(self):
        self.user.shopping_lists = {'Rolex': ['eggs']}
        self.assertEqual(self.user.update_shopping_list_item('Rolex', 'flas', 'flat'),
                         'Item not in list', msg='Item not in list')

    def test_read_shopping_list_items(self):
        self.user.shopping_lists = {'Rolex': ['eggs', 'highs']}
        self.assertEqual(self.user.read_list('Rolex'), ['eggs', 'highs'])

    def test_delete_shopping_list(self):
        self.user.shopping_lists = {'Rolex': ['eggs', 'highs'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_shopping_list(
            'Rolex'), {'grocery': ['onions', 'tomatoes']})

    def test_delete_shopping_list_item(self):
        self.user.shopping_lists = {'Rolex': ['eggs', 'highs'], 'grocery': ['onions', 'tomatoes']}
        self.assertEqual(self.user.delete_shopping_list_item('Rolex', 'eggs'), {
                         'Rolex': ['highs'], 'grocery': ['onions', 'tomatoes']})

"""
