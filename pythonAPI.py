import openai

# Import the OpenAI model and attach the API key
API_KEY = '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'
openai.api_key = API_KEY
model_id = 'gpt-3.5-turbo'

def chatgpt_conversation(conversation_log):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation_log
    )

    conversation_log.append({
        'role': response.choices[0].message.role, 
        'content': response.choices[0].message.content.strip()
    })
    return conversation_log

conversations = []
# system, user, assistant
conversations.append({'role': 'system', 'content': 'How may I help you?'})
conversations = chatgpt_conversation(conversations)
print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))

while True:
    prompt = input('User: ')
    conversations.append({'role': 'user', 'content': prompt})
    conversations = chatgpt_conversation(conversations)
    print()
    print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))
