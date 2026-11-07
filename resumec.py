from pydantic import BaseModel

class resumeCreation(BaseModel):
    name: str
    email: str
    phone: str
    totalExpYears: int
    skills: list[str]
    certification: list[str]
    experiences: list[str]
    project: list[str]

resumeSchema=resumeCreation.model_json_schema()
