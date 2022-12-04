from flask import Blueprint, request, redirect, url_for, render_template, session, jsonify
from sqlalchemy import desc
from app.models import Accounts, Announcements, Reports, Feedbacks, Tobepaid, Notification, Payments, Total
from app.extensions import db
from datetime import datetime
import json
module = Blueprint("admin", __name__, url_prefix="/admin")

@module.route('/confirm-payment', methods=['POST', 'GET'])
def add_to_payment():

	tenant_name = Notification.query.with_entities(Notification.paidBy).first()		
	bill = Notification.query.with_entities(Notification.billType).first()
	unit_get = Notification.query.with_entities(Notification.unit).first()
	month_get = Notification.query.with_entities(Notification.month).first()
	get_id = Notification.query.with_entities(Notification.id).first()
	amount = Notification.query.with_entities(Notification.amount).first()

	exist = Payments.query.filter_by(month=month_get.month, name=tenant_name.paidBy).first()
	if exist:
		if bill.billType=="Rent":
			this_one = Payments.query.filter_by(month=month_get.month, name=tenant_name.paidBy).first()
			this_one.rent = "Paid"
			db.session.commit()

			plus_rent = Total.query.filter_by(month=month_get.month).first()
			current_rent = Total.query.with_entities(Total.totalRent).filter_by(month=month_get.month).first()

			plus_rent.totalRent = current_rent.totalRent + amount.amount
			db.session.commit()
		elif bill.billType=="Water Bill":
			this_one = Payments.query.filter_by(month=month_get.month, name=tenant_name.paidBy).first()
			this_one.waterbill = "Paid"
			db.session.commit()

			plus_water = Total.query.filter_by(month=month_get.month).first()
			current_water = Total.query.with_entities(Total.totalWater).filter_by(month=month_get.month).first()

			plus_water.totalWater = current_water.totalWater + amount.amount
			db.session.commit()
		elif bill.billType=="Wifi Bill":
			this_one = Payments.query.filter_by(month=month_get.month, name=tenant_name.paidBy).first()
			this_one.wifibill = "Paid"
			db.session.commit()

			plus_wifi = Total.query.filter_by(month=month_get.month).first()
			current_wifi = Total.query.with_entities(Total.totalWifi).filter_by(month=month_get.month).first()

			plus_wifi.totalWifi = current_wifi.totalWifi + amount.amount
			db.session.commit()
		elif bill.billType=="Electric Bill":
			this_one = Payments.query.filter_by(month=month_get.month, name=tenant_name.paidBy).first()
			this_one.electricbill = "Paid"
			db.session.commit()

			plus_electric = Total.query.filter_by(month=month_get.month).first()
			current_electric = Total.query.with_entities(Total.totalElectric).filter_by(month=month_get.month).first()

			plus_electric.totalElectric = current_electric.totalElectric + amount.amount
			db.session.commit()
		
		db.session.query(Notification).filter(Notification.id==get_id.id).delete()
		db.session.commit()
	else:
		if bill.billType=="Rent":
			rent_bill = "Paid"
			wifi_bill = "Not Paid"
			water_bill = "Not Paid"
			e_bill = "Not Paid"

			plus_rent = Total.query.filter_by(month=month_get.month).first()
			current_rent = Total.query.with_entities(Total.totalRent).filter_by(month=month_get.month).first()
			plus_rent.totalRent = current_rent.totalRent + amount.amount
			db.session.commit()
		elif bill.billType=="Water Bill":
			rent_bill = "Not Paid"
			wifi_bill = "Not Paid"
			water_bill = "Paid"
			e_bill = "Not Paid"

			plus_water = Total.query.filter_by(month=month_get.month).first()
			current_water = Total.query.with_entities(Total.totalWater).filter_by(month=month_get.month).first()
			plus_water.totalWater = current_water.totalWater + amount.amount
			db.session.commit()
		elif bill.billType=="Wifi Bill":
			rent_bill = "Not Paid"
			wifi_bill = "Paid"
			water_bill = "Not Paid"
			e_bill = "Not Paid"

			plus_wifi = Total.query.filter_by(month=month_get.month).first()
			current_wifi = Total.query.with_entities(Total.totalWifi).filter_by(month=month_get.month).first()
			plus_wifi.totalWifi = current_wifi.totalWifi + amount.amount
			db.session.commit()
		elif bill.billType=="Electric Bill":
			rent_bill = "Not Paid"
			wifi_bill = "Not Paid"
			water_bill = "Not Paid"
			e_bill = "Paid"

			plus_electric = Total.query.filter_by(month=month_get.month).first()
			current_electric = Total.query.with_entities(Total.totalElectric).filter_by(month=month_get.month).first()
			plus_electric.totalElectric = current_electric.totalElectric + amount.amount
			db.session.commit()

		new_payment = Payments(name=tenant_name.paidBy, unit=unit_get.unit, waterbill=water_bill, electricbill=e_bill, wifibill=wifi_bill, rent=rent_bill, month=month_get.month)
		db.session.add(new_payment)
		db.session.commit()

		db.session.query(Notification).filter(Notification.id==get_id.id).delete()
		db.session.commit()
	return redirect(url_for('admin.admin'))

