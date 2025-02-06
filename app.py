from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Helper function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Helper function to check if a number is perfect
def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

# Helper function to check if a number is an Armstrong number
def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digit ** len(digits) for digit in digits) == number

# Helper function to fetch fun fact from Numbers API
def get_fun_fact(number):
    response = requests.get(f'http://numbersapi.com/{number}?json')
    if response.status_code == 200:
        return response.json().get('text', '')
    return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        number = request.args.get('number')

        if not number.isdigit():
            return jsonify({"number": number, "error": True}), 400

        number = int(number)

        prime = is_prime(number)
        perfect = is_perfect(number)
        armstrong = is_armstrong(number)

        properties = []
        if armstrong:
            properties.append("armstrong")
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        fun_fact = get_fun_fact(number)

        response = {
            "number": number,
            "is_prime": prime,
            "is_perfect": perfect,
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(number)),
            "fun_fact": fun_fact
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)  
