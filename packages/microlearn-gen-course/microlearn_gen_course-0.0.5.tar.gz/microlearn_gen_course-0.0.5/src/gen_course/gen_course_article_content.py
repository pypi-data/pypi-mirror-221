"""
Generator for course's article's content.
"""
import logging
from typing import List
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from .gen_base import GenBase


logger = logging.getLogger(__name__)


class CourseArticleModel(BaseModel):
    content: str = Field(description="Article content")
    questions: List[str] = Field(
        description="List of questions related to the article")

    def get_article_content(self) -> str:
        return f"""{self.content}

Questions the reader may be interested in making after reading the article:
1. {self.questions[0]}
2. {self.questions[1]}
3. {self.questions[2]}"""


class GenCourseArticleContent(GenBase):
    """
    Generator class for course's article's content'.
    """
    HUMAN_PROMPT = """I'm developing a micro learning course about the following:
---
Title: {course_title}
Description: {course_description}
---
Write a short article of maximum {content_length_words} for this title: "{article_title}". Do not repeat the title in the article content. Write 3 questions about the article that the reader might be interested in asking after reading the article."""

    def __init__(self, llm, verbose: bool = False):
        super().__init__(llm, verbose)

    def get_output_parser(self):
        return PydanticOutputParser(pydantic_object=CourseArticleModel)

    def generate(self,
                 course_title: str,
                 course_description: str,
                 article_title: str,
                 content_length_words: int = 150,
                 ) -> CourseArticleModel:
        return self.generate_output(
            course_title=course_title,
            course_description=course_description,
            article_title=article_title,
            content_length_words=content_length_words,
        )


class GenCourseArticleContentUsingPreviousArticles(GenBase):
    """
    Generator class for course's article's content'.
    """
    HUMAN_PROMPT = """I'm developing a micro learning course about the following:
---
Title: {course_title}
Description: {course_description}
---
Following are the previous articles generated in the course delimited by 2 newlines:
---
{previous_articles}
---
Write a short article of maximum {content_length_words} for this title: "{article_title}". Do not repeat the title in the article content. Do not include previous articles content in the article content. Write 3 questions about the article that the reader might be interested in asking after reading the article."""

    def __init__(self, llm, verbose: bool = False):
        super().__init__(llm, verbose)

    def get_output_parser(self):
        return PydanticOutputParser(pydantic_object=CourseArticleModel)

    def generate(self,
                 course_title: str,
                 course_description: str,
                 article_title: str,
                 previous_articles: List[str],
                 content_length_words: int = 150,
                 ) -> CourseArticleModel:
        if len(previous_articles) == 0:
            previous_articles_str = "None"
        else:
            previous_articles_str = "\n\n".join(previous_articles)
        logger.debug(f"previous_articles_str: {previous_articles_str}")

        return self.generate_output(
            course_title=course_title,
            course_description=course_description,
            article_title=article_title,
            previous_articles=previous_articles_str,
            content_length_words=content_length_words,
        )
