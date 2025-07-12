from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = ['Home', 'About', 'FAQ', 'Contacts']

@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Home', menu=menu)

@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='About')

@app.route('/faq')
def faq():
    print(url_for('faq'))
    return render_template('FAQ.html', title='FAQ')

@app.route('/contacts', methods=["POST", "GET"])
def contacts():
    message_sent = False

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        message = request.form.get('message')

        print(f"Name: {username}, Email: {email}, Message: {message}")

        message_sent = True

    return render_template('contacts.html', title='Contacts', message_sent=message_sent, menu=menu)


@app.route('/profile/<path:username>')
def profile(username):
    return f"User: {username}"

if __name__ == '__main__':
    app.run(debug=True)