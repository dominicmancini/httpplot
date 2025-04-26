# server.py

from flask import Flask, send_file, jsonify, render_template_string
from io import BytesIO
import threading
import webbrowser
import time
from .templates.templates import httpgd, httpgd_2
# import loader

app = Flask(__name__)
plot_history = []


@app.route('/')
def index():
    # httpgd = loader.load_resource_text("httpgd.html")
    # return render_template_string(httpgd)
    return render_template_string(httpgd_2())

@app.route('/plots')
def get_plots():
    return jsonify([f'/plot/{i}' for i in range(len(plot_history))])

@app.route('/plot/<int:plot_id>')
def get_plot(plot_id):
    return send_file(BytesIO(plot_history[plot_id]), mimetype='image/png')

def save_current_plot():
    from matplotlib import pyplot as plt
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_history.append(buf.getvalue())
    buf.close()

_server_thread = None

def _run_app():
    from waitress import serve
    serve(app, host='127.0.0.1', port=5000)

def start_server():
    global _server_thread
    if _server_thread is None or not _server_thread.is_alive():
        _server_thread = threading.Thread(target=_run_app, daemon=True)
        _server_thread.start()
        time.sleep(1)  # Let server start
        webbrowser.open("http://127.0.0.1:5000")

def stop_server():
    print("Stop server is not implemented (you can just close the REPL).")