@module.route('/reject-payment', methods=['POST', 'GET'])
def not_add_to_payment():
	get_id = Notification.query.with_entities(Notification.id).first()

	db.session.query(Notification).filter(Notification.id==get_id.id).delete()
	db.session.commit()

	return redirect(url_for('admin.admin'))

@module.route('/', methods=['POST', 'GET'])
def admin():
	if request.method == 'POST' or 'GET':
		# get all info per unit
		unit1 = Accounts.query.filter_by(unit='1').all()
		unit2 = Accounts.query.filter_by(unit='2').all()
		unit3 = Accounts.query.filter_by(unit='3').all()
		unit4 = Accounts.query.filter_by(unit='4').all()
		unit5 = Accounts.query.filter_by(unit='5').all()
		unit6 = Accounts.query.filter_by(unit='6').all()
		unit7 = Accounts.query.filter_by(unit='7').all()
		unit8 = Accounts.query.filter_by(unit='8').all()

		# get all tenants info
		tenants = Accounts.query.all()

		# query announcements by descending order
		new_post = Announcements.query.order_by(Announcements.date_posted.desc()).limit(10).all()
		viewReports = Reports.query.order_by(Reports.date_reported.desc()).limit(20).all()
		viewFeedbacks = Feedbacks.query.order_by(Feedbacks.date_sent.desc()).limit(20).all()
		
		# query notifications
		admin_notif = Notification.query.all()
		admin_notif_count = Notification.query.count()

		#query paid tenants
		paid_tenants_e = Payments.query.filter_by(electricbill="Paid").order_by(Payments.unit.asc())
		paid_tenants_wi = Payments.query.filter_by(wifibill="Paid").order_by(Payments.unit.asc())
		paid_tenants_wa = Payments.query.filter_by(waterbill="Paid").order_by(Payments.unit.asc()).all()
		paid_tenants_r = Payments.query.filter_by(rent="Paid").order_by(Payments.unit.asc()).all()

		#get month now
		getdate = datetime.today().date()
		monthNow = datetime.strftime(getdate, '%B')

		#compute every bill
		rent_computation()

		# set bill amounts
		totalrent = Total.query.with_entities(Total.totalRent).filter_by(month=monthNow).first()
		totalwifi = Total.query.with_entities(Total.totalWifi).filter_by(month=monthNow).first()
		totalwater = Total.query.with_entities(Total.totalWater).filter_by(month=monthNow).first()
		totalelectric = Total.query.with_entities(Total.totalElectric).filter_by(month=monthNow).first()

		rents_paid = totalrent.totalRent
		e_bills_paid = totalelectric.totalElectric
		w_bills_paid = totalwater.totalWater
		wifi_bills_paid = totalwifi.totalWifi
		rent = rents_paid + e_bills_paid + w_bills_paid + wifi_bills_paid

		if request.method == 'POST' or 'GET':
			return render_template('admin.html', paid_tenants_wi=paid_tenants_wi, rent=rent, rents_paid=rents_paid, e_bills_paid=e_bills_paid, w_bills_paid=w_bills_paid,
			admin_notif=admin_notif, paid_tenants_e=paid_tenants_e, paid_tenants_r=paid_tenants_r, paid_tenants_wa=paid_tenants_wa, wifi_bills_paid=wifi_bills_paid,
			unit1=unit1, unit2=unit2, unit3=unit3, unit4=unit4, unit5=unit5, unit6=unit6, unit7=unit7, unit8=unit8, tenants=tenants, new_post=new_post, viewReports=viewReports, viewFeedbacks=viewFeedbacks)
	return render_template('admin.html'), {admin_notif_count}
	return redirect(url_for('admin.admin_key'))

