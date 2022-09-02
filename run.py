from imp import reload
import uvicorn
import threading
from spindrift_dash.api.main import app as api_app
from spindrift_dash.src.main import app as dash_app

def run_api():
    uvicorn.run(api_app)

def run_dash():
    dash_app.run_server(debug=True)

def run():
    print("Starting API")
    threading.start_new_thread(run_api, ())
    # print("Starting Dash")
    # threading.start_new_thread(run_dash, ())
    # print("Done")
    # while True:
    #     pass

if __name__ == "__main__":
    run()

    