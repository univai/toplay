from flask import Flask
app = Flask("toplay")
import random

choices=['Hilary','Trump','Jill','Gary']

@app.route('/')
def is_nuts():
    return "{} is nuts!".format(random.choice(choices))

@app.route('/<person>')
def is_nuts_person(person):
    return "{} is nuts!".format(person)

if __name__ == '__main__':
    app.run()
