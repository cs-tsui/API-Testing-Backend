from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

def printRequesterIP():
    request_addr = request.remote_addr
    HTTP_X_REAL_IP_header = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    print("request_addr:", request.remote_addr)
    print("HTTP_X_REAL_IP_HEADER:", HTTP_X_REAL_IP_header)
    
# For testing introspect endpoint in oauth flow
@app.route('/', methods=['GET', 'POST'])
def hello():
    printRequesterIP()
    return '{"active": true }'

@app.route('/true', methods=['GET', 'POST'])
def returnTrue():
    printRequesterIP()
    return '{"active": true, "scope": "openid"}'

@app.route('/false', methods=['GET', 'POST'])
def returnFalse():
    printRequesterIP()
    return '{"active": false}'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

