# Import the libraies
import numpy as np
from flask import Flask, request, render_template
#from sklearn.externals import joblib
import joblib

# Create the Flask app and load the trained model
app = Flask(__name__)
model = joblib.load('model_svm.pkl')

# Define the '/' root route to display the content from index.html
@app.route('/')
def home():
    return render_template('index.html')

# Define the '/predict' route to:
# - Get form data and convert them to float values
# - Convert form data to numpy array
# - Pass form data to model for prediction

@app.route('/predict',methods=['POST'])
def predict():

    form_data = [float(x) for x in request.form.values()]
    features = [np.array(form_data)]
    prediction = model.predict(features)

	# Format prediction text for display in "index.html"
    return render_template('index.html', iris_prediction='Iris species should be {}'.format(prediction[0]))

# Define the '/' root route to display the content from index.html
@app.route('/')
def home2():
    return render_template('index.html')

#Run the flask application (if this module is the entry point to the program)
if __name__ == "__main__":
    app.run(debug=False)
