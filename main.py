import os
from groq import Groq
from dotenv import load_dotenv
from jobd import jobd_schema
from resumeRead import readResume
import time
from resumec import resumeSchema

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
    response=client.chat.completions.create(model=model,messages=messages,temperature=0,response_format={"type":"json_schema","json_schema":{"name":"jobd_schema","strict":True,"schema":jobd_schema}})
    jobrequirements=response.choices[0].message.content
    print("***********Extracted Job Requirements:************")
    print(jobrequirements)
    print("**************************************************")
    time.sleep(5)
    resumeMessage=readResume()
    
    systemMessage1 = {
        "role": "system",
        "content": """
        You are an expert Resume Information Extraction Agent.

        Analyze the resume provided by the user.

        Extract the following information:

        1. name: Candidate's full name.
        2. email: Candidate's email address.
        3. phone: Candidate's phone number.
        4. totalExpYears: Total professional experience in years.
        5. skills: List of technical and professional skills.
        6. certification: List of certifications.
        7. experiences: List of professional work experiences.
        8. project: List of projects.

        STRICT INSTRUCTIONS:

        - Return all eight fields.
        - Do not omit any field.
        - Do not invent information.
        - For missing string values, return "".
        - For missing list values, return [].
        - For missing numerical values, return 0.
        - totalExpYears must be a number.
        - skills, certification, experiences and project
        must always be arrays of strings.
        - Follow the JSON schema provided in the API request.
        - Return structured JSON only.
        """
    }
    allresumedeils=[]
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
        allresumedeils.append(resumedetails)
        print("**************************************************")
        time.sleep(5)
    systemMessage2={
        "role":"system",
        "content":"You are advance resume parsing agent.You need to compare the jobrequirements and allresumedeils. "
        "Once all the comparison is done give me the best suitable candidate name,phone no and email in json format"
        }
    message2={
        "role":"user",
        "content":f"Job Requirements: {jobrequirements} Candidates Resume: {allresumedeils}"
    }
    messages3=[systemMessage2,message2]
    finalresponse=client.chat.completions.create(model=model,messages=messages3)
    print(finalresponse.choices[0].message.content)
    




if __name__=="__main__":
    main()