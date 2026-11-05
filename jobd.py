
from pydantic import BaseModel



class jobDescription(BaseModel):
    role: str
    requiredSkill: str
    minimumSkill: str
    preferredSkill: str
    experience: float
    education: str
    responsibilites: str
jobd_schema=jobDescription.model_json_schema()