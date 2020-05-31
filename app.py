from flask import Flask , render_template,request
app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(host= '0.0.0.0',port=5001,threaded = True)
    