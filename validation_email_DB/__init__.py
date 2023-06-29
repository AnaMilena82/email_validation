from flask import Flask


app = Flask(__name__)

app.secret_key = "shhhhhh"

BASE_DE_DATOS = "email"