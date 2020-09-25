import flask
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
 artists=["Honey Singh","Sunidhi chauhan","Atif Aslam","Arjit Singh", "Shreya Ghosal"]
 images=["static/HS.jpg","static/SC.jpg","static/Atif.jpg","static/AS.jpg","static/SG.jpg"]
 return flask.render_template(
  "index.html",
  len = len(artists),
  artists=artists,
  images=images
  )

app.run(
 port=int(os.getenv('PORT', 8080)),
 host=os.getenv('IP', '0.0.0.0')
)
