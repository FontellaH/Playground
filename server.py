# Create a new Flask project

from flask import Flask, render_template

app = Flask(__name__)

# Also known as Stacking route placing one ontop of each other
@app.route('/play')
# Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:nums>')
# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value
@app.route('/play/<int:nums>/<color>')
# Have the /play route render a template with 3 blue boxes
def play(nums=3, color="blue"):
    return render_template("index.html", nums = nums, color = color)




if __name__=="__main__":
    app.run(debug=True)


