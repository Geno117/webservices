import os
from flask import Flask, request, render_template, Response
import responses
app = Flask(__name__)


@app.route('/', methods=['GET'])
def launch_html():
    cwd = os.getcwd()
    print(cwd)
    return render_template('index.html')


@app.route('/model', methods=['POST'])
def launch_config_api():
    print('API {api} called'.format(api='/method'))

    return Response('OKlah!', status=200)


if __name__ == '__main__':
    app.run()
