from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List

# Function to get the current time in UTC
def get_current_utc_time():
    return datetime.now(timezone.utc)

# Pydantic model for Records
class Records(BaseModel):
    record_identifier: str
    description: str
    timestamp: datetime = Field(default_factory=get_current_utc_time)
    category: int

# Pydantic model for DeleteIDsModel
class DeleteIDsModel(BaseModel):
    ids: List[str]  # List of record identifiers to delete
