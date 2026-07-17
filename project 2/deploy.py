from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load model + vectorizer
with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()   # ✅ read JSON body
    input_text = data['text']
    vectorized = tfidf.transform([input_text])
    prediction = model.predict(vectorized)[0]
    label = "Fake" if prediction == 1 else "Real"
    return jsonify({"label": label})

if __name__ == "__main__":
    app.run(debug=True)
