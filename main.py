from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '06f77aa26f171f93597603fe60b4f37a'

@app.route("/")
@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
   form = ContactForm()
   return render_template('contact.html', form = form)

if __name__ == "__main__":
    app.run(debug=True)