def rent_computation():
	getdate = datetime.today().date()
	monthNow = datetime.strftime(getdate, '%B')

	this_month_exist = Total.query.filter_by(month=monthNow).all()
	if not this_month_exist:
		update_total = Total(totalRent='0.00', totalElectric='0.00', totalWifi='0.00', totalWater='0.00', month=monthNow)
		db.session.add(update_total)
		db.session.commit()

@module.route('/admin_key', methods=['POST', 'GET'])
def admin_key():
	if request.method == 'POST':
		key = request.form[ 'admin_key' ]
		if key=="EdFer@12!90":
			return redirect(url_for('admin.admin'))
		else:
			return "Wrong admin key!"

	return render_template("admin_log.html")

@module.route('/posts', methods=['POST', 'GET'])
def post():
	if request.method == 'POST':
		post = request.form.get('annInput')
		add_post = Announcements(posts=post)
		db.session.add(add_post)
		db.session.commit()
		new_post = Announcements.query.order_by(Announcements.date_posted.desc()).all()
		if request.method == 'GET':
			return redirect(url_for('admin.admin', new_post=new_post))
	return redirect(url_for('admin.admin'))
	
@module.route('/reports', methods=['POST', 'GET'])
def reports():
	viewReports = Reports.query.order_by(Reports.date_reported.desc()).all()
	return render_template('admin.html', viewReports=viewReports)

@module.route('/feedbacks', methods=['POST', 'GET'])
def feedbacks():

	viewFeedbacks = Feedbacks.query.order_by(Feedbacks.date_sent.desc()).all()
	return render_template('admin.html', viewFeedbacks=viewFeedbacks)

@module.route('/bills', methods=['POST', 'GET'])
def bills():
	if request.method == 'POST':
		unit = request.form.get('unit')
		rent = 2000.00
		getwBill = request.form.get('waterBill')
		wBill = float(getwBill)
		geteBill = request.form.get('electricBill')
		eBill = float(geteBill)
		getwifiBill = request.form.get('wifiBill')
		wifiBill = float(getwifiBill)
		month = request.form.get('month')
		send = Tobepaid(unit=unit, user_rent=rent, w_bill=wBill, e_bill=eBill, wifi_bill=wifiBill, month=month)

		db.session.add(send)
		db.session.commit()
		
		return redirect(url_for('admin.admin'))
		# return render_template('admin.html')
	return redirect(url_for('admin.admin'))

@module.route('/remove', methods=['POST', 'GET'])
def remove():
	if request.method == 'POST':
		nameToRemove = request.form.get('nameToRemove')
		mobileToRemove = request.form.get('mobileToRemove')

		# removeTenant = Accounts.query.filter_by(fullname=nameToRemove, mobile=mobileToRemove).first()
		# print(removeTenant)

		# print(nameToRemove, mobileToRemove)

		remove_id = Accounts.query.with_entities(Accounts.id).filter_by(fullname=nameToRemove, mobile=mobileToRemove).first()

		db.session.query(Accounts).filter(Accounts.id==remove_id.id).delete()
		db.session.commit()

		return redirect(url_for('admin.admin'))
	return redirect(url_for('admin.admin'))

@module.route('/move', methods=['POST', 'GET'])
def move():
	if request.method == 'POST':
		nameToMove = request.form.get('nameToMove')
		mobileToMove = request.form.get('mobileToMove')
		print(nameToMove)
		print(mobileToMove)

@module.route('/viewRent', methods=['POST', 'GET'])
def viewRent():
	if request.method == 'POST':
		getdate = datetime.today().date()
		monthNow = datetime.strftime(getdate, '%B')
		print(monthNow)
		rents = Payments.query.filter_by(month=monthNow).all()
		print(rents)
		return redirect(url_for('admin.admin'))
	return redirect(url_for('admin.admin'))