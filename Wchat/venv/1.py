from flask import Flask,render_template
app =Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',moto='lets chat free')
    
@app.route('/about')
def about():
    return "<h1> Hello world about page</h1>"

@app.route('/chatroom')
def chatroom():
    return "<h1>welcome to my chatroom</h1>"
    
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)