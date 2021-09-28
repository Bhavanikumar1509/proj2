from flask import Flask,render_template
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
  
  

  
    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)