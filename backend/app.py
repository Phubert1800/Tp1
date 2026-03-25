from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend funcionando"

if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))
