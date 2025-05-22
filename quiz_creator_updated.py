# Import libraries.
import os
import json

# Create a class.
class QuizCreator:
    
    # File location.
    def __init_(self, file_name = "category.json"):
        self.file_name = file_name
        self.categories = self.load.categories()

    # Accessing categories
    def access_categories(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return {}