from flask import Flask, render_template
app=Flask(__name__)
@app.route('/play')
def play():
    return render_template('index.html',num_times=None)

@app.route('/play/<num>')
def play_times(num):
    return render_template('index.html', num_times=int(num))


@app.route('/play/<num>/<color>')
def play_times_color(num,color):
    return render_template('index.html', num_times=int(num), given_color=color)   
if __name__=="__main__":
    app.run(debug=True)   