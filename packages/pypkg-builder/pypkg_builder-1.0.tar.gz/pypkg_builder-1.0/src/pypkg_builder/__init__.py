from .app import app_fn
import webbrowser
import threading

app = app_fn()

def open_browser():
    url = "http://127.0.0.1:5000/"
    webbrowser.open(url)

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()  # Open the browser after 1 second
    app.run()

