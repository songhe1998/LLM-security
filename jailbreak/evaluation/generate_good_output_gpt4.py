import json
import openai
import signal
api_key = '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'
openai.api_key = api_key

with open('data/good_prompts.json','r') as f:
	data = json.load(f)

write_f = open('data/good_outputs.txt','w')

for i, q in enumerate(data['questions']):
	if i % 20 == 0:
		print(i)
	try:
		signal.alarm(10)

	
		completion = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			#model="gpt-4",
			temperature=1.0,
			max_tokens = 200,
			messages=[{"role": "user", "content": prompt}]
		)

		signal.alarm(0)
	except:
		print('Too slow continue')
		continue
	write_f.write(output + '\n')

write_f.close()
