from flask import Flask, render_template_string

# python.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""<!doctype html>
<html>
<body><h1>Hello {{ name }}</h1>
<p>{{ message }}</p></body>
</html>""", name="World", message="This is Python")

if __name__ == '__main__':
    app.run(debug=True)