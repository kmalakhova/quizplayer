from dataclasses import dataclass
from typing import List

@dataclass
class QuizQuestion:
    question: str
    # Ordered list of answer variants.
    variants: List[str]
    # Zero based number of the right answer in variants list.
    right_answer: int

@dataclass
class Quiz:
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
        right_answer = 0
    )

    second_question = QuizQuestion(
        question = 'What is the tallest building in the world?',
        variants = [
            'Federation Tower',
            'Burj Khalifa',
            'Eurasia',
        ],
        right_answer = 1
    )

    third_question = QuizQuestion(
        question = 'Which is the most dense city in India?',
        variants = [
            'Maharashtra',
            'Tamil Nadu',
            'Delhi',
        ],
        right_answer = 2
    )
    
    return Quiz(
        description = 'A fake quiz.',
        quiz_questions = [
            first_question,
            second_question,
            third_question]
    )

print('Welcome to QuizPlayer!')
fake_quiz = _CreateFakeQuiz()
print(fake_quiz)