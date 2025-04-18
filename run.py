from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Import audio only if not on Render
if not os.environ.get("RENDER"):
    import audio

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
