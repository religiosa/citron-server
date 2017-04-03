from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def serve():
	if request.method == 'POST':
		msg_len = request.content_length
		print msg_len
		return 'POSTed ' + str(msg_len) + '\n'
	else:
		return 'GET.'

if __name__ == "__main__":
    app.run()
