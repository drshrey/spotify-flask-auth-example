Authorization Code Flow Walkthrough
=======

How to do an authorization code flow, through Flask and Python.

##Step 1
Fill in your credentials in main.py. This includes the CLIENT_ID and CLIENT_SECRET, which is left blank. You can obtain this by going to [Spotify Developers](https://developer.spotify.com/my-applications/#!/).


##Step 2
Be sure that your redirect uri, inside your application page in the Spotify Developers website is "http://127.0.0.1:8080/callback/q".


##Step 3
To see that it works, simply run the application by running '''python main.py''', and point your browser to http://127.0.0.1:8080.

