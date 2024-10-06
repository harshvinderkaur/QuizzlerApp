This Quizzer App is a Python-based trivia game application that fetches true/false questions from the Open Trivia Database. The app features a graphical interface built using Tkinter where users are allowed to answer multiple-choice questions and receive instant feedback.

Modules:

1. Main.py: Initializes the quiz by fetching questions from the API, formats them into objects and starts the quiz interface.
2. UI.py: Manages the graphical interface, displaying questions and score and handling user input.
3. QuizBrain.py: Controls the quiz logic, including question progression, answer validation and score tracking.
4. Question_model.py: Defines the structure of a question with text and answer attributes.
5. Data.py: Pulls question data using OpenTDB API, formats it into a usable list of questions.
