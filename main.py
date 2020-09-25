import json
import sys
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

def _ParseKeywordFromData(data, filename: str, keyword: str):
    if keyword not in data:
        raise ValueError(f'[{filename}] has invalid format, [{keyword}] keyword absents.')
    return data[keyword]

def _ParseQuizQuestion(data, filename: str)->List[QuizQuestion]:
    json_questions = _ParseKeywordFromData(data, filename, 'quiz_questions')
    parsed_questions = []
    for json_question in json_questions:
        parsed_questions.append(QuizQuestion(
            question=_ParseKeywordFromData(json_question, filename, 'question'),
            variants=_ParseKeywordFromData(json_question, filename, 'variants'),
            correct_answer=int(_ParseKeywordFromData(json_question, filename, 'correct_answer')),
        ))
    return parsed_questions

def _ReadQuiz(filename: str)->Quiz:
    with open(filename) as f:
        data = json.load(f)
       
    quiz = Quiz(
        name=_ParseKeywordFromData(data, filename, 'name'),
        description=_ParseKeywordFromData(data, filename, 'description'),
        quiz_questions=_ParseQuizQuestion(data, filename))
    return quiz


if (len(sys.argv) > 2):
    raise SystemExit('Extected strictly two arguments. usage: @> main.py filename.')
filename = sys.argv[1]
print('Welcome to QuizPlayer!')
print(f'Reading quiz from file [{filename}]')
quiz = _ReadQuiz(filename)
_PlayQuiz(quiz)