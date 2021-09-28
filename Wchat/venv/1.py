from flask import Flask, request, render_template 

app =Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',moto="be secure")
    
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/login')
def login():
    return render_template('login.html') 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with  email in HTML form
       email = request.form.get("email")
       # getting input with password in HTML form 
       password = request.form.get("password") 
       return "email is "+email + "password"+password
    return render_template("signup.html") 
  

  
    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)
    
