from flask import Flask, jsonify, request
import asyncio
import httpx
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

async def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math?json"
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            r = await client.get(url)
            return r.json().get('text', 'No fun fact available.') if r.status_code == 200 else "No fun fact available."
    except httpx.RequestError:
        return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
async def classify_number():
    number = request.args.get('number', "").strip()
    if not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    prime, perfect, armstrong = await asyncio.gather(
        asyncio.to_thread(is_prime, number),
        asyncio.to_thread(is_perfect, number),
        asyncio.to_thread(is_armstrong, number),
    )

    properties = ["armstrong"] if armstrong else []
    properties.append("even" if number % 2 == 0 else "odd")

    response = {
        "number": number,
        "is_prime": prime,
        "is_perfect": perfect,
        "properties": properties,
        "digit_sum": sum(map(int, str(number))),
        "fun_fact": await get_fun_fact(number),
    }

    return jsonify(response)

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=10000)
