from pydantic import BaseModel


class QuestionSchema(BaseModel):
    """Annotation of Qiestions model"""
    question: str
    answer: str


class RequestDataSchema(BaseModel):
    """Annotation of request data"""
    questions_num: int
