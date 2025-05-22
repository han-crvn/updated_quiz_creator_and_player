# Import libraries.
import os
import json

# Create a class.
class QuizCreator:
    
    # File location.
    def __init__(self, file_name = "category.json"):
        self.file_name = file_name
        self.categories = self.access_categories()

    # Accessing categories.
    def access_categories(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return json.load(file)
        return {}
    
    # Save categories.
    def save_categories(self):
        with open(self.file_name, "w") as file:
            json.dump(self.categories, file, indent=4)

    # Add categories.
    def add_category(self, name):
        # Allow users to add category and format it to title case.
        name = name.title()

        # Check if the file name is existing.
        if name in self.categories:
            print(f"{name} already exists.\n")
        else:
            self.categories[name] = []
            self.save_categories()
            print(f"{name} is successfully added!\n")

    # List down categories.
    def list_categories(self):

        # Check if there is existing categories
        if not self.categories:
            print("\nNo categories available.\n")
            return []
        for i, category in enumerate(self.categories.keys(), 1):
            print(f"{i}. {category}")
        return list(self.categories.keys())

# Create the main program.
def main_program():
    main_creator = QuizCreator()
    
    # Add short opening message.
    print("Hello! This is Quizzo.")

    while True:
        # Print the selections.
        print("\nSelection:\n1. Add Category\n2. Access Category\n3. Exit\n")
        
        try:

            # Allow users to choose from the options.
            choice = int(input("Enter your choice: "))
            
            # If users choose option 1, allow them to add category.
            if choice == 1:
                
                # Allow users to add category and format it to title case.
                category_name = input("\nEnter category name (0 = main menu): ")
                
                # Go back to main menu.
                if category_name == "0":
                    continue

                # Add the category name.
                main_creator.add_category(category_name)

             # If users choose option 2, allow them to access category and add question set.
            elif choice == 2:
                
                # Call list category.
                category_list = main_creator.list_categories()
                
                # Check if there is existing categories
                if not category_list:
                    continue
                
                try:

                    # Allow users to choose from options.
                    options = int(input("\nChoose a category (0 to go back): "))
                    
                    # Check if the chosen option is valid.
                    if options == 0:
                        continue
                    elif 1 <= options <= len(category_list):
                        pass
                    
                     # Catch invalid input.
                    else:
                        print("Invalid selection.\n")
                
                 # Catch invalid input.
                except ValueError:
                    print("Invalid input.\n")

            elif choice == 3:
                print("Thank you for using Quizzo!")
                break
            
            # Catch invalid input.
            else:
                print("Invalid choice! Try again.")

        # Catch invalid input.
        except ValueError:
            print("Invalid input! Try again.")

# Run the main program.
if __name__ == "__main__":
    main_program()