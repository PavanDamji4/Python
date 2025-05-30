#: Mini-Game

# Create a program capable of displaying Questions to the user like KBC
# Use list data-type to store the questions and their correct answers
# Display the final amount the person takes home post game-play

print("*************** Welcome to Quiz Game *****************")
print("Note :- There are 4 questions and you can win 100$ per question.\n")

questions = [
    "1. What is the National Bird of India? ",
    "2. What is the tallest mountain in the world? ",
    "3. How many players are there in a cricket team? ",
    "4. What is the currency of Japan? "
]

answers = ["peacock", "mount everest", "11", "yen"]
prize = 100
score = 0

for i in range(4):
    ans = input(questions[i])
    if ans.lower() == str(answers[i]):
        score += prize
        print(" Correct! You won ",prize)
    else:
        print(" Wrong answer!\n")

print(" Game Over! You take home a total of $", score)
