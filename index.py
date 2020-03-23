import flask
from time import sleep
app = flask.Flask(__name__)

@app.route('/<path:u_path>', methods=['GET', 'POST', 'PUT'])
def index(u_path):
	sleep(100000000)
	status_code = flask.Response(status=201)
	return status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8089)