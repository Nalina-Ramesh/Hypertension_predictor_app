from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        input_data = pd.DataFrame([data])
        
        # Predict using model
        prediction = model.predict(input_data)[0]
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

from pyngrok import ngrok
ngrok.connect(5000)
