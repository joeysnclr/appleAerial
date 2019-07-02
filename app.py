from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify
import json
import webview
import sys
import threading
import time

app = Flask(__name__)

developmentMode = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/play')
def play():
	return render_template('play.html')	



def start_server(debug=False):
    app.run(debug=debug)
 
if __name__ == '__main__': 
	if developmentMode:
		#start server
		start_server(debug=True)
	else:
		# start the server and create a window for the video
		t = threading.Thread(target=start_server)
		t.daemon = True
		t.start()

		time.sleep(0.5)
		webview.create_window("Apple Aerial", "http://127.0.0.1:5000", debug=True)
		webview.load_url("http://127.0.0.1:5000")

		sys.exit()