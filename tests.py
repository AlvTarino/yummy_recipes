import unittests
from yummy_classes import User,Recipe,RecipeItem

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.recipe = Recipe()
        self.recipeitem = recipeItem()

    def test_add_to_list(self):
        self.recipe.create_recipe('Rolex')
        self.assertEqual(self.recipe.lst, ['Fried-cassava'], msg = "List has not been updated with item")

    def update_with_new_item(self):
        self.recipe.update_recipe('Rolex')
        self.assertEqual(self.recipe.lst, ['Fried-cassava'], msg="Item item has not been removed")

    def delete_from_list(self):
        self.mylist.delete_from_list("blanket")
        self.assertEqual(self.mylist.lst, ['wine'], msg="Item not Added")
