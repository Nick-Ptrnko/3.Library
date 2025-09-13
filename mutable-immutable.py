'''
If you send a mutable object to a function and change it there — it will be changed after exiting the function,
unlike an immutable object:
'''
def fruts(param_list: list, param_string: str, param_word: str):
    param_list.append(param_word)
    param_string += param_word
    print(f'''Inside func:
        List: {param_list},
        ID list: {id(param_list)}
        String: {param_string}
        ID string: {id(param_string)}''')
arg_list = ["apple", "banana"]
arg_string = "I love fruts"
arg_word = "orange"
print(f'''Before func:
        List: {arg_list}
        ID list: {id(arg_list)}
        String: {arg_string}
        ID string: {id(arg_string)}''')
fruts(arg_list, arg_string, arg_word)
print(f'''After func:
        List: {arg_list}
        ID list: {id(arg_list)}
        String: {arg_string}
        ID string: {id(arg_string)}''')

