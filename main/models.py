from typing import List

from pydantic import BaseModel


class AdPlatformResponse(BaseModel):
    platforms: List[str]
