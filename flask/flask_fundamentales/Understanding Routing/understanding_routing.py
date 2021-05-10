from flask import Flask, render_template
app=Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello World'


# @app.route('/dojo')
# def dojo():
#     return 'Dojo!'

# @app.route('/say/<var>')
# def variable(var):
#     return f'Hi {var}!'   


     
@app.route('/repeat/<times>/<name>')
def repeat(times,name):
    return render_template('index.html', num_times=int(times), user_name=name)

@app.errorhandler(404)
def errorMessage(e):
    return "Sorry! No response. Try again."

   
if __name__=="__main__":
    app.run(debug=True)    