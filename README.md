# Asynchronous-flaskapi
This is the code for the create asynchronous API in python using Flask and asyncio.Asynchronous programming is a method by which we achieve parallel programming.

## Prerequisites:-
- [Python3.7+](https://www.python.org/downloads/release/python-370/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [async](https://docs.python.org/3/library/asyncio.html)



## How does Asynchronous API work?
Asynchronous API in Python follows the same principle of Asynchronous programming. These APIs don’t return the data immediately. They provide a callback to the client when the results are ready. In the meantime, the client can continue to execute other functions while the API is preparing the results. 


There’s one disadvantage as well, these APIs are not suitable where you need an instant response from the API as the latency is the issue here.


<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/4gLRzjX/Screenshot-from-2022-02-02-22-49-03.png" height="175px"/></a>



## Example 1 :-
```
@app.route("/get", methods=["GET"])
def index():

    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()

    result = loop.run_until_complete(get_json_data())
    return jsonify({"result": result})
```
I have defined an API endpoint `/get` where we’ll set an event loop. Once the loop is set we’ll try to get that event by calling the function `get_event_loop()`. The loop will keep on running until a response is returned from the `get_json_data()`. Once the result is ready, then return response.


One point to remember here is that `get_json_data()` is an async function here.
Now we’ll define the async function `get_json_data()`:
```
async def get_json_data():

    # Opening JSON file
    data = open('data.json')
    return_data = json.load(data)

    await asyncio.sleep(5)

    return return_data
```
The function will do nothing just read the `json data` and asynchronously wait for 5 seconds and then return `return_data`.

<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/d2p2PW1/Screenshot-from-2022-02-02-23-10-25.jpg" height="255px"/></a>