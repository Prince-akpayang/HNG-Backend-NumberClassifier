from flask import Flask, jsonify, request
import asyncio
import httpx  # Use `httpx` instead of `requests`
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi  # Convert Flask to ASGI

app = Flask(__name__)
CORS(app)

# Check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Check if a number is perfect
def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

# Check if a number is an Armstrong number
def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digit ** len(digits) for digit in digits) == number

# **Use async for fetching fun fact**
async def get_fun_fact(number):
    url = f"http://numbersapi.com/{number}?json"
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:  # **Set timeout**
            response = await client.get(url)
            if response.status_code == 200:
                return response.json().get('text', 'No fun fact available.')
    except httpx.RequestError:
        return "No fun fact available."
    return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
async def classify_number():
    try:
        number = request.args.get('number')

        # Handle missing or invalid number input
        if number is None or not number.strip().isdigit():
            return jsonify({"error": "Invalid or missing number parameter"}), 400

        number = int(number)

        # **Run functions in parallel**
        prime, perfect, armstrong = await asyncio.gather(
            asyncio.to_thread(is_prime, number),
            asyncio.to_thread(is_perfect, number),
            asyncio.to_thread(is_armstrong, number),
        )

        properties = ["armstrong"] if armstrong else []
        properties.append("even" if number % 2 == 0 else "odd")

        # **Fetch fun fact asynchronously**
        fun_fact = await get_fun_fact(number)

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

# **Convert Flask app to ASGI**
asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=10000)  # Use Uvicorn for speed
