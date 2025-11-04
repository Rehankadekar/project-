from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Simple HTML page with a button to download the file
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Download ZIP File</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f2f2f2;
            }
            h2 {
                color: #333;
            }
            a.button {
                display: inline-block;
                padding: 15px 25px;
                font-size: 18px;
                color: white;
                background-color: #007bff;
                border: none;
                border-radius: 10px;
                text-decoration: none;
                transition: 0.3s;
            }
            a.button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h2>Download Your ZIP File</h2>
        <a href="/download" class="button">Click Here to Download</a>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/download')
def download():
    # Make sure bs.zip exists in the same directory as this file
    return send_file('bs.zip', as_attachment=True)

if __name__ == '__main__':
    # Use Render’s assigned port
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
