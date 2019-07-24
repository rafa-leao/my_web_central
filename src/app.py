from flask import Flask, render_template

from utils.trending_news import news
from utils.hours_later import hours_later
from utils.buses_arrivals import buses_arrivals
from utils.temperature_now import temperature_now
from utils.temperatures_to_one_hour_later import temperatures_to_one_hour_later

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html',
                           temperature_now=temperature_now(),
                           bus_arrival=buses_arrivals(),
                           one_hour_later=hours_later(),
                           temperature_to_one_hour_later=temperatures_to_one_hour_later(),
                           news=news())


if __name__ == "__main__":
    app.run(debug=True)