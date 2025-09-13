'''
`*args` and `**kwargs` allow you to pass multiple ==arguments== or ==keyword arguments== to a function.
Here `*args` will be saved as a tuple of values. All non-keyword arguments will be packed in this parameter.
'''
def function(*args, **kwargs):
    print(kwargs)
    print(args)
function(1, 2, [3, 4], "summer", name="Mariia", favorite_number=7)
