import os
from groq import Groq
from dotenv import load_dotenv
from jobd import jobd_schema,jobDescription
from resumeRead import readResume
import time
from resumec import resumeCreation,resumeSchema
from resumeRead import readResume

load_dotenv()
#Getting the API Key from environment Variable
my_api_keys=os.getenv("GROQ_API_KEY")
if not my_api_keys:
    raise ValueError("API Key is not available")
client=Groq(api_key=my_api_keys)
model="qwen/qwen3.8-27b"

def userInput():
    print("Please enter the Job description in detailed way.Type exit to finish")
    lines=[]
    while True:
        line=input()
        if line.lower()=="exit":
            break;
        lines.append(line)
    return "\n".join(lines)


def main():
    userMessage=userInput()
    if not userMessage.strip():
        raise ValueError("No Job Description Provide")
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
    jobrequirements=response.choices[0].message.content
    print("***********Extracted Job Requirements:************")
    print(jobrequirements)
    print("**************************************************")
    time.sleep(5)
    resumeMessage=readResume()
    systemMessage1={
        "role":"system",
        "content":"You are advance resume parsing agent.Yu need to go through the resume data and create the resume details "
        "in json format using the resumeSchema"
    }
    for resume in resumeMessage:
        resumeInput={
            "role":"user",
            "content":resume["content"]
        }
        messages=[systemMessage1,resumeInput]
        response=client.chat.completions.create(model=model,messages=messages,response_format={"type":"json_schema","json_schema":{"name":"resumeSchema","strict":True,"schema":resumeSchema}})
        resumedetails=response.choices[0].message.content
        print("***********Extracted Resume Details :************")
        print(resumedetails)
        print("**************************************************")
    time.sleep(5)
    




if __name__=="__main__":
    main()