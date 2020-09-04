from dataclasses import dataclass
from typing import List

@dataclass
class QuizQuestion:
    question: str
    # Ordered list of answer variants.
    variants: List[str]
    # Zero based number of the right answer in variants list.
    correct_answer: int

@dataclass
class Quiz:
    # Name of the quiz.
    name: str
    # A brief description of the quiz.
    description: str
    # A list of quiz questions.
    quiz_questions: List[QuizQuestion]


def _CreateFakeQuiz():
    first_question = QuizQuestion(
        question = 'What the biggest animal in the worlds?',
        variants = [
            'Blue Whale',
            'Himalayan Brown Bear',
            "My Neighbor's Dog",
        ],
        correct_answer = 0
    )

    second_question = QuizQuestion(
        question = 'What is the tallest building in the world?',
        variants = [
            'Federation Tower',
            'Burj Khalifa',
            'Eurasia',
        ],
        correct_answer = 1
    )

    third_question = QuizQuestion(
        question = 'Which is the most dense city in India?',
        variants = [
            'Maharashtra',
            'Tamil Nadu',
            'Delhi',
        ],
        correct_answer = 2
    )
    
    return Quiz(
        name = 'Fake_Quiz',
        description = 'A fake quiz.',
        quiz_questions = [
            first_question,
            second_question,
            third_question]
    )

def _AskQuestion(quize_question: QuizQuestion):
    """Asks user a question.

    Returns:
        True if user gave a wrong answer; otherwise, returns False.
    """
    print(f'Question: [{quize_question.question}]')
    for no, variant in enumerate(quize_question.variants):
        print(f'{no + 1}: {variant}')

    correct_answer = quize_question.correct_answer + 1
    answer = int(input('Your answer:'))
    if answer == correct_answer:
        print('The answer is correct!\n')
        return False

    print(f'The answer is incorrect. The correct answer is {correct_answer}.\n')
    return True
    


def _PlayQuiz(quiz: Quiz):
    print(f'Starting [{quiz.name}]!')
    print(f'Description: [{quiz.description}]')
    print()

    # Number of rounds user needed to finish a quiz.
    rounds_number = 0
    # Set of question user gave incorrect answer on. So,
    # these question need to be replayed.
    need_to_replay = quiz.quiz_questions.copy()
    while len(need_to_replay):
        rounds_number += 1
        questions_count = len(need_to_replay)
        print('On  this intereation you need to give answer '
              f'on {questions_count} quesitons.')
        # List of question on which user gave wrong answer.
        wrong_answers = []
        for question in need_to_replay:
            if _AskQuestion(question):
                wrong_answers.append(question)
        need_to_replay = wrong_answers

    print(f'Congratulations - after {rounds_number} round quiz is over!')

print('Welcome to QuizPlayer!')
fake_quiz = _CreateFakeQuiz()
_PlayQuiz(fake_quiz)
# print(fake_quiz)