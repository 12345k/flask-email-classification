from flask import Flask, render_template ,request
from flask import jsonify
# from flask_wtf import FlaskForm

# from sklearn.externals import joblib

app = Flask(__name__)
 
# @app.route("/")
# @app.route("/index")
# def index():
#    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
	if str(request.method)==str('POST'):
		content = request.get_json(silent=True)
		print(content)

		email_text = content['email_text']
		subject_text = content['subject_text']

		full_text= subject_text + email_text
        
		if full_text.count("kyc") > full_text.count("shiptrack"):
			text="datalabs_kyc@optisolbusiness.com"
		else:
			text="datalabs_shiptrack@optisolbusiness.com"

		
		return jsonify(text)
	
if __name__ == "__main__":
    app.run(debug=True)