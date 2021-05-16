from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
    name=request.form['name']
    gender=request.form['gender']
    courses=request.form.getlist('courses') #we used gelist function for checkbox because we may have more than one value for the checkbox so we need to put them in a list. also we set the name attribute in the html file to courses for all checkbox to refer them in the getlist function.
    location=request.form['location']
    language=request.form['language']
    comment=request.form['comment']


    return render_template('index1.html', name=name, gender=gender, courses=courses, location=location, language=language, comment=comment )

if __name__ == "__main__":
    app.run(debug=True)
