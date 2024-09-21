from fastapi.responses import FileResponse
from fastapi import APIRouter
from app.models.models import *

router = APIRouter()

@router.get("/v1")
async def root():
    return {"message": "Hello World"}


@router.get("/v1/index.html")
async def index():
    return FileResponse('./app/index.html')

@router.get('/v1/calculate/{item_id}')
async def calculate(item_id: str):
    a, b = map(int, item_id.split('+'))
    return {'result': a + b}

@router.get("/v1/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@router.post("/v1/app1")
async def root(user: User):
    '''тут мы можем с переменной user, которая в себе содержит объект класса User с соответствующими полями (и указанными типами), делать любую логику
    - например, мы можем сохранить информацию в базу данных
    - или передать их в другую функцию
    - или другое'''
    print(f'Мы получили от юзера {user.username} такое сообщение: {user.message}') # тут мы просто выведем полученные данные на экран в отформатированном варианте
    return user # или можем вернуть обратно полученные данные, как символ того, что данные получили, или другая логика на ваш вкус

@router.get('/v1/users')
async def get_user():
    params = {'username':'serega', 'message':'chernovar', 'id':'123',}
    user: User = User(**params)
    return user

@router.post('/v1/user_is_adult')
async def is_audlt(user: User1):
    class ExtendedUser(User1):
        is_audlt: bool = True

    tmp_user = ExtendedUser(is_audlt=False if user.age < 18 else True, **user.model_dump(mode='json'))

    return tmp_user

feedback_db:list[Feedback] = [Feedback(username='kek', fb_message='wmek'),
                              Feedback(username='chpok', fb_message='aaaaa')]

@router.get('/v1/feedback/show/{number}')
async def show_feedback(number:int, show_name:bool=True):
    fb = {}
    for idx, letter in enumerate(feedback_db):
        if idx >= number:
            break
        fb[idx] = letter if show_name else {'fb_message':letter.fb_message}
    return fb

@router.post('/v1/feedback/write')
async def feedback(letter:Feedback):
    feedback_db.append(letter)
    return {'message': f'Feedback received. Thank you, {letter.username}!'}

