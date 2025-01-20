from flask import Flask, render_template_string

app = Flask(name)

@app.route('/')
def epiphany_message():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Happy Epiphany!</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .message-container {
                background: linear-gradient(135deg, #fbb034, #ffdd00);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                width: 90%;
                max-width: 400px;
            }
            .message-container h1 {
                font-size: 2rem;
                color: #ffffff;
                margin-bottom: 10px;
            }
            .message-container p {
                font-size: 1.2rem;
                color: #ffffff;
                margin-bottom: 20px;
            }
            .message-container .holiday-icon {
                font-size: 3rem;
                margin-bottom: 15px;
            }
            .message-container .btn {
                display: inline-block;
                background-color: #ffffff;
                color: #fbb034;
                padding: 10px 20px;
                font-size: 1rem;
                border-radius: 25px;
                text-decoration: none;
                font-weight: bold;
                transition: background-color 0.3s, color 0.3s;
            }
            .message-container .btn:hover {
                background-color: #fbb034;
                color: #ffffff;
            }
        </style>
    </head>
    <body>
        <div class="message-container">
            <div class="holiday-icon">✨🎉</div>
            <h1>Happy Epiphany!</h1>
            <p>Wishing you a joyous holiday filled with peace, love, and blessings. Let's celebrate this day with happiness and gratitude.</p>
            <a href="https://t.me/yourchannel" class="btn">Join the Celebration</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if name == 'main':
    app.run(debug=True)