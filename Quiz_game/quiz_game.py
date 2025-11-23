import time

questions = {
    "1. What is the capital of India?": "delhi",
    "2. Who developed Python?": "guido van rossum",
    "3. What is 5 * 6?": "30",
    "4. Which keyword defines a function in Python?": "def",
    "5. What does AI stand for?": "artificial intelligence"
}

score = 0

print("\n📘 Welcome to the Python Quiz Game!")
print("You will get 5 questions. Type your answer.\n")

time.sleep(1)

for q, a in questions.items():
    print(q)
    user_answer = input("👉 Your Answer: ").lower().strip()

    if user_answer == a:
        print("✔ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {a}\n")

    time.sleep(0.5)

print("------------------------------------------------")
print(f"🏁 Quiz Finished! Your Final Score: {score}/{len(questions)}")

if score == len(questions):
    print("🔥 Excellent! Full Marks!")
elif score >= 3:
    print("👍 Good job! Keep improving!")
else:
    print("📚 You need practice, but don’t give up!")
print("------------------------------------------------")
