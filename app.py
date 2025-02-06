from flask import Flask, request, jsonify
import math
import time

app = Flask(__name__)

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
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n

def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n

@app.route('/validate', methods=['GET'])
def validate_number():
    start_time = time.time()
    num_str = request.args.get('number')

    if not num_str or not num_str.isdigit():
        return jsonify({"error": True, "number": num_str}), 400

    num = int(num_str)
    result = {
        "error": False,
        "number": num,
        "isPrime": is_prime(num),
        "isPerfect": is_perfect(num),
        "isArmstrong": is_armstrong(num)
    }

    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    if elapsed_time > 800:
        return jsonify({"error": True, "message": "Response time exceeded 800ms"}), 500

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)