from flask import Flask, render_template

app = Flask(__name__)


@app.route('/play')
@app.route('/play/<int:nums>')
@app.route('/play/<int:nums>/<color>')
def play(nums=3, color="blue"):
    return render_template("index.html", nums = nums, color = color)




if __name__=="__main__":
    app.run(debug=True)


