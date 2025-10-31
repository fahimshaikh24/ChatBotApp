# Author : Fahim Shaikh
# Simple Rule-Based Chatbot


print("🤖 Hi! I'm ChatBot. Type 'bye' to exit.")
print("---------------------------------------")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hello there! How can I help you today?")

    elif "how are you" in user_input:
        print("ChatBot: I'm just a bunch of code, but I'm doing great! How about you?")

    elif "name" in user_input:
        print("ChatBot: My name is ChatBot — your virtual assistant.")

    elif "weather" in user_input:
        print("ChatBot: I can’t feel it, but I hope it’s sunny where you are ")

    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        print(f"ChatBot: The current time is {now}")

    elif "date" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%d %B %Y")
        print(f"ChatBot: Today's date is {today}")

    elif "your creator" in user_input or "who made you" in user_input:
        print("ChatBot: I was created by a Python developer for learning purposes ")

    elif "help" in user_input:
        print("ChatBot: Sure! You can ask me about time, date, weather, or just chat casually 🙂")

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        print("ChatBot: Goodbye! Have a great day ")
        break

    else:
        print("ChatBot: Sorry, I didn’t understand that. Can you please rephrase?")
