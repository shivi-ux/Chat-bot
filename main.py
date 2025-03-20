qna = {
    "hi":"hey",
    "how are you":"I am fine",
    "what is your name":"My name is shivani",
    "how old are you":"I am 21 years old",
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna.get(qs, "Sorry, I don't understand that."))