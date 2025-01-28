data={
        "hi": "Hi there!!! I'm a friendly chatbot here to assist you.",
    "hello": "Hello!!! How can I help you today?",
    "what is your name": "I don't have a name, I'm Sanjay's created chatbot.",
    "what did you eat today": "I don't eat, but I can help you find food-related information and recipes.",
    "what is your favorite color": "I'm just a chatbot, I don't have any personal preferences for colors.",
    "do you enjoy listening to music": "I'm just a chatbot, I can't listen to music.",
    "how are you": "I'm just a program, but thanks for asking! How can I assist you?",
    "what is ai": "AI, or Artificial Intelligence, refers to systems or machines that mimic human intelligence to perform tasks.",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus!",
    "what can you do": "I can answer your questions, chat with you, and assist you with basic information!",
    "how old are you": "I don't age! I'm as new as the day I was created.",
    "who created you": "I was created by Sanjay!",
    "what is your purpose": "My purpose is to assist, chat, and provide helpful information to users like you.",
    "thank you": "You're welcome! Let me know if there's anything else I can help you with.",
    "bye": "BYE!! Take care and have a great day."

}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
        return "I'm sorry, I didn't understand that. Can you please rephrase your setence?"
print("Chatbot: Hi! I'm just a chatbot,I'm here to assist you!!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response=get_response(user_input)
    print("Chatbot:",response) 
