import sys
sys.path.append('..')

class RecipeItem(object):
    def __init__(self, name):
        self.name = name
        self.status = False
        self.items = []

    def __repr__(self):
        return 'Recipe list items: ' + ', ' .join(item for item in self.items)
