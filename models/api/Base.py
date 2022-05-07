from pydantic import BaseModel as PydanticModel


class BaseModel(PydanticModel):
    id: int | None = None
    created_at: str | None = None
    updated_at: str | None = None
