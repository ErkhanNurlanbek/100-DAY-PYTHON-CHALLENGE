from flask import Flask

app = Flask(__name__)




@app.route("/")
def hello_world():
    return "Hello, World!"

# @app.route('/lys.website')
# def massage():
#     return 'love yourself'

if __name__ == '__main__':
    app.run()

# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#         function()
#     return wrapper_function
#
#
#
# def ez():
#     print('ez')
#
# def hello2():
#     print('Hello')
#
#
# @delay_decorator
# def hello(): # TODO <===== this is the same
#     print('hello')
# hello()
#
# delayed_function = delay_decorator(hello2) # TODO <====== as this
# delayed_function()