from flask import Flask
app = Flask(__name__)


# For testing introspect endpoint in oauth flow
@app.route('/', methods=['GET', 'POST'])
def hello():
    return '{"active": true }'

@app.route('/true', methods=['GET', 'POST'])
def returnTrue():
    return '{"active": true, "scope": "openid"}'

@app.route('/false', methods=['GET', 'POST'])
def returnFalse():
    return '{"active": false}'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

