from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load only XGBoost model
xgb_model = joblib.load('models/xgb_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    final_close = None

    if request.method == 'POST':
        try:
            user_input = [float(x) for x in request.form['features'].split(',')]

            if len(user_input) != 5:
                return render_template('index.html', prediction="Please enter exactly 5 values.")

            # Pad input to reach 1282 features
            filler = np.zeros(1277)
            final_input = np.array(user_input + filler.tolist()).reshape(1, -1)

            if final_input.shape[1] != 1282:
                raise ValueError(f"Expected 1282 features, got {final_input.shape[1]}")

            # Predict using XGBoost
            xgb_pred = xgb_model.predict(final_input)[0]

            # Multiply with 5th user input (index 4) and add 1
            adjusted_close = (xgb_pred * user_input[4]) + 1

            prediction = f"📈 XGBoost Prediction: {round(xgb_pred, 4)}"
            final_close = f"💰 Final Close : {round(adjusted_close, 2)}"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction, final_close=final_close)

if __name__ == '__main__':
    app.run(debug=True)
