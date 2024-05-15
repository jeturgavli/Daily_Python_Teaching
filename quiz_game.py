
# -----------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in question:
        print("-----------------------------")
        print(key)
        for i in option[question_num-1]:
            print(i)
        guess = input("Enter (A , B, C, or D) : ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_ans(question.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

# -----------------------------
def check_ans(answer, guess):
    if answer == guess:
        print("Correct Answer.. :)")
        return 1
    else:
        print("Wrong Answer.. :(")
        return 0
# -----------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULT")
    print("-----------------------------")
    print("Answer  : ", end = "")
    for i in question:
        print(question.get(i), end= " ")
    print()

    print("Guesses : ", end = "")
    for i in guesses:
        print(i , end= "")
    print(i)
    

# -----------------------------
def play_again():
    pass


question = {
    "Who created python ? : " : "A",
    "what year was python created? : ": "B",
    "Python is tributed to which comedy group? : ": "C",
    "Is the Earth round? : ": "A"
}

option = [
    ["A. Guido van Rossum", "B. Elon Mask", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()