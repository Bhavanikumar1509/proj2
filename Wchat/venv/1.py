from flask import Flask, request, render_template 
from replit import db

app =Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)
    
