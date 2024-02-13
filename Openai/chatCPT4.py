import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me a joke."}
  ]
)

print(response.choices[0].message['content'])
