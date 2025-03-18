from flask import Flask
import random
app = Flask(__name__)

random_num = random.randint(0, 9)
print(random_num)

# def decorator_bold(fun):
#     def wrapped_fun():
#         return f"<b>{fun()}</b>"
#     return wrapped_fun
#
#
# def decorator_u(fun):
#     def wrapped_fun():
#         return f"<u>{fun()}</u>"
#     return wrapped_fun
#
#
# def decorator_em(fun):
#     def wrapped_fun():
#         return f"<em>{fun()}</em>"
#     return wrapped_fun


@app.route('/')
# @decorator_bold
# @decorator_em
# @decorator_u
def hello_world():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp">')


@app.route('/<int:input>')
def low_high_game(input):
    if input < random_num:
        return ('<h1>Guess higher!</h1>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczRhOTVndDg0OW56c3dlanp1c3p5dDk3YzRzenBjZGxhandoaDAxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AwttwIryJLZodu6UyS/giphy.gif" >')
    elif input > random_num:
        return ('<h1>Guess lower!</h1>'
                '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExa291NG9xZ3g1cDV6N29iaDVkNmZuNjFiemp1YzB5ZDJ3eTAxZ2FpNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cWjFnDTq2N87YBn0uN/giphy.gif">')
    else:
        return ('<h1>You are correct!</h1>'
                '<img src="https://media1.tenor.com/m/VKZCJNVQ_EcAAAAC/maverick-topgun.gif">')


if __name__ == '__main__':
    app.run(debug=True)
