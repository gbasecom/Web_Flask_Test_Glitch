from flask import Flask, url_for, render_template
import json
import os

app = Flask(__name__)

    

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/oddeven')
def odd_even():
    return render_template('oddeven.html', number=2)

@app.route('/news')
def news():
    #with open("news.json", "rt", encoding="utf8") as f:
        #news_list = json.loads(f.read())
    news_list = {
    "news": [
        {
            "title": "Сегодня хорошая погода",
            "content": "Невероятно, сегодня хорошая погода"
        },
        {
            "title": "Завтра хорошая погода",
            "content": "С ума сойти, и завтра хорошая погода"
        },
        {
            "title": "Послезавтра дождь",
            "content": "Все вошло в норму"
        }
            ]
        } 
    print(news_list)
    return render_template('news.html', news=news_list)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
