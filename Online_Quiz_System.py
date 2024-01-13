# Quiz Application
'''
Create a Python program for an online quiz system. Implement classes for
quizzes, questions, and users. Include methods for taking quizzes, scoring, and
displaying results.
'''
import os  # Import the os module for clearing the screen

class Question:
    """
    Represents a single quiz question.
    """

    def __init__(self, text, options, correct_option):
        """
        Initializes the question with its text, options, and correct answer.

        Args:
            text (str): The question text.
            options (list): A list of answer options.
            correct_option (int): The index of the correct answer option.
        """

        self.text = text
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        """
        Prints the question text and its options.
        """

        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        """
        Checks if the user's answer is correct.

        Args:
            user_answer (int): The user's chosen answer option.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """

        return user_answer == self.correct_option


class Quiz:
    """
    Represents a quiz with multiple questions.
    """

    def __init__(self, name, questions):
        """
        Initializes the quiz with its name and a list of questions.

        Args:
            name (str): The name of the quiz.
            questions (list): A list of Question objects.
        """

        self.name = name
        self.questions = questions

    def take_quiz(self, user):
        """
        Administers the quiz to the user.

        Args:
            user (User): The user object representing the quiz taker.

        Returns:
            int: The user's score on the quiz.
        """

        print(f"Welcome {user.name}, to the {self.name} quiz!")
        score = 0

        for question in self.questions:
            print()
            question.display_question()
            user_answer = int(input("Your answer (enter the option number): "))

            if question.check_answer(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was option {question.correct_option}.\n")

        print(f"Quiz completed! Your score: {score}/{len(self.questions)}")
        return score


class User:
    """
    Represents a quiz user.
    """

    def __init__(self, name):
        """
        Initializes the user with their name.

        Args:
            name (str): The user's name.
        """

        self.name = name

# ... (Rest of the code with comments)
