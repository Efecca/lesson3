from flask import Flask, json, render_template, request
import requests

import locale

import settings

app=Flask(__name__)

locale.setlocale(locale.LC_ALL, "russian")
json_data = {}

@app.route("/")
def index():
    json_data = get_names_data()
    return json_data

@app.route("/names")
def names():
    year = request.args.get('year', type = int)
    print(year)
    json_data = get_names_data(year)
    return render_template('table.html', data=json_data)

def get_names_data(year=None):
    info = {'api_key': settings.API_KEY}
    if (year):
        info["$filter"] = "Cells/Year eq {}".format(str(year))
#2009
    response = requests.get(settings.FEMALE_SET, params=info)
    return response.json()


if __name__ == '__main__':
    app.run()