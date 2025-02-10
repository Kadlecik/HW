from flask import Flask, render_template, redirect, url_for, request
from data import users_data, users_details  # Import dat z externího souboru

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def users():
    # Předáme fiktivní seznam uživatelů do šablony users.html
    return render_template('users.html', users=users_data)

@app.route('/profile/<int:id>')
def profile(id):
    # Vyhledáme uživatele podle id
    user = next((u for u in users_data if u["id"] == id), None)
    if user is None:
        return "Uživatel nenalezen", 404

    # Přidáme detailní informace k uživateli
    details = users_details.get(id, {})
    user.update(details)
    return render_template('profile.html', user=user)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Zpracování dat z formuláře
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Logika pro uložení nebo odeslání zprávy
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Zpracování formulářových dat
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Například zde můžete zprávu uložit nebo odeslat emailem
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
