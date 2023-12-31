from app import schemas, db_services, outer_services
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter

router = APIRouter()


async def get_another_and_create(database):
    while True:
        try:
            another_questions = await outer_services.jservice_request(1)
            db_services.create_question(
                schemas.QuestionSchema(question=another_questions[0]["question"],
                                       answer=another_questions[0]["answer"]),
                database
            )
            break
        except:
            pass

@router.post('/')
async def add_questions(data: schemas.RequestDataSchema = None, database: Session = Depends(get_db)):
    data_to_return = db_services.get_last_question(database)
    if not data_to_return:
        returned_question = {}
    else:
        returned_question = schemas.QuestionSchema(
            id=data_to_return.id,
            question=data_to_return.question,
            answer=data_to_return.answer,
            created_at=data_to_return.created_at
        )
    questions = await outer_services.jservice_request(data.questions_num)
    for question in questions:
        try:
            create_data = schemas.QuestionSchema(question=question["question"], answer=question["answer"])
            db_services.create_question(create_data, database)
        except:
            await get_another_and_create(database)
    return returned_question



@router.get('/')
async def get_question(question_id: int = None, database: Session = Depends(get_db)):
    data = db_services.get_question(question_id, database)
    if data:
        return data
    else:
        return {}
