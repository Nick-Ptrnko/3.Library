import pytest

from main import sum_instances

def test_cannot_add_int_and_str() -> None:
    with pytest.raises(TypeError):
        sum_instances(2, "3")


def test_cannot_add_2_lists() -> None:
    with pytest.raises(TypeError):
        # but it will not rise TypeError, because actually we can use ‘+’ with lists
        sum_instances([2], ["3"])  