from flask import Flask, render_template, url_for, request, flash,redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hdvsdvhsd9v89fhv2dfds2'

menu = ['Home', 'About', 'FAQ', 'Contact us']

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
    if request.method == 'POST':
        username = request.form.get('username').strip()
        email = request.form.get('email').strip()
        message = request.form.get('message').strip()

        error = False

        if not username or len(username) < 2:
            flash('Name should contain at least 2 letters', 'error')
            error = True

        if '@' not in email or '.' not in email.split('@')[-1]:
            flash('Enter a valid email address', 'error')
            error = True

        if not message or len(message) < 10:
            flash('Message should have at least 10 symbols', 'error')
            error = True

        if error:
            return render_template('contacts.html', title='Contact us', menu=menu,
                                   username=username, email=email, message=message)

        print(f"Name: {username}, Email: {email}, Message: {message}")
        flash('Message sent!', 'success')
        return redirect(url_for('contacts'))

    return render_template('contacts.html', title='Contact us', menu=menu)


@app.route('/profile/<path:username>')
def profile(username):
    return f"User: {username}"

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Page not found", menu=menu)

if __name__ == '__main__':
    app.run(debug=True)