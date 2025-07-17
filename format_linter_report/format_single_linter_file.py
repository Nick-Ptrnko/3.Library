from .format_linter_error import format_linter_error
errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
         "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, ' 
        "store and decorate numbers: {', '.join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
]

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors":[format_linter_error(error) for error in errors],
    "path": file_path,
    "status": ("passed" if "errors" == [] else "failed")}

print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))
