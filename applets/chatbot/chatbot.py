## from openai.api_resources import Engine, Completion, engine
import openai

prompt = """"""


openai.Engine.retrieve("davinci")
testCompletion = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=500,
    n=3,
    temperature=0.9,
    presence_penalty=0.5,
    frequency_penalty=0.5,
)


for choice in testCompletion.choices:
    # print("Prompt:")
    # print(prompt)

    print("\n\n")

    print("Answer:")
    print(choice.text)

    print("\n\n\n\n\n")
