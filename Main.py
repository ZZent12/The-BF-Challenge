from flask import Flask, render_template, redirect, url_for, request


def Main():
    app = Flask(__name__)
    app.secret_key = "HAigsggirp"

    @app.route("/")
    def index():
        return redirect(url_for("backstory"))
    
    @app.route("/backstory")
    def backstory():
        return render_template("backstory.html", nav_back="/", nav_next="/principles")
    
    @app.route("/compVinter")
    def compVinter():
        return render_template("compVinter.html", back_to="/backstory")
    
    @app.route("/principles")
    def principles():
        return render_template("principles.html", nav_back="/backstory", nav_next="defining")

    @app.route("/loops")
    def loops():
        return render_template("loops.html", back_to="/principles")
    
    @app.route("/defining")
    def defining():
        return render_template("defining.html", nav_back="/principles", nav_next="/")

    app.run(debug=True)


if __name__ == "__main__":
    Main()