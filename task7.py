from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/news/')
def news():

    context = [
        {'name': 'Наука и техника' },
        {'description':
             'В этой статье кратко рассмотрим свойства черных дыр, '
             'возникающие вследствие их колоссального гравитационного притяжения, '
             'и то как интересно эти свойства «можно» было бы использовать при решении некоторых бытовых вопросов.. '
         },
        {'date': '11-12-2023',
         }
    ]
    return render_template('news.html', news=context)



if __name__ == '__main__':
    app.run()
