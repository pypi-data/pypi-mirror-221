import openai
import replicate
# OpenAI

def gpt3(api_key:str = "", prompt:str = ""):

    openai.api_key = api_key
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages= [{"role": "system", "content": prompt}])

    response = completion.choices[0].message
    return response

def gpt4(api_key:str = "", prompt:str = ""):

    openai.api_key = api_key
    
    completion = openai.ChatCompletion.create(    
        model="gpt-4-0613",
        messages= [{"role": "system", "content": prompt}])

    response = completion.choices[0].message
    return response

# Replicate

def stablelm7b(api_key: str = "", prompt: str = ""):
    
    client = replicate.Client(api_token=api_key)

    output = client.run(
        "stability-ai/stablelm-tuned-alpha-7b:c49dae362cbaecd2ceabb5bd34fdb68413c4ff775111fea065d259d577757beb",
        input={
            "prompt": prompt,
            "max_tokens": 500,
            "top_p": 1,
            "temperature": 0.75,
            "repetition_penalty": 1.2
        }
    )

    response = ''.join(output)
    return response

def vicuna_13b(api_key: str = "", prompt: str = ""):
    
    client = replicate.Client(api_token=api_key)

    output = client.run(
        "replicate/vicuna-13b:6282abe6a492de4145d7bb601023762212f9ddbbe78278bd6771c8b3b2f2a13b",
        input={
            "prompt": prompt,
            "max_tokens": 50,
            "top_p": 1,
            "temperature": 0.75,
            "repetition_penalty":1.2
            }
    )

    response = ''.join(output)
    return response

def flan_t5_xl(api_key: str = "", prompt: str = ""):
    
    client = replicate.Client(api_token=api_key)

    output = client.run(
        "replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210",
        input={
            "prompt": prompt,
            "max_tokens": 50,
            "top_p": 1,
            "temperature": 0.75,
            "repetition_penalty":1.2
            }
    )

    response = ''.join(output)
    return response

def llama70b(api_key: str = "", prompt: str = ""):
    
    client = replicate.Client(api_token=api_key)

    output = replicate.run(
        "replicate/llama70b-v2-chat:e951f18578850b652510200860fc4ea62b3b16fac280f83ff32282f87bbd2e48",
        input={"prompt": prompt}
    )
    # The replicate/llama70b-v2-chat model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    for item in output:
        # https://replicate.com/replicate/llama70b-v2-chat/versions/e951f18578850b652510200860fc4ea62b3b16fac280f83ff32282f87bbd2e48/api#output-schema
        print(item)

    response = ''.join(output)
    return response
