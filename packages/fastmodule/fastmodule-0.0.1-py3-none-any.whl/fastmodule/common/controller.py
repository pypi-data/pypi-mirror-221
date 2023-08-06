from fastapi import APIRouter
from typing import Any, Dict, List, Type
import inspect


class Controller:

    def __init__(self, *args, **kargs):
        self.args = args
        self.kargs = kargs
        

    def __call__(self, controller: Type[Any]) -> Type[Any]:
        members =  [o for m, o in inspect.getmembers(controller) if not m.startswith('__')]
        router: APIRouter = APIRouter()
        router.prefix = f'/{self.args[0]}'
        router.tags = [f'{self.args[0]}'.capitalize()]

        for m in members:
            router.add_api_route(methods=[m.method], path=m.path, endpoint=m)

        setattr(controller, 'router',  router)
        return controller

