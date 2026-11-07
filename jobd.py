
from pydantic import BaseModel,ConfigDict



class jobDescription(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: str
    requiredSkill: str
    minimumSkill: str
    preferredSkill: str
    experience: float
    education: str
    responsibilities: str
jobd_schema=jobDescription.model_json_schema()