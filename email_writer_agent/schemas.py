from pydantic import BaseModel, Field
from typing import Optional, List

class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email. Should be concise and descriptive of the email's content.")
    body: str = Field(description="The main content of the email. Should be well formatted with proper greetings, paragraphs, and closings.")