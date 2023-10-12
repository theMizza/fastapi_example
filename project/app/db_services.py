from app.models import Questions
from app.schemas import QuestionSchema


class CreateQuestionException(Exception):
    ...


def create_question(data: QuestionSchema, database):
    """Add question to database"""
    question = Questions(question=data.question, answer=data.answer)

    try:
        database.add(question)
        database.commit()
        database.refresh(question)

    except Exception as error:
        database.rollback()
        raise CreateQuestionException(error)

    return question


def get_last_question(database):
    """Get last question from database"""
    return database.query(Questions).order_by(Questions.id.desc()).first()


def get_question(question_id: int, database):
    """Get question by id"""
    return database.query(Questions).filter(Questions.id == question_id).first()


