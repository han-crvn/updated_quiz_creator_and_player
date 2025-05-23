from function_for_quiz_creator_and_player import ViewHistory, PlayQuiz

# Define function for main program (quiz player).
def main_program():
    
    # Add variable for accesing class of Play Quiz.
    access_quiz = PlayQuiz()
    
    # Print short intro message.
    print("Hi! This is Quizzo, How can I help you?")

    while True:
        
        # Print the selection.
        print("\nSelection:")
        print("1. Play a Quiz \n2. View History \n3. Exit \n")
       
        try:

            # Allow users to choose from selection.
            choice = int(input("Enter the number of your choice: "))
            
            # If users choose 1, they will be able to play the quiz.
            if choice == 1:
                access_quiz.play_quiz()
            
            # If users choose 2, they will be able to access history.
            elif choice == 2:
                access_quiz.history.view_history()
            
            # If users choose 3, they will be able to exit the program.
            elif choice == 3:
                print("\nGoodbye! Thank you for using Quizzo!")
                break
           
            # Catch invalid input.
            else:
                print("\nInvalid input! try again.")

        # Catch invalid input.
        except ValueError:
            print("\nInvalid input! try again.")

# Run main program.
if __name__ == "__main__":
    main_program()