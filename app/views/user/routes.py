from flask import Blueprint, render_template, url_for, redirect, request, session, jsonify, json, flash
from app.models import Accounts, UserSchema, Announcements, Reports, Tobepaid, Notification, Feedbacks, Payments
from app.extensions import db
import os, random
from datetime import datetime, timedelta
from sqlalchemy import func

module = Blueprint("user", __name__)


def get_user_by_id(id):
    user = Accounts.query.get(id)
    return UserSchema().dump(user)


@module.route("/", methods=["GET"])
def index():
    # redirect to login page if there is no user id in session
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    if not user_id:
        return redirect(url_for("login.index"))

    # query announcements
    announcements = Announcements.query.order_by(Announcements.date_posted.desc()).limit(10).all()

    # query feedbacks
    new_feedback = Feedbacks.query.filter_by(by=user.fullname).order_by(Feedbacks.date_sent.desc()).limit(20).all()

    # query reports
    new_report = Reports.query.filter_by(by=user.fullname).order_by(Reports.date_reported.desc()).limit(20).all()

    # query bills per unit
    unitBills = Tobepaid.query.filter_by(unit=user.unit).all()

    # query notifications
    user_notif = Notification.query.filter_by(paidBy=user.fullname).all()

    # query payment month
    month = datetime.now().date()
    currentMonth = month.strftime('%B')

    # query past payments
    getdate = datetime.today().date()
    monthNow = datetime.strftime(getdate, '%B')
    paymentMonth = Tobepaid.query.filter(Tobepaid.month==monthNow).first()
    monthlyBills = Tobepaid.query.filter(Tobepaid.month==paymentMonth.month > datetime.today() - timedelta(days=30)).first()
   
    pastBills = Tobepaid(unit=user.unit, user_rent=monthlyBills.user_rent, e_bill=monthlyBills.e_bill,
    w_bill=monthlyBills.w_bill, wifi_bill=monthlyBills.wifi_bill, month=monthlyBills.month)

    # query new payments
    newmonthlyBills = Tobepaid.query.filter(Tobepaid.month==paymentMonth.month <= datetime.today() - timedelta(days=30)).first()
        
    newBills = Tobepaid(unit=user.unit, user_rent=newmonthlyBills.user_rent, e_bill=newmonthlyBills.e_bill,
        w_bill=newmonthlyBills.w_bill, wifi_bill=newmonthlyBills.wifi_bill, month=newmonthlyBills.month)

    # render user profile page
    user = get_user_by_id(user_id)
    return render_template("new_user_dash.html", user=user, announcements=announcements, new_reports=new_report, user_notif=user_notif,
    unitBills=unitBills, new_feedback=new_feedback, currentMonth=currentMonth, pastBills=pastBills, newBills=newBills, editable=True)

@module.route("/update", methods=["POST","GET"])
def update():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    # fullname = request.form.get('user_fullname')
    # print(request.form.get('user_fullname'))
    if request.method == 'POST':
        user.fullname = request.form.get('user_fullname')
        user.address = request.form.get('user_address')
        user.mobile = request.form.get('user_mobile')
        user.guardian = request.form.get('user_guardian')
        user.guardian_num = request.form.get('user_guardian_num')
        user.school = request.form.get('user_school')
        user.yearLevel = request.form.get('user_year')
        user.email = request.form.get('user_email')

        db.session.commit()

    return redirect(url_for('user.index'))

@module.route("/users", methods=["GET"])
def users():
    users = Accounts.query.all()
    return render_template("users.html", users=users)


@module.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = get_user_by_id(id)
    return render_template("user_dash.html", user=user, editable=False)


@module.route("/users/<int:id>", methods=["DELETE"])
def delete(id):
    session.pop("user_id", None)

    # delete user
    user = Accounts.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return {"message": "User successfully deleted"}

@module.route('/report', methods=['POST', 'GET'])
def report():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login.index"))
    if request.method == 'POST':
        user = Accounts.query.get_or_404(user_id)
        reporter = Accounts.query.filter_by(fullname=user.fullname).first()
        report = request.form.get('repInput')
        add_report = Reports(reports=report, by=reporter.fullname)
        db.session.add(add_report)
        db.session.commit()
        if request.method == 'GET':
            return render_template('new_user_dash.html')
    return redirect(url_for('user.index'))

@module.route('/feedbacks', methods=['POST', 'GET'])
def feedback():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login.index"))
    if request.method == 'POST':
        user = Accounts.query.get_or_404(user_id)
        feedbacker = Accounts.query.filter_by(fullname=user.fullname).first()
        feedback = request.form.get('feedInput')
        add_feedback = Feedbacks(feedbacks=feedback, by=feedbacker.fullname)
        db.session.add(add_feedback)
        db.session.commit()
        if request.method == 'GET':
            return render_template('new_user_dash.html')
    return redirect(url_for('user.index'))

@module.route('/confirmRent', methods=['POST', 'GET'])
def confirmRent():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)

    if request.method == 'POST':
        
        getdate = datetime.today().date()
        monthNow = datetime.strftime(getdate, '%B')
        paymentMonth = Tobepaid.query.filter_by(month=monthNow).first()
        user_unit = Tobepaid.query.filter_by(unit=user.unit).first()

        check_exist = Payments.query.filter_by(name=user.fullname, rent="Paid", unit=user.unit).first()
        if check_exist:
            flash ("You are already paid.")
            print("bayad ka na")
        else:
            notif = Notification(paidBy=user.fullname, unit=user.unit, billType='Rent', amount=user_unit.user_rent, status='Paid', month=paymentMonth.month)
            db.session.add(notif)
            db.session.commit()
        return redirect(url_for('user.index'))
    return redirect(url_for('user.index'))
 

