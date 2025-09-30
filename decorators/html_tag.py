from typing import Callable
def html_tag(tag: str) -> Callable:
    def inner(func: Callable) -> Callable:
        def wrapper(name: str) -> None:
            return f"<{tag}>{func(name)}</{tag}>"
        return wrapper
    return inner

@html_tag('p')
@html_tag('a')
def greeter(name: str) -> str:
    return f"Hello, {name}!"

print(greeter("Микола"))

