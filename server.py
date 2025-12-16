from flask import Flask, render_template

app = Flask(__name__)

@app.route ('/')
def index():
  title = 'Home Pade'
  return render_template('index.html' , title = title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Punyapat Tonpho'
  email = 'std.67122420219@ubru.ac.th'
  mobile = '0633604712'
  age = 19
  return render_template('about.html' ,  title=title,
                      name=name,
                      email=email,
                      mobile=mobile,
                      age=age)
@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Food Page'
  foods = ['กะเพราหมูกรอบ','ไข่เจียว','ก๋ยวเตี๋ยวเรือ']
  return render_template('favorite_foods.html' ,
                        title=title,
                        foods=foods)

@app.route('/favorite/sports')
def favorite_sports():
  title = 'Favorite Sports Page'
  sports = ['ฟุตบอล','วอลเล่บอล','บาสเกตบอล']
  return render_template('favorite_sports.html',
                        title=title,
                        sports=sports)



