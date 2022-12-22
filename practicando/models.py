from tortoise import fields, models

from tortoise.contrib.pydantic import pydantic_model_creator

class Persona(models.Model):
    
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=250)
    age = fields.CharField(max_length=250)
    
    class PydanticMeta:
        pass
    
persona_Pydantic = pydantic_model_creator(Persona, name="Persona")
personaIn_Pydantic = pydantic_model_creator(Persona, name="PersonaIn", exclude_readonly=True)