@module.route('/confirmEBill', methods=['POST', 'GET'])
def confirmEBill():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    if request.method == 'POST':
        getdate = datetime.today().date()
        monthNow = datetime.strftime(getdate, '%B')
        paymentMonth = Tobepaid.query.filter_by(month=monthNow).first()
        user_unit = Tobepaid.query.filter_by(unit=user.unit).first()

        check_exist = Payments.query.filter_by(name=user.fullname, electricbill="Paid", unit=user.unit).first()
        if check_exist:
            flash ("You are already paid.")
        else:
            notif = Notification(paidBy=user.fullname, unit=user.unit, billType='Electric Bill', amount=user_unit.e_bill, status='Paid', month=paymentMonth.month)
            db.session.add(notif)
            db.session.commit()
        return redirect(url_for('user.index'))
    return redirect(url_for('user.index'))

@module.route('/confirmWBill', methods=['POST', 'GET'])
def confirmWBill():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    if request.method == 'POST':
        getdate = datetime.today().date()
        monthNow = datetime.strftime(getdate, '%B')
        paymentMonth = Tobepaid.query.filter_by(month=monthNow).first()
        user_unit = Tobepaid.query.filter_by(unit=user.unit).first()

        check_exist = Payments.query.filter_by(name=user.fullname, waterbill="Paid", unit=user.unit).first()
        if check_exist:
            flash ("You are already paid.")
        else:
            notif = Notification(paidBy=user.fullname, unit=user.unit, billType='Water Bill', amount=user_unit.w_bill, status='Paid', month=paymentMonth.month)
            db.session.add(notif)
            db.session.commit()
        return redirect(url_for('user.index'))
    return redirect(url_for('user.index'))

@module.route('/confirmWifiBill', methods=['POST', 'GET'])
def confirmWifiBill():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    if request.method == 'POST':
        getdate = datetime.today().date()
        monthNow = datetime.strftime(getdate, '%B')
        paymentMonth = Tobepaid.query.filter_by(month=monthNow).first()
        user_unit = Tobepaid.query.filter_by(unit=user.unit).first()

        check_exist = Payments.query.filter_by(name=user.fullname, wifibill="Paid", unit=user.unit).first()
        if check_exist:
            flash ("You are already paid.")
        else:  
            notif = Notification(paidBy=user.fullname, unit=user.unit, billType='Wifi Bill', amount=user_unit.wifi_bill,  status='Paid', month=paymentMonth.month)
            db.session.add(notif)
            db.session.commit()
        return redirect(url_for('user.index'))
    return redirect(url_for('user.index'))

# view previous monthly bills
@module.route('/pastMonth', methods=['POST', 'GET'])
def pastMonth():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    if request.method == 'POST':
        getdate = datetime.today().date()
        monthNow = datetime.strftime(getdate, '%B')
        paymentMonth = Tobepaid.query.filter(Tobepaid.month==monthNow).first()
        monthlyBills = Tobepaid.query.filter(Tobepaid.month==paymentMonth.month > datetime.today() - timedelta(days=30)).first()

        pastBills = Tobepaid(unit=user.unit, user_rent=monthlyBills.user_rent, e_bill=monthlyBills.e_bill,
            w_bill=monthlyBills.w_bill, wifi_bill=monthlyBills.wifi_bill, month=monthlyBills.month)
        return render_template('new_user_dash.html', pastBills=pastBills, user=user)
    return redirect(url_for('user.index'))

@module.route('/newMonth', methods=['POST', 'GET'])
def newMonth():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    if request.method == 'POST':
        getdate = datetime.today().date()
        monthNow = datetime.strftime(getdate, '%B')
        paymentMonth = Tobepaid.query.filter(Tobepaid.month==monthNow).first()
        newmonthlyBills = Tobepaid.query.filter(Tobepaid.month==paymentMonth.month <= datetime.today() - timedelta(days=30)).first()
        
        newBills = Tobepaid(unit=user.unit, user_rent=newmonthlyBills.user_rent, e_bill=newmonthlyBills.e_bill,
            w_bill=newmonthlyBills.w_bill, wifi_bill=newmonthlyBills.wifi_bill, month=newmonthlyBills.month)
        return render_template('new_user_dash.html', newBills=newBills, user=user)
    return redirect(url_for('user.index'))
        
@module.route('/paymentCheck', methods=['POST', 'GET'])
def paymentCheck():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)

    # check if paid to disable payment button later
    getRentStatus = Payments.query.filter_by(name=user.fullname, rent='Paid').first()
    isPaid = getRentStatus.rent
    # if getRentStatus:
    if request.method == 'POST' or 'GET':
        print(isPaid)
        return redirect(url_for('user.index', {isPaid}))
    return render_template('new_user_dash.html'), {isPaid}
    # return redirect(url_for('user.index', {"ispaid":isPaid}))

@module.route('/date')
def get_current_date():
    user_id = session.get("user_id")
    user = Accounts.query.get_or_404(user_id)
    # check if paid to disable payment button later
    getRentStatus = Payments.query.filter_by(rent="Paid").first()
    isPaid = getRentStatus.rent
    return {"Date": datetime.today(), "ispaid": isPaid}