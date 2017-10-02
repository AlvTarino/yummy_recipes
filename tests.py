import unittest
from yummy_classes import User

class TestYummy(unittest.TestCase):

    def setUp(self):
        self.user = User("qwerty", "qwerty@qwerty.com", "qqq")
        self.recipes=Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")

    #Test if the user has Username Variable
    def test_username(self):
        self.assertEqual(self.user.username, "qwerty", msg = "Username is invalid")

    #Test if the user has Email Variable
    def test_emailaddress(self):
        self.assertEqual(self.user.email, "qwerty@qwerty.com", msg = "Email is Invalid")

    #Test if the user has Password Variable
    def test_password(self):
        self.assertEqual(self.user.password, "qqq", msg = "Password is invaid")

    #Test if the User can be registered
    def test_registerUser(self):
        self.user.registerUser(["qwerty", "qwerty@qwerty.com", "qqq"])
        self.assertEqual(self.user.database, [["qwerty", "qwerty@qwerty.com", "qqq"]], msg="User Not Registered")

        #test to see if recipelist has been created
    def test_create(self):
        self.recipe.create_recipe('Rolex')
        self.assertEqual(self.create_recipe.lst,['Rolex'],msg ="RecipeList has not been created")

         #Test for add item to an empty recipelist
    def test_add_recipe(self):
        self.recipe.add_recipe('eggs')
        self.assertEqual(self.recipe.lst, ['eggs'], msg="Recipe item has not been added with new item")

        #Test for updating recipelist with a new item
    def update_recipe(self):
        self.recipe.update_recipe('Rolex')
        self.assertEqual(self.recipe.lst, ['chicken soup'], msg="Recipe list has not been updated")

        #Test for removing an item from recipelist
    def delete_recipe(self):
        self.recipes.delete_recipes("Rolex")
        self.assertEqual(self.recipe.lst, ['chicken soup'], msg="Item not deleted")

"""
    def setUp(self):
        self.user = User("spiderman", "spiderman@gmail.com", "maryJaneparker")
        self.new_recipe=Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")

    #Test if the user has Username Variable
    def test_username(self):
        self.assertEqual(self.user.username, "spiderman", msg = "Username is invalid")

    #Test if the user has Email Variable
    def test_emailaddress(self):
        self.assertEqual(self.user.email, "spiderman@gmail.com", msg = "Email is Invalid")

    #Test if the user has Password Variable
    def test_password(self):
        self.assertEqual(self.user.password, "maryJaneparker", msg = "Password is invaid")

    #Test if the User can be registered
    def test_registerUser(self):
        self.user.registerUser(["spiderman", "spiderman@gmail.com", "maryJaneparker"])
        self.assertEqual(self.user.database, [["spiderman", "spiderman@gmail.com", "maryJaneparker"]], msg="User Not Registered")

    #Test Import of Recipes class to make sure the user can interact with a recipe
    def test_recipe_class(self):
        self.assertIsInstance(self.new_recipe,Recipes, msg='Object is not an instance of the  class')
        
    #Test if user can create a recipe
    def test_create_recipe(self):
            self.assertTrue(self.user.create_recipe(self.new_recipe))
    
    def test_recipe_to_create_already_exists(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.recipes = {"546": recipe1}
        self.assertFalse(self.user.create_recipe(recipe1))
    
    def test_new_recipe_stored_in_dictionary(self):
        self.assertEqual(type(self.user.get_recipes()), dict, msg='Output is not a dictionary')
    

    def test_a_recipe_is_returned_when_an_id_is_specified(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.recipes = {"546": recipe1}
        self.assertEqual(self.user.get_recipe("546"), recipe1)

    def test_none_is_returned_for_recipe_doesnot_exist(self):
        self.assertIsNone(self.user.get_recipe("Sandwich"))

    def test_edit_recipe(self):
        self.user.create_recipe(self.new_recipe)
        self.assertTrue(self.user.edit_recipe("Sandwich","Obtain ingredients-bread ,salads,bacon" ,"546"))

    def test_recipe_to_edit_doesnt_exists(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.create_recipe(recipe1)
        self.assertFalse(self.user.edit_recipe("Sandwich","Obtain ingredients-bread ,salads,bacon" ,"548"))

    def test_del_recipe(self):
        self.user.create_recipe(self.new_recipe)
        self.assertTrue(self.user.del_recipe("546"))

    def test_recipe_to_delete_doesnt_exists(self):
        recipe1 = Recipes("Rolex recipe","Obtain ingredients - eggs and chapatis","546")
        self.user.create_recipe(recipe1)
        self.assertFalse(self.user.del_recipe("548"))

        """