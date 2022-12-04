from app.extensions import db, ma
from datetime import datetime

# User Table
class Accounts(db.Model):
	# __tablename__ = 'Accounts'
	id = db.Column(db.String(5), primary_key=True, nullable=False)
	fullname = db.Column(db.String(35), nullable=False)
	address = db.Column(db.String(50), nullable=False)
	mobile = db.Column(db.String(11), nullable=False)
	guardian = db.Column(db.String(35), nullable=False)
	guardian_num = db.Column(db.String(11), nullable=False)

	school = db.Column(db.String(50), nullable=False)
	yearLevel = db.Column(db.String(20), nullable=False)
	unit = db.Column(db.String(5), nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	email = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(50), nullable=False)
	reports = db.relationship('Reports', backref='reporter')
	feedbacks = db.relationship('Feedbacks', backref='feedbacker')
	tobepaid = db.relationship('Tobepaid', backref='tobepaid')
	payments = db.relationship('Payments', backref='payments')

# Admin Table/ Rents and Billings
# class Admin(db.Model):
# 	# __tablename__ = 'admin'
# 	id = db.Column(db.Integer, primary_key=True)
# 	total_rent = db.Column(db.Float)
# 	user_rent = db.Column(db.Float)
# 	e_bill = db.Column(db.Float)
# 	w_bill = db.Column(db.Float)
# 	wifi_bill = db.Column(db.Float)
# 	payment_date = db.Column(db.DateTime, default=datetime.utcnow)

# Bill Declaration/ Inputs from Admin
class Tobepaid(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	unit = db.Column(db.String(5), db.ForeignKey('accounts.unit'), nullable=False)
	user_rent = db.Column(db.Float, nullable=False)
	e_bill = db.Column(db.Float, nullable=False)
	w_bill = db.Column(db.Float, nullable=False)
	wifi_bill = db.Column(db.Float, nullable=False)
	month = db.Column(db.String(15), nullable=False)
	monthNotif = db.relationship('Notification', backref='monthNotif')
	monthPayment = db.relationship('Payments', backref='monthPayment')

# Notification Table/ For Admin to be notified of a tenants payment
class Notification(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	paidBy = db.Column(db.String(35), db.ForeignKey('accounts.fullname'), nullable=False)
	unit = db.Column(db.String(5), nullable=False)
	billType = db.Column(db.String(10), nullable=False)
	amount = db.Column(db.Float, nullable=False)
	status = db.Column(db.String(10), nullable=False)
	month = db.Column(db.String(15), db.ForeignKey('tobepaid.month'))
	date_created = db.Column(db.DateTime, default=datetime.now)

# Total Payments Table
class Total(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	totalRent = db.Column(db.Float, nullable=False)
	totalElectric = db.Column(db.Float, nullable=False)
	totalWifi = db.Column(db.Float, nullable=False)
	totalWater = db.Column(db.Float, nullable=False)
	month = db.Column(db.String(15), nullable=False)


# Payments Table/ Store data if tenants are paid or not
class Payments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(35), db.ForeignKey('accounts.fullname'), nullable=False)
	unit = db.Column(db.String(5), nullable=False)
	waterbill = db.Column(db.String(10), nullable=False)
	electricbill = db.Column(db.String(10), nullable=False)
	wifibill = db.Column(db.String(10), nullable=False)
	rent = db.Column(db.String(10), nullable=False)
	month = db.Column(db.String(15), db.ForeignKey('tobepaid.month'))

# Announcement Table
class Announcements(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	posts = db.Column(db.String(300), nullable=False)
	date_posted = db.Column(db.DateTime, default=datetime.now)

# Reports Table
class Reports(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	by = db.Column(db.String(35), db.ForeignKey('accounts.fullname'), nullable=False)
	reports = db.Column(db.String(300), nullable=False)
	date_reported = db.Column(db.DateTime, default=datetime.now)

# Feedbacks Table
class Feedbacks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	by = db.Column(db.String(35), db.ForeignKey('accounts.fullname'), nullable=False)
	feedbacks = db.Column(db.String(300), nullable=False)
	date_sent = db.Column(db.DateTime, default=datetime.now)

class Reminders(db.Model):
	# __tablename__ = 'reminders'
	id = db.Column(db.Integer, primary_key=True)
	reminder = db.Column(db.String(100), nullable=False)
	date_added = db.Column(db.DateTime, default=datetime.now)
	
class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Accounts
