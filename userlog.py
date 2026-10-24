
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Login credentials
inbuild_user_name = "admin"
inbuild_user_password = "admin123"

# HTML and CSS in the same Python file
page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', sans-serif;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 25px;
            background: linear-gradient(135deg, #f8d7e8, #d5e3ff, #e8d5ff);
        }

        .container {
            width: 900px;
            max-width: 100%;
            min-height: 520px;
            display: flex;
            overflow: hidden;
            border-radius: 24px;
            background: white;
            box-shadow: 0 20px 60px rgba(51, 40, 100, 0.18);
        }

        .left {
            width: 50%;
            padding: 55px 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            background: linear-gradient(145deg, #7765e8, #a76be9, #e28ac2);
        }

        .left .logo {
            font-size: 42px;
            margin-bottom: 25px;
        }

        .left h1 {
            font-size: 35px;
            line-height: 1.25;
            margin-bottom: 18px;
        }

        .left p {
            font-size: 15px;
            line-height: 1.8;
            color: #f5efff;
        }

        .features {
            margin-top: 30px;
            line-height: 2.3;
            font-size: 14px;
        }

        .right {
            width: 50%;
            padding: 55px 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .right h2 {
            color: #292347;
            font-size: 30px;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #85829a;
            font-size: 14px;
            margin-bottom: 30px;
        }

        label {
            display: block;
            color: #413b59;
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 8px;
        }

        .input-box {
            margin-bottom: 22px;
        }

        input {
            width: 100%;
            padding: 14px 15px;
            border: 1px solid #dedbea;
            border-radius: 10px;
            font-size: 15px;
            outline: none;
            background: #faf9ff;
            transition: 0.3s;
        }

        input:focus {
            border-color: #8a70ed;
            box-shadow: 0 0 0 3px rgba(138, 112, 237, 0.12);
        }

        button {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            background: linear-gradient(100deg, #7967e9, #ad6ce4);
            box-shadow: 0 7px 18px rgba(121, 103, 233, 0.25);
            transition: 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 22px rgba(121, 103, 233, 0.35);
        }

        .message {
            padding: 12px;
            margin-bottom: 20px;
            border-radius: 9px;
            font-size: 14px;
            text-align: center;
        }

        .success {
            color: #17683c;
            background: #e2f8eb;
        }

        .error {
            color: #b42335;
            background: #ffebee;
        }

        .footer {
            margin-top: 25px;
            text-align: center;
            color: #9994ab;
            font-size: 12px;
        }

        @media (max-width: 650px) {
            body {
                padding: 15px;
            }

            .container {
                flex-direction: column;
            }

            .left, .right {
                width: 100%;
                padding: 35px 25px;
            }

            .left h1 {
                font-size: 28px;
            }

            .left .logo {
                font-size: 32px;
                margin-bottom: 12px;
            }

            .features {
                margin-top: 12px;
            }
        }
    </style>
</head>

<body>
    <div class="container">

        <div class="left">
            <div class="logo">✦</div>
            <h1>Welcome to<br>Your Digital Space</h1>
            <p>
                Sign in to access your account and enjoy
                a simple, secure and beautiful experience.
            </p>

            <div class="features">
                <div>✦ Simple and easy login</div>
                <div>✦ Clean, modern design</div>
                <div>✦ Responsive user interface</div>
            </div>
        </div>

        <div class="right">
            <h2>Login</h2>
            <p class="subtitle">Welcome back! Please enter your details.</p>

            {% if message %}
                <div class="message {{ status }}">
                    {{ message }}
                </div>
            {% endif %}

            <form method="POST">
                <div class="input-box">
                    <label for="username">Username</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        placeholder="Enter your username"
                        autocomplete="username"
                        required
                    >
                </div>

                <div class="input-box">
                    <label for="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        placeholder="Enter your password"
                        autocomplete="current-password"
                        required
                    >
                </div>

                <button type="submit">Sign In →</button>
            </form>

            <div class="footer">
                © 2026 My Login Page. All rights reserved.
            </div>
        </div>

    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    status = ""

    if request.method == "POST":
        user_name = request.form.get("username", "")
        user_password = request.form.get("password", "")

        if (
            user_name == inbuild_user_name
            and user_password == inbuild_user_password
        ):
            message = "Login successful! Welcome, admin."
            status = "success"
        else:
            message = "Invalid username or password. Please try again."
            status = "error"

    return render_template_string(
        page,
        message=message,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)
