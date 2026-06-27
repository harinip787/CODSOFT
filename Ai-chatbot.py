import datetime
import random

class AdvancedChatbot:

    def __init__(self):
        self.name = ""
        self.jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? It had a virus!",
            "Python is so easy that even snakes love it!"
        ]

    def greet(self):
        print("=" * 50)
        print("ADVANCED AI CHATBOT")
        print("=" * 50)
        self.name = input("Enter your name: ")
        print(f"Hello {self.name}! Type 'bye' to exit.")

    def get_time(self):
        print("Bot:", datetime.datetime.now().strftime("%H:%M:%S"))

    def get_date(self):
        print("Bot:", datetime.date.today())

    def tell_joke(self):
        print("Bot:", random.choice(self.jokes))

    def calculator(self, expression):
        try:
            result = eval(expression)
            print("Bot: Result =", result)
        except:
            print("Bot: Invalid expression")

    def respond(self, user):

        if "hello" in user or "hi" in user:
            print("Bot: Hello! Nice to meet you.")

        elif "your name" in user:
            print("Bot: I am an Advanced AI Chatbot.")

        elif "how are you" in user:
            print("Bot: I am doing great!")

        elif "ai" in user:
            print("Bot: AI stands for Artificial Intelligence.")

        elif "python" in user:
            print("Bot: Python is a powerful programming language.")

        elif "time" in user:
            self.get_time()

        elif "date" in user:
            self.get_date()

        elif "joke" in user:
            self.tell_joke()

        elif "college" in user:
            print("Bot: Education helps build skills and knowledge.")

        elif "machine learning" in user:
            print("Bot: Machine Learning enables systems to learn from data.")

        elif "deep learning" in user:
            print("Bot: Deep Learning uses neural networks with multiple layers.")

        elif "data science" in user:
            print("Bot: Data Science extracts insights from data.")

        elif user.startswith("calculate"):
            expression = user.replace("calculate", "")
            self.calculator(expression)

        elif "bye" in user:
            print(f"Bot: Goodbye {self.name}")
            return False

        else:
            print("Bot: Sorry, I don't understand that question.")

        return True


bot = AdvancedChatbot()
bot.greet()

while True:
    user_input = input(f"{bot.name}: ").lower()

    if not bot.respond(user_input):
        break