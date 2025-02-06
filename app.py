from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable CORS support
import math
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n):
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
    if n < 1:
        return False
    total = 1
    # Only need to check up to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n

def is_armstrong(n):
    # Armstrong numbers are usually defined for non-negative numbers.
    digits = list(map(int, str(abs(n))))
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def generate_properties(n):
    props = []
    # Check if Armstrong
    if is_armstrong(n):
        props.append("armstrong")
    # Check if prime
    if is_prime(n):
        props.append("prime")
    # Check if perfect
    if is_perfect(n):
        props.append("perfect")
    # Check parity
    if n % 2 == 0:
        props.append("even")
    else:
        props.append("odd")
    return props

def generate_fun_fact(n):
    facts = []
    if is_armstrong(n):
        digits = list(map(int, str(abs(n))))
        power = len(digits)
        fact = f"{n} is an Armstrong number because " + " + ".join(f"{d}^{power}" for d in digits)
        fact += f" = {n}"
        facts.append(fact)
    # You can add more fun facts here for prime, perfect, etc.
    if facts:
        return facts[0]
    return "No fun fact available for this number."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    start_time = time.time()
    num_str = request.args.get('number')

    # Validate input: must be convertible to an integer
    try:
        num = int(num_str)
    except (ValueError, TypeError):
        return jsonify({
            "number": num_str,
            "error": True
        }), 400

    # Build the result dictionary according to the specification
    result = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": generate_properties(num),
        "digit_sum": digit_sum(num),
        "fun_fact": generate_fun_fact(num)
    }

    elapsed_time = (time.time() - start_time) * 1000  # milliseconds
    # Optionally check response time (should be < 500ms)
    if elapsed_time > 800:
        return jsonify({"error": True, "message": "Response time exceeded 800ms"}), 500

    return jsonify(result), 200

if __name__ == '__main__':
    # Use the port your hosting provider specifies (e.g., PORT environment variable)
    # Here we are using port 10000 as before.
    app.run(host="0.0.0.0", port=10000, debug=True)
