import os
from groq import Groq
from dotenv import load_dotenv
from jobd import jobd_schema,jobDescription

load_dotenv()
#Getting the API Key from environment Variable
my_api_keys=os.getenv("GROQ_API_KEY")
if not my_api_keys:
    raise ValueError("API Key is not available")
client=Groq(api_key=my_api_keys)
model="qwen/qwen3.8-27b"

def userInput():
    userMessage=input("Please enter the Job description in detailed way: ")
    if not userMessage:
        raise NameError("Job Description is not mentioned.Please enter at least a job description")
    return userMessage


def main():
    userMessage=userInput()
    systemMessage={
        "role":"system",
        "content":"You are advance resume parsing agent.The user has given you input about the job description.Your task is to read the job description and convert the job description "
        "in json format using the jobd_schema"
    }
    user_Input={
        "role":"user",
        "content":userMessage
    }
    messages=[systemMessage,user_Input]
    response=client.chat.completions.create(model=model,messages=messages,response_format={"type":"json_schema","json_schema":{"name":"jobd_schema","strict":True,"schema":jobd_schema}})

if __name__=="__main__":
    main()