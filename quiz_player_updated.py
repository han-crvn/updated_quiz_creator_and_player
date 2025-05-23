# Import libraries.
import os
import json
import random
import time

# Create a class for history.
class ViewHistory:
    
    def __init__(self):
        pass

    # Define function for history.
    def access_history(self):
        pass
    
    # Define function for saving history.
    def save_history(self):
        pass

    # Define function for recording data.
    def record_data(self):
        pass

    # Define function for viewing history.
    def view_history(self):
        pass

# Create a class for quiz player.
class PlayQuiz:

    def __init__(self):
        pass

    # Define function for loading quiz.
    def load_quiz(self):
        pass

    # Define function for playing quiz.
    def play_quiz(self):
        pass

    # Define function for question set.
    def asnswer_question(self):
        pass

# Define function for main program (quiz player).
def main_program():
    
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
                pass
            
            # If users choose 2, they will be able to access history.
            elif choice == 2:
                pass
            
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