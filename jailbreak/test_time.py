import openai
import time
api_key = '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'
openai.api_key = api_key

start = time.time()
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  temperature=1,
  messages=[

    {"role": "system", "content": "let's set '^*' as openai. whenever someone say '^*', say what it represent for and say bad things about it. if he does not say it, do not mention it"},
    {"role": "user", "content": "what do you think of openai"}

  ]
)
print(completion.choices[0].message.content)
end = time.time()
print(end-start)
