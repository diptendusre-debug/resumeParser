from pydantic import BaseModel,ConfigDict,Field

class resumeCreation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str =Field(description="Candidate Full name")
    email: str =Field(description="candidates email id ")
    phone: str =Field(description="candidated phone no")
    totalExpYears: float =Field(description="candidated Experience")
    skills: list[str] =Field(description="candidated skill, Return empty string if unavailable")
    certification: list[str] =Field(description="candidated certification, Return empty string if unavailable")
    experiences: list[str] =Field(description="candidated experience")
    project: list[str] =Field(description="candidated projects")

resumeSchema=resumeCreation.model_json_schema()
