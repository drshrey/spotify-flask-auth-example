import json
from flask import Flask, request, redirect, g, render_template
import requests
import base64

app = Flask(__name__)

#Authorization code flow
url = "https://accounts.spotify.com/authorize"
CLIENT_ID = ""
REDIRECT_URI = "http://127.0.0.1:8080/callback/q"
SCOPE = "user-modify-private user-modify-public"
CLIENT_SECRET = ""

payload = {"client_id":CLIENT_ID, "response_type":"code","redirect_uri":REDIRECT_URI,"scope":SCOPE}

@app.route('/')
def index():
	return redirect("https://accounts.spotify.com/authorize/?client_id=&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fcallback%2Fq&scope=playlist-modify-public+playlist-modify-private")

@app.route("/callback/q")
def callback():
	access_token = request.args
	code_payload = {"grant_type":"authorization_code","code":str(access_token['code']),"redirect_uri":REDIRECT_URI}
	base64encoded = base64.b64encode(CLIENT_ID + ":" + CLIENT_SECRET)
	headers = {"Authorization":"Basic %s" % base64encoded}
	post_request = requests.post("https://accounts.spotify.com/api/token",data=code_payload,headers=headers)
	json_response = json.loads(post_request.text)
	test_response = requests.get("https://api.spotify.com/v1/me", headers={'Authorization':'Bearer ' + json_response[u'access_token']})
	json_profile = json.loads(test_response.text)
	playlists = requests.get(json_profile['href']+"/playlists", headers={'Authorization':'Bearer '+json_response[u'access_token']})
	jsoned_playlists = json.loads(playlists.text)
	json_array = []
	for playlist in jsoned_playlists['items']:
		json_array.append(playlist)
	return render_template("index.html",sorted_array=json_array)


if __name__ == "__main__":
	app.run(debug=True,port=8080)
