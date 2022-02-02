import asyncio
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/get", methods=["GET"])
def index():

    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()

    result = loop.run_until_complete(get_json_data())
    return jsonify({"result": result})


# helper async function is here :
async def get_json_data():

    # Opening JSON file
    data = open('data.json')
    return_data = json.load(data)

    await asyncio.sleep(5)

    return return_data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)