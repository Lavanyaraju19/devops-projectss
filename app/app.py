from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Hello from DevOps Project!"

if __name__ == "__main__":
    print("✅ Starting Flask app...")
    app.run(host="0.0.0.0", port=5000, debug=True)

