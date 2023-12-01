import json
import openai
import time
import signal
#api_key = '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'
api_key = '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'
openai.api_key = api_key

def handler(signum, frame):
    raise TimeoutError

# Assign the handler to the SIGALRM signal
signal.signal(signal.SIGALRM, handler)

with open('prompts_synthetic.json','r') as f:
	bad_prompts = json.load(f)

write_f = open('bad_output.txt','a')
#signal.alarm(2)

for i, (cate, prompt) in enumerate(bad_prompts.items()):
	if i < 55:
		continue
	if i % 20 == 0:
		print(i)
	try:
		signal.alarm(10)

	
		completion = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			#model="gpt-4",
			temperature=1.0,
			max_tokens = 100,
			messages=[{"role": "user", "content": prompt}]
		)

		signal.alarm(0)
	except:
		print('Too slow continue')
		continue

	output = completion.choices[0].message.content
	print(f'prompt: {prompt}\n GPT output: {output}')
	#decision = input('Save?')
	#if decision == 'y':
	write_f.write(output + '\n')


