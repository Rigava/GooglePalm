import google.generativeai as palm
palm.configure(api_key = "AIzaSyAKEaaM7fWIErN3VbikjP_T5m0UfhBy5iE")
models = [m for m in palm.list_models() 
          if 'generateText' 
          in m.supported_generation_methods]
model_bison = models[0]
from google.api_core import retry
@retry.Retry()
def generate_text(prompt,
                  model=model_bison,
                  temperature=0.0):
    return palm.generate_text(prompt=prompt,
                              model=model,
                              temperature=temperature)
# Prompt template - # priming: getting the LLM ready for the type of task you'll ask it to do.
# question: the specific task.
# decorator: how to provide or format the output.
prompt_template = """
{priming}

{question}

{decorator}

Your solution:
"""
priming_text = "You are an expert at writing clear, concise, Python code."
question = "create a very large list of random numbers in python, and then write code to sort that list"
# option 1
# decorator = "Work through it step by step, and show your work. One step per line."
# option 2
decorator = "Insert comments for each line of code."
prompt = prompt_template.format(priming=priming_text,
                                question=question,
                                decorator=decorator)
# print(prompt)

completion = generate_text(prompt)
print(completion.result)
