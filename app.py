#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200

@app.route('/all', methods=['GET'])
def get_all():
    return ({
        '_remote': request.environ['REMOTE_ADDR'],
        'address': request.environ['HTTP_X_FORWARDED_FOR']
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
