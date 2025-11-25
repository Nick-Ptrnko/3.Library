from typing import Callable

class UnauthenticatedError(Exception):
    pass


class PermissionDeniedError(Exception):
    pass


def login_required(func: Callable) -> Callable:
    def wrapper(request: dict) -> Callable:
        if "user" in request:
            return func(request)
        else:
            raise UnauthenticatedError("Authentication credentials were not provided!")
    return wrapper

def admin_required(func: Callable) -> Callable:
    def wrapper(request: dict) -> Callable:
        if request["user"]["is_admin"] is False:
            raise PermissionDeniedError("User must be admin!")
        else:
            return func(request)
    return wrapper

@login_required
@admin_required
def access_admin_page(request: dict) -> None:
    print(f"Welcome to the admin page, {request['user']['full_name']}")

request = {"user": {"full_name": "James Bond", "is_admin": True}}
access_admin_page(request)
# Welcome to the admin page, James Bond

request = {"user": {"full_name": "John Smith", "is_admin": False}}
access_admin_page(request)
# PermissionDeniedError: User must be admin!

request = {}
access_admin_page(request)
# UnauthenticatedError: Authentication credentials were not provided!
