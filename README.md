# quizplayer
Learning has never been so easy - learn new things with Quiz Player!

It's often case that you need to prepare for a quiz. Sometimes you wish to have a person who might went you thru different questions so you can check yourself. Wait no more! It could never be easier to learn and repeat new things, Quiz Payer is here just for you.

### Quick Start.
1. Create a [json](https://en.wikipedia.org/wiki/JSON) file describing your quiz in the following format:
```
{
    "name": "Simple Quiz",
    "description": "Demo for quiz configuration",
    "quiz_questions":  [
        {
            "question": "What the biggest animal in the worlds?",
            "variants": [
                "Blue Whale",
                "Himalayan Brown Bear",
                "My Neighbor's Dog"
            ],
            "correct_answer": "0"
        },
        {
            "question": "What is the tallest building in the world?",
            "variants": [
                "Federation Tower",
                "Burj Khalifa",
                "Eurasia"
            ],
            "correct_answer": "1"
        },
        {
            "question": "Which is the most dense city in India?",
            "variants": [
                "Maharashtra",
                "Tamil Nadu",
                "Delhi"
            ],
            "correct_answer": "2"
        }
    ]
}
```
2. Run quiz player.
```
@> python main.py path_to_your_file.
```
3. Enjoy!

