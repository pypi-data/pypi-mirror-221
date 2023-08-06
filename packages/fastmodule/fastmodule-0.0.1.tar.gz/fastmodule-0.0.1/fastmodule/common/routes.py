from fastapi import APIRouter
from typing import Type, Any, Dict, List
from functools import wraps
import inspect
import types


class Routes():
    
    def get(self, path, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        def decorator(function: Type[Any]) -> Type[Any]:
            setattr(function, 'path', path)
            setattr(function, 'method', 'GET')
            @wraps(function)
            def wrapper(self, *args, **kwds):
                return function(self, *args, **kwds)

            return wrapper

        return decorator
    
    def post(self, path, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        def decorator(function: Type[Any]) -> Type[Any]:
            setattr(function, 'path', path)
            setattr(function, 'method', 'POST')
            @wraps(function)
            def wrapper(self, *args, **kwds):
                return function(self, *args, **kwds)

            return wrapper

        return decorator