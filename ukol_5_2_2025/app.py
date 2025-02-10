from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Zpracování dat z formuláře
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Sem můžete přidat logiku pro uložení nebo odeslání zprávy
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/users')
def users():
    # Zde načítáme šablonu se seznamem uživatelů
    return render_template('users.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Alternativní zpracování formuláře
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Zde můžete přidat logiku pro zpracování zprávy
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
