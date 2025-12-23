def sum_instances(a: int | str, b: int | str) -> int | str:
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    return a + b

if __name__ == "__main__":
    print(sum_instances(2, 3))
    print(sum_instances([2], ["3"]))