from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n):
    # Only positive numbers > 1 can be prime.
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(n):
    # For this task, any single-digit number (|n| < 10) should return False.
    if abs(n) < 10:
        return False
    if n < 1:
        return False
    total = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n

def is_armstrong(n):
    # Use the absolute value for Armstrong check so that negative numbers are handled similarly.
    digits = list(map(int, str(abs(n))))
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def generate_properties(n):
    parity = "even" if n % 2 == 0 else "odd"
    # If the number is Armstrong, include "armstrong" along with parity.
    if is_armstrong(n):
        return ["armstrong", parity]
    else:
        return [parity]

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    start_time = time.time()
    num_str = request.args.get('number')

    # Validate input: must be convertible to an integer.
    try:
        num = int(num_str)
    except (ValueError, TypeError):
        return jsonify({
            "number": num_str,
            "error": True
        }), 400

    result = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": generate_properties(num),
        "digit_sum": digit_sum(num),
        "fun_fact": generate_fun_fact(num)
    }

    elapsed_time = (time.time() - start_time) * 1000  # in milliseconds
    if elapsed_time > 800:
        return jsonify({"error": True, "message": "Response time exceeded 800ms"}), 500

    return jsonify(result), 200

def generate_fun_fact(n):
    # Currently, only provides a fun fact if the number is Armstrong.
    if is_armstrong(n):
        digits = list(map(int, str(abs(n))))
        power = len(digits)
        fact = f"{n} is an Armstrong number because " + " + ".join(f"{d}^{power}" for d in digits)
        fact += f" = {n}"
        return fact
    return "No fun fact available for this number."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
