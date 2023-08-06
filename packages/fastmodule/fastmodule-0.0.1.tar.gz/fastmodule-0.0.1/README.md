# FastModule
Mini tool to create FastAPI applications with a basic project structure inspired by Nest.js

## Installation
### Create a virtual enviroment (Optional)
```bash
python -m venv venv
source venv/bin/activate # venv/Scripts/activate on Windows
```
### Install package (require python ^3.10 version)
```bash
pip install fastmodule
```
## Example
Create a controller file and add the following code:
```python
from fastmodule.common import Controller, Get, Post
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

@Controller('users')
class UserController:

    @Get('/')
    def find_all(self) -> str:
        return 'This action returns all users'
    
    @Get('/{id}')
    def find_one(self, id: int) -> str:
        return f'This action returns one user with id {id}'

    @Post('/')
    def create(self, user: User) -> str:
        return f'This action create a user with data {user}'

```

## Add the controller in the main file

Add in the main file:
```bash
from fastmodule import FastModule
from src.user_controller import UserController

app = FastModule()

app.include_router(UserController().router)
```


Run the application:
```bash
uvicorn main:app --port 8000
```

Open docs in the browser at localhost:8000/docs:

![plot](./media/doc.png)

