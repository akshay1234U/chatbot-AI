# Simple chatbot using if-else statements

def chatbot_response(user_input):
    user_input = user_input.lower()  


    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm functioning as expected! How about you?"
    elif "weather" in user_input:
        return "The weather is looking great! Do you want to know more about a specific location?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: " + chatbot_response(user_input))
        break
    print("Chatbot: " + chatbot_response(user_input))
