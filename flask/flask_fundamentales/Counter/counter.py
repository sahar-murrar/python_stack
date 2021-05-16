from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def count():
    if 'flag' in session:
        if session['flag'] != 1:
            if 'count_times' and 'actual_times' in session:
                session['count_times'] +=1
                session['actual_times']+=1
            else:
                session['count_times'] = 1
                session['actual_times']= 1 
        elif session['flag'] == 1:
            if 'count_times' in session:
                session['count_times'] +=1
                session['flag']=0 #return the value of he flag to 0 becuase without this line it will remain 1 and the actual visit times will be never changed when refresh the url!
            else:
                session['count_times'] = 1  
                session['flag']=0 #return the value of he flag to 0 becuase without this line it will remain 1 and the actual visit times will be never changed when refresh the url!    
    else:
       session['flag']=0
       if 'count_times' and 'actual_times' in session:
                session['count_times'] +=1
                session['actual_times']+=1
       else:
            session['count_times'] = 1
            session['actual_times']= 1 

    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()		# clears all keys
    if 'count_times' in session:
        session.pop('count_times')		# clears a specific key
        session.pop('actual_times')
    return redirect("/") #redirect to root route

@app.route('/reset_addTwo', methods=['POST'])
def reset_addTwo():
    if request.form["button"]=="Add two Visits!":
        session["count_times"] += 1 #we added here 1 not 2 because when we redirect it to the root route it will add nother 1, so it will be 3 not 2 as we want, that's why we added 1 becuase after redirecting it will be increamented by another 1 and in total we added 2 to the counter.
    elif request.form["button"]=="Reset":
        session["count_times"] = 0 # we put here 0 not 1 as a reset case because when we redirect to the root route it will add 1 directly by itself.

    elif request.form["button"]=="Increament":
        if request.form['increamentBy'] != '': #check if the input text is not none/empty
            session['increamentBy']= int(request.form['increamentBy'])
            session['count_times'] = session['count_times'] + session['increamentBy']-1 # -1 because the redirect will add 1 by default
        else:
            session['count_times']-=1 #if it empty so decrement by 1 because the redirect will increment by 1 and in the end the count will be the same because count-1+1 = count so it will remain the same value and that what we want.

    session['flag']=1
    return redirect("/") #redirect to root route

if __name__ == "__main__":
    app.run(debug=True)
