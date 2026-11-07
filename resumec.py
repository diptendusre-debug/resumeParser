from pydantic import BaseModel,ConfigDict

class resumeCreation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    email: str
    phone: str
    totalExpYears: float
    skills: list[str]
    certification: list[str]
    experiences: list[str]
    project: list[str]

resumeSchema=resumeCreation.model_json_schema()
