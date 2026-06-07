import random
questions = [
    {
        "question": "Which planet has the most moons?",
        "options": ["A) Jupiter", "B) Saturn", "C) Uranus", "D) Neptune"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "In which year did the Berlin Wall fall?",
        "options": ["A) 1987", "B) 1989", "C) 1991", "D) 1993"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Go", "B) Gd", "C) Gl", "D) Au"],
        "answer": "D"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["A) Nucleus", "B) Ribosome", "C) Mitochondria", "D) Vacuole"],
        "answer": "C"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "B"
    },
    {
        "question": "Which country will win the Fifa world cup",
        "options": ["A) Brazil", "B) Argentina", "C) Portugal", "D) France"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A) Central Process Unit", "B) Computer Personal Unit", "C) Central Processing Unit", "D) Core Processing Unit"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "How many girls are there in the class?",
        "options": ["A) 0", "B) 1", "C) 2", "D) Is sonia a girl"],
        "answer": "C"
    }

]
def start_quiz():
    i=1
    score=0
    random.shuffle(questions)
    for q in questions:
            print(f"Q{i}:{q['question']}")
            for option in q['options']:
                print(f"{option}")
            while True:
                try:
                    answer = input().strip().upper()
                    if answer not in ["A", "B", "C", "D"]:
                        raise ValueError
                    break
                except ValueError:
                    print("must be A, B, C or D")
                
            if answer == q['answer']:
                print("correct")
                        
                score +=1
            else:
                print("oops, wrong answer") 
            i +=1         
    if score< 5:
        print (f"your score is{score} /n")
        print("someone needs to study")
    elif score<8:
        print (f"your score is{score} /n")
        print("good attempt")
    elif score >8:
        print (f"your score is{score} /n")
        print("Lets gooo, ur a rockstarrr")


start_quiz()
