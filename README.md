# Recommended Repo Name: HNG-Backend-NumberClassifier


---

HNG Backend Number Classifier API

Welcome to the HNG Backend Number Classifier API, a simple yet powerful API that classifies numbers based on different mathematical properties. This API is built using Flask and is designed to be deployed on Render for easy accessibility.


---

🚀 Features

This API provides the following number classifications:
✅ Prime Number Check – Determines if a number is prime.
✅ Perfect Number Check – Checks if a number is perfect (sum of its proper divisors equals the number).
✅ Armstrong Number Check – Identifies Armstrong numbers.
✅ Even or Odd Classification – Distinguishes between even and odd numbers.
✅ Digit Sum Calculation – Computes the sum of the digits in a number.
✅ Fun Facts from Numbers API – Fetches interesting facts about numbers.


---

📂 Project Structure

📦 HNG-Backend-NumberClassifier
 ┣ 📜 app.py            # Main Flask application
 ┣ 📜 requirements.txt   # Dependencies for the project
 ┣ 📜 Procfile           # Configuration for Render deployment
 ┣ 📜 README.md          # Documentation (this file)


---

📌 API Endpoint

➡️ Classify a Number

URL:

GET /api/classify-number?number=<your_number>

Example Request:

curl "https://your-deployed-api.onrender.com/api/classify-number?number=28"

Example Response:

{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["even"],
    "digit_sum": 10,
    "fun_fact": "28 is the number of dominoes in a standard set."
}


---

⚡ How to Run Locally

1️⃣ Clone the Repository

git clone https://github.com/your-username/HNG-Backend-NumberClassifier.git
cd HNG-Backend-NumberClassifier

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the App

python app.py

The API will now be available at http://127.0.0.1:10000/api/classify-number?number=28


---

🚀 Deployment on Render

1. Push the repository to GitHub


2. Go to Render, create a new web service, and link your repository.


3. Set the Start Command to:

gunicorn app:app


4. Deploy and access your public API!




---

🛠 Technologies Used

Python 🐍

Flask 🔥

Requests 🌍 (for fetching fun facts)

Gunicorn 🚀 (for production deployment)

Render ☁️ (for hosting the API)



---

🤝 Contribution

Contributions are welcome! Feel free to fork this repository and submit a pull request.


---

📜 License

This project is licensed under the MIT License.


---

💡 Author

👤 Etini Akpayang
📧 Contact: princeakpayang@gmail.com or https://www.linkedin.com/in/etini-akpayang-754aa4101?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app


---

Now you have a beautiful README that explains everything about your repository! Let me know if you want any modifications. 🚀

