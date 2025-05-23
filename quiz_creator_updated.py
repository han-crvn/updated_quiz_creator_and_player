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

        # Check if there is existing categories.
        if not self.categories:
            print("\nNo categories available.\n")
            return []
        for num_category, category in enumerate(self.categories.keys(), 1):
            print(f"{num_category}. {category}")
        return list(self.categories.keys())
    
    # Add questions to categories
    def add_question_set(self, category_name):
        
        # Check if there is an existing category.
        if category_name not in self.categories:
            print("Invalid category.\n")
            return
        
        while True:

            # Allow users to input the questions.
            question = input("Enter the question: ").strip()
            
            # Check if there is a question.
            if not question:
                print("Question cannot be empty.\n")
                continue
            
            # Stores the choices.
            choices = {}

            # Loop choices for A-D.
            for number in range(4):
                
                # Tell what letter is the choice.
                option = chr(65 + number)
                
                while True:
                    
                    # Allow users to input the choices.
                    choice_text = input(f"Enter choice '{option}': ").strip()
                    
                    # Check if there is a choice.
                    if choice_text:
                        choices[option] = choice_text
                        break
                    else:
                        print("Choice cannot be empty.\n")

            while True:

                # Allow users to input the correct answer.
                answer = input("Enter the correct answer (A, B, C, D): ").upper()
                
                # Check if the answer is valid.
                if answer in choices:
                    break
                print("\nInvalid answer! Try again.\n")

            # Add the question set to the category.
            self.categories[category_name].append({
                "question": question,
                "choices": choices,
                "answer": answer
            })

            # Save the question set.
            self.save_categories()

            # Indicator that it was successful.
            print("Question set successfully added.\n")

            # Ask if users want to try again.
            try_again = input("\nAdd another question set? (1 = Yes, 2 = No): ")
            
            # Validate their answers.
            if try_again != "1":
                break

# Create the main program.
def main_program():
    
    # Variable for quiz creator.
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
                category_name = input("\nEnter category's number (0 = main menu): ")
                
                # Go back to main menu.
                if category_name == "0":
                    continue

                # Add the category name.
                main_creator.add_category(category_name)

             # If users choose option 2, allow them to access category and add question set.
            elif choice == 2:
                
                # Call list category.
                category_list = main_creator.list_categories()
                
                # Check if there is existing categories.
                if not category_list:
                    continue
                
                try:

                    # Allow users to choose from options.
                    options = int(input("\nChoose a category (0 to go back): "))
                    
                    # Check if the chosen option is valid.
                    if options == 0:
                        continue
                    elif 1 <= options <= len(category_list):
                        main_creator.add_question_set(category_list[options - 1])
                    
                     # Catch invalid input.
                    else:
                        print("Invalid selection.\n")
                
                 # Catch invalid input.
                except ValueError:
                    print("Invalid input.\n")

            # Allow users to exit the program.
            elif choice == 3:
                print("\nThank you for using Quizzo. Goodbye!\n")
                break
            
            # Catch invalid input.
            else:
                print("Invalid choice! Try again.\n")

        # Catch invalid input.
        except ValueError:
            print("Invalid input! Try again.\n")

# Run the main program.
if __name__ == "__main__":
    main_program()