from flask import Flask, render_template,request
from utils import data

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/description')
def description():
    name = request.args.get('name')
    print(name)
    
    url='https://github.com/AmimiHamza/'+name
    description=data[name][0]
    image=name+data[name][1]
    print(image)
    return render_template('description.html',image=image ,url=url,description=description)
if __name__ == '__main__':
    app.run(debug=True)
