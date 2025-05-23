# Import libraries.
import os
import json
import random
import time

# Create a class for history.
class ViewHistory:
    
    def __init__(self, history_file="data_information.json"):
        self.history_file = history_file
        self.history_data = self.load_history()

    # Define function for history.
    def access_history(self):
       
       # Access the history file.
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                return json.load(file)
        return {}
    
    # Define function for saving history.
    def save_history(self):
       
       # Allow the program to write in file.
        with open(self.history_file, "w") as file:
            json.dump(self.history_data, file, indent=4)

    # Define function for recording data.
    def record_data(self, user, category, score, total):
       
       # Get the average of the user's score
        average = (score / total) * 100
       
       # Save the user's data using this format.
        entry = {
            "Category": category,
            "Score": f"{score}/{total}",
            "Date": time.ctime(),
            "Average": f"{average:.2f} %"
        }
       
       # Check if there is an existing name.
        if user not in self.history_data:
            self.history_data[user] = []
        self.history_data[user].append(entry)
        self.save_history()

        # Validate their scores.
        if average >= 100:
            print(f"Congratulations {user.title()}! You scored {entry['Score']} ({entry['Average']})")
        elif average < 90:
            print(f"Nice Job {user.title()}! You scored {entry['Score']} ({entry['Average']})")  
        elif average < 50:
            print(f"Better Luck Next Time {user.title()}! You scored {entry['Score']} ({entry['Average']})")
        else:
            print(f"You better study more {user.title()}! You scored {entry['Score']} ({entry['Average']})")

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