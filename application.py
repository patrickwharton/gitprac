from flask import Flask

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello_world.html")

if __name__=="__main__":
        app.run(debug=True)
