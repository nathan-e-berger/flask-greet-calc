from flask import Flask

app = Flask(__name__)

@app.get("/welcome")
def show_welcome():
    """Returns welcome"""

    return """
    <h1>Welcome</h1>"""

@app.get("/welcome/home")
def show_welcome_home():
    """Returns welcome home"""

    return """
    <h1>Welcome Home</h1>
"""


@app.get("/welcome/back")
def show_welcome_back():
    """Returns welcome back"""

    return """
    <h1>Welcome Back</h1>
"""