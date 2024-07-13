from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List


def get_current_utc_time():
    return datetime.now(timezone.utc)


class Records(BaseModel):
    record_identifier: str
    description: str
    timestamp: datetime = Field(default_factory=get_current_utc_time)
    category: int

class DeleteIDsModel(BaseModel):
    ids: List[str]
