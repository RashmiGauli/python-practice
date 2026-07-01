quiz = [
    {"question": "what is your name?", "answer":"claude"},
    {"question": "you annnoying?", "answer": "very"}
]
correct = 0
for item in quiz:
    print(item["question"])
    userInput = input("answer:")
    if userInput == item["answer"]:
        print("yay")
        correct += 1
    else:
        print("nay")
print(f"got it in {correct}/{len(quiz)} tries")
    