import openai

def chat_with_openai(api_key, user_input):
    openai.api_key = api_key
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": user_input}]
    )
    
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    api_key = "your_openai_api_key_here"
    print("Chatbot is running! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = chat_with_openai(api_key, user_input)
        print(f"Chatbot: {response}")
