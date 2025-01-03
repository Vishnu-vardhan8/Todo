
    
from flask import Flask,render_template,url_for


app=Flask(__name__)


@app.route('/home')
def HomePage():
    return render_template('main/home.html')

@app.route('/signup')
def SignUpPage():
    return render_template('auth/signup.html')

@app.route('/login')
def LoginPage():
    return render_template('auth/login.html')


@app.route('/complete')
def CompletePage():
    return render_template('main/complete.html')

@app.route('/present')
def PresentPage():
    return render_template('main/present.html')



if __name__=='__main__':
    app.run(debug=True)
