from flask import Blueprint, render_template, url_for, redirect, request
from app.models import Accounts
from app.extensions import db
from werkzeug.security import generate_password_hash
import random, string, os

module = Blueprint("signup", __name__, url_prefix="/signup")


@module.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # get form data from request
        numbers = string.digits
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        random_pass = numbers + lower_case + upper_case
        generate = random.sample(random_pass, 5)
        generated_pass = "".join(generate)
        new_fullname = request.form[ 'fullname' ]
        new_address = request.form[ 'address' ]
        new_number = request.form[ 'number' ]
        new_guardian = request.form[ 'guardian' ]
        new_gnum = request.form[ 'guardian_number' ]
        new_school = request.form[ 'school' ]
        new_year = request.form[ 'year' ]
        new_unit = request.form[ 'unit' ]
        new_email = request.form[ 'e-mail' ]
        new_password = generate_password_hash(request.form['pw'])

        # add form data to database
        user = Accounts(id=generated_pass, fullname=new_fullname, address=new_address, mobile=new_number, guardian=new_guardian, guardian_num=new_gnum,
        school=new_school, yearLevel=new_year, unit=new_unit, email=new_email, password=new_password)
        db.session.add(user)
        db.session.commit()

        # redirect to login page
        return redirect(url_for("login.index"))

    # render register page
    return render_template("index.html")
