from flask import Flask

app = Flask(__name__)

WIN = "https://giphy.com/gifs/you-won-we-have-a-winner-prize-YpFnbM8Vjx7qaxL39a"


def solution(function):
    def wrapper(number):
        function(number)
        if number < 5:
            return low()
        elif number > 5:
            return high()

        else:
            return won()

    return wrapper


@solution
@app.route("/")
def guess():
    return "<h1 style='text-align: center'> GUESS A NUMBER BETWEEN 0 & 9</h1>" \
           "<p><b>Good Luck!!!</b></p>" \
           "<img src ='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=400>"


@app.route("/low")
def low():
    return "<h1 style='text-align: center'> GUESS A NUMBER BETWEEN 0 & 9</h1>" \
           "<p><b>Too Low!!!</b></p>" \
           "<img src ='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjU3YTJkYzg1ZmJkMzZlMWJkZGIxZTkyNjI5NWZmNzMxZDQzOWM4YyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/TgmiJ4AZ3HSiIqpOj6/giphy.gif' width=400>"


@app.route("/high")
def high():
    return "<h1 style='text-align: center'> GUESS A NUMBER BETWEEN 0 & 9</h1>" \
           "<p><b>Too High!!!</b></p>" \
           "<img src ='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTFmYTJhYTYyNTQxMjg1OWU5MzQ0OGJiNDY5ZDI1NmI3YjgzYjM5NCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/21JMq0e5LSUJq/giphy.gif' width=400>"


@app.route("/won")
def won():
    return "<h1 style='text-align: center'> GUESS A NUMBER BETWEEN 0 & 9</h1>" \
           "<p><b>CONGRATULATIONS, YOU WON!!!</b></p>" \
           "<img src ='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzgwNjQ5NWYxN2NkZThiMzE5NTQ0NjYwOTkzYjBmNjE1NmM3ZTMxMiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/YpFnbM8Vjx7qaxL39a/giphy.gif' width=400>"


@app.route("/username/<int:number>")
@solution
def n(number):
    return number


n(1)

if __name__ == "__main__":
    app.run(debug=True)
