class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def god() -> list:
    # write your code here
    adam = Man()
    yea = Woman()
    return [adam, yea]

god()