from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2: return False
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i + (n // i if i != n // i else 0)
    return total == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    if not number or not number.lstrip('-').isdigit():
        return jsonify({"error": True, "number": number}), 400

    number = int(number)

    # Handle negative numbers
    if number < 0:
        return jsonify({
            "number": number,
            "is_prime": False,
            "is_perfect": False,
            "properties": [],
            "digit_sum": sum(int(digit) for digit in str(abs(number))),
            "fun_fact": "Negative numbers are not classified.",
            "error": True
        }), 400

    properties = []
    if is_armstrong(number): properties.append("armstrong")
    if number % 2 == 0: properties.append("even")
    else: properties.append("odd")

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": f"{number} is a great number!"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
