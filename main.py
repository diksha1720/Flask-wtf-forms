from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import email_validator
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "secret key"


class LoginForm(FlaskForm):
    email = StringField(label="email", validators=[DataRequired(), Email()])
    password = PasswordField(label="password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="login")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    # loginform.validate_on_submit()
    if loginform.validate_on_submit():
        if loginform.email.data == "admin@email.com" and loginform.password.data =="12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=loginform)


if __name__ == '__main__':
    app.run(debug=True)
