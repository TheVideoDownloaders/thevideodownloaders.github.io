import youtube_dl
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download', methods=["POST", "GET"])
def download():
    
	url = request.form["url"]
	print("Someone just tried to download", url)
	with youtube_dl.YoutubeDL() as ydl:
		url = ydl.extract_info(url, download=False)
		print(url)
		try:
			download_link = url["entries"][-1]["formats"][-1]["url"]
		except:
			download_link = url["formats"][-1]["url"]
		return redirect(download_link+"&dl=1")

if __name__ == '__main__':
	app.run(port=80, debug=True)
