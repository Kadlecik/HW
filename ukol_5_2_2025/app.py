from flask import Flask, render_template, redirect, url_for, request
# Import dat a další konfigurace

app = Flask(__name__)

# Seznam uživatelů
@app.route('/users')
def users():
    return render_template('users.html', users=users)

@app.route('/profile/<int:id>')
def profile(id):
    # Vyhledáme uživatele nebo provedeme další logiku
    user = ...  # logika pro získání uživatele dle id
    return render_template('profile.html', user=user)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message_text = request.form.get('message')
        print("Přijatá zpráva:", message_text)
        return redirect(url_for('users'))
    return render_template('contact.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        message_text = request.form.get('message')
        print("Přijatá zpráva:", message_text)
        return redirect(url_for('users'))
    return render_template('message.html')

# Další routy, např. home, about, ...
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
