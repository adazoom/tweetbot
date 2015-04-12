from flask import *
from models import * 

connection = "mysql://aristotle:happy@45.33.90.42:3306/aristotle" 

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = connection 
db.init_app(app) 

with app.app_context(): 
	db.create_all()
	db.session.commit() 

@app.route('/')
def home(): 
	return render_template('index.html')

@app.route('/insert_data', methods=['POST'])
def insert(request):
	res = request.json 

	new_tweet = Tweets(res['tweetid'],
		res['tweettext'])

	db.session.add(new_tweet)
	db.session.commit()

	return jsonify(res)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

