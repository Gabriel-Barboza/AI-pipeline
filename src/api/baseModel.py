from pydantic import BaseModel , Field

class IrisFeatures(BaseModel):
    sepal_length: float = Field(
        ..., 
        example=5.1, 
        description="Comprimento da sépala (em cm)"
    )
    sepal_width: float = Field(
        ..., 
        example=3.5, 
        description="Largura da sépala (em cm)"
    )
    petal_length: float = Field(
        ..., 
        example=1.4, 
        description="Comprimento da pétala (em cm)"
    )
    petal_width: float = Field(
        ..., 
        example=0.2, 
        description="Largura da pétala (em cm)"
    )