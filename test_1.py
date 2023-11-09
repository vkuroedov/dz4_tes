from fastapi import FastAPI
from fastapi import param_functions
from fastapi.responses import PlainTextResponse, FileResponse, HTMLResponse

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello, world!'}

# типизация в fastapi является принудительной!
# query params
@app.get('/add')
def add(x: int, y: int) -> int:
    return x + y

# передача параметра через ручку (path params)
@app.get('/double/{number}')
def double(number: int) -> int:
    return number * 2 

# требования к длине
@app.get('/welcome/{name}')
def welcome(name: str = param_functions.Path(min_length=2, max_length=20)) -> str:
    return f'Good luck, {name}!'

# с использование регулярных выражений
@app.get('/phone/{number}')
def phone_number(number: str = param_functions.Path(regex=r'\d+')):
    return {'phone': number}

# как можно возвращать ответ (в явном виде)
@app.get('/plaintext')
def get_text():
    content = 'Tralala'
    return PlainTextResponse(content=content)

# как можно возвращать ответ (в явном виде)
@app.get('/html')
def get_html():
    content = '<h1>Привет</h1>'
    return HTMLResponse(content=content)

# как можно возвращать ответ (в явном виде)
@app.get('/file')
def get_file():
    content = '<h1>Привет<\h1>'
    return FileResponse(content)