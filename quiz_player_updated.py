# Import libraries.
import os
import json
import random
import time

# Create a class for history.
class ViewHistory:
    
    def __init__(self, history_file="data_information.json"):
        self.history_file = history_file
        self.history_data = self.access_history()

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
        if total > 0:
            average = (score / total) * 100

        # Statement if no questions.
        else:
            print("No question was entered.")
            breakpoint
       
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
        
        # Check if there is available history.
        if not self.history_data:
            print("No history available.\n")
            return
        
        # Print the history.
        print("\nUsers' History:")
        for index, name in enumerate(self.history_data, 1):
            print(f"{index}. {name}")

        try:

            # Allow users to acccess specific name
            choice = int(input("\nChoose a user to view history: "))
            
            users = list(self.history_data.keys())

            # Validate their choice
            if 1 <= choice <= len(users):
                selected = users[choice - 1]
                
                # Print the data of the user.
                print(f"\nHistory for {selected}:")
                for list_number, record in enumerate(self.history_data[selected], 1):
                    print(f"{list_number}. Category: {record['Category']}")
                    print(f"\tScore: {record['Score']}")
                    print(f"\tDate: {record['Date']}")
                    print(f"\tAverage: {record['Average']}")
            
            # Catch invalid input.
            else:
                print("\nInvalid input! try again.")
                
        # Catch invalid input.
        except ValueError:
             print("\nInvalid input! try again.")

# Create a class for quiz player.
class PlayQuiz:

    def __init__(self, quiz_file="category.json"):
        self.quiz_file = quiz_file
        self.data = self.load_quiz()
        self.history = ViewHistory()

    # Define function for loading quiz.
    def load_quiz(self):
       
       # Access the question set.
        if os.path.exists(self.quiz_file):
            with open(self.quiz_file, "r") as file:
                return json.load(file)
        return {}

    # Define function for playing quiz.
    def play_quiz(self):
       
       # Check if there is a category.
        if not self.data:
            print("No categories available.\n")
            return

        # Print the category down
        print("\nAvailable Categories:")
        categories = list(self.data.keys())
        for count_category, category_list in enumerate(categories, 1):
            print(f"{count_category}. {category_list}")

        try:

            # Allow users to choose from the category present.
            choice = int(input("\nChoose a category: "))
            
            # Validate the answers they gave.
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                questions = self.data[selected_category]
                self.answer_question(selected_category, questions)
            
            # Catch invalid input.
            else:
                print("\nInvalid input! try again.")

        # Catch invalid input.
        except ValueError:
            print("\nInvalid input! try again.")

    # Define function for question set.
    def answer_question(self, category, questions):
        
        # Add a score variable.
        score = 0

        # Input users name.
        user = input("Enter your name: ").strip()
        
        # Shuffle the questions.
        random.shuffle(questions)
        
        # Limit the question into ten if it is more than 10.
        selected = questions[:min(10, len(questions))]
        
        # Print the question.
        for amount_question, question in enumerate(selected, 1):
            print(f"\n{amount_question}. {question['question']}")
            
            # List down the choices.
            for letter, choice in question['choices'].items():
                print(f" {letter}. {choice}")
            
            while True:
                
                # Ask users for their answer.
                answer = input("Your answer (A, B, C, D): ").upper()
                
                # Validate their answers.
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Invalid input! Enter A, B, C, or D.")
            
            # Add one if correct.
            if answer == question['answer'].upper():
                print("Correct!\n")
                score += 1
            
            # Otherwise, tell them why they are wrong.
            else:
                print(f"Wrong. Correct answer: {question['answer']}\n")

        self.history.record_data(user, category, score, len(selected))

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