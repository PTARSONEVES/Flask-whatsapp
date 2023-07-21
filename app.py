import json
from flask import Flask, render_template
import flask
from message_helper import get_text_message_input, send_message

app = Flask ( __name__ )

with open('config.json') as f:
	config=json.load(f)
	print(config)

@app.route ("/")
def index():
	return render_template('index.html', name=__name__)

@app.route('/welcome', methods=['POST'])
async def welcome():
#	print(app.config['RECIPIENT_WAID'])
	data = get_text_message_input('+5581991581431','Bem-vindo ao aplicativo de demonstração de confirmação de voo para Python!')
	await send_message(data)
	return flask.redirect(flask.url_for('index'))