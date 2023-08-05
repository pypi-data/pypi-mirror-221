
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from .gen_base import GenBase


class CourseMetadataModel(BaseModel):
    title: str = Field(
        description="title of the course of only 3 words")
    description: str = Field(
        description="description of the course which is an introduction article of maximum 40 words")


class GenCourseMetadata(GenBase):
    """
    Generator class for course metadata(title, description, etc.) using the description as text.
    """
    SYSTEM_PROMPT = """Act like a copywriter expert in course editing"""
    HUMAN_PROMPT = """Write a title of only 3 words and an introduction article to a course of maximum 40 words based on the following:
---
Description: {course_description}
---
"""

    def __init__(self, llm, verbose: bool = False):
        super().__init__(llm, verbose)

    def get_output_parser(self):
        return PydanticOutputParser(pydantic_object=CourseMetadataModel)

    def generate(self,
                 course_description: str,
                 ) -> CourseMetadataModel:
        return self.generate_output(
            course_description=course_description,
        )
