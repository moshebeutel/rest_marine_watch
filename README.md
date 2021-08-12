# rest_marine_watch
This repo is intended to define a REST API for marine watch 

The repo contains the app.py script which is a dummy server that gets an image file and returns a json annotation format.

The request.py is a pythonic POST request for that server.

##Required installations##
`pip install Flask==2.0.1`

##Running the server##
Open a command prompt.
2. Navigate to this repo directory 
3. Type `flask run`
4. Run request.py - You should get a response with json annotations
