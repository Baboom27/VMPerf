from time import sleep
from flask import Flask, render_template, request
import subprocess
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        interface = request.form["interface"]
        period = request.form["period"]
        min_val = request.form["min_val"]
        max_val = request.form["max_val"]
        units = request.form["units"]
        
        while True:
            value = random.randint(int(min_val), int(max_val))
            cmd = "sudo tc qdisc add dev {} root netem {} {}".format(interface, value, units)
            subprocess.run(cmd, shell=True)
            sleep(int(period))
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
