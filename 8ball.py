#Felix Tan
#8 Ball
#1/22

#Inital
answers = ["It is certain", "Ask again later", "Signs point to yes", "Very doubtful", "My sources say no", "Better not tell you now", "Cannot predict now", "Without a doubt", "Outlook good", "Outlook not so good"]
import random
#Main
def magic8ball():
    while True:
        og = input("Ask me any question: ")
        if og.endswith("?", 1):
            print(random.choice(answers))
            question = input("Would you like to ask another question? ")
            if question == "no":
                break
        else:
            print("Invalid question, please re-enter question")

magic8ball()