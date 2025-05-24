from function_for_quiz_creator_and_player import QuizCreator

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