from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Login_admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    email=db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    designation = db.Column(db.String(150), nullable=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Emp_login(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    email = db.Column(db.String(150))
    name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150))
    emp_id = db.Column(db.Integer)
    phoneNumber=db.Column(db.Integer)   #newly added
    role =db.Column(db.String(150), nullable=False)
    late_balance = db.Column(db.Integer, default=20)
    leave_balance = db.Column(db.Integer, default=20)
    address = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    shift=db.Column(db.String(150),default="8G")
    attendances = db.relationship('Attendance', back_populates='employee', cascade='all, delete-orphan')
    freezed_account =db.Column(db.String(150),default=False)


# class Employee(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     emp_id = db.Column(db.Integer)
#     name = db.Column(db.String(150), nullable=False)
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     dob = db.Column(db.DateTime(timezone=True))
#     designation = db.Column(db.String(150), nullable=True)
#     workType = db.Column(db.String(150))
#     email = db.Column(db.String(150))
#     phoneNumber = db.Column(db.String(150))
#     adharNumber = db.Column(db.Integer)
#     gender = db.Column(db.String(150))
#     address = db.Column(db.String(150))
#     mimetype =db.Column(db.String(150))
#     profile_pic = db.Column(db.String(100000), default='Default/Default.jpeg')
    
#     attendances = db.relationship('Attendance', back_populates='employee', cascade='all, delete-orphan')
#     shift=db.Column(db.String(150))
    
    
class Attendance(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    emp_id = db.Column(db.Integer, db.ForeignKey('emp_login.id'))
    name = db.Column(db.String(150), nullable=False)
    attendance =db.Column(db.String(150))
    wages_per_Day=db.Column(db.String(150))
    inTime=db.Column(db.String(150))
    outTime=db.Column(db.String(150))
    overtime=db.Column(db.String(150),default='00:00')
    employee = db.relationship('Emp_login', back_populates='attendances')
    shiftType=db.Column(db.String(150))
    shiftIntime = db.Column(db.String(150))
    shift_Outtime = db.Column(db.String(150))
    TotalDuration=db.Column(db.String(150))
    lateBy=db.Column(db.String(150))
    earlyGoingBy=db.Column(db.String(150))
    punchRecords=db.Column(db.String(150))	
    


class LoginEmp(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    email=db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
    
class Shift_time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shiftIntime = db.Column(db.String(150))
    shift_Outtime = db.Column(db.String(150))
    shiftType = db.Column(db.String(150))
    week_off=db.Column(db.DateTime(timezone=True))
    emp_id=db.Column(db.Integer)
    
    
class Backup(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    emp_id = db.Column(db.Integer, db.ForeignKey('emp_login.id'))
    attendance =db.Column(db.String(150))
    wages_per_Day=db.Column(db.String(150))
    inTime=db.Column(db.String(150))
    outTime=db.Column(db.String(150))
    overtime=db.Column(db.String(150),default='00:00')
    shiftType=db.Column(db.String(150))
    shiftIntime = db.Column(db.String(150))
    shift_Outtime = db.Column(db.String(150))
    TotalDuration=db.Column(db.String(150))
    lateBy=db.Column(db.String(150))
    earlyGoingBy=db.Column(db.String(150))
    punchRecords=db.Column(db.String(150))	
    
    
    
    
    
class NewShift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_date_day = db.Column(db.String(255))
    filename=db.Column(db.String(255))
    
    # Define columns for days 1 through 31
    for day_num in range(1, 32):
        locals()[f"day_{day_num}"] = db.Column(db.String(255))
    monday = db.Column(db.String(255))
    tuesday = db.Column(db.String(255))
    wednesday = db.Column(db.String(255))
    thursday = db.Column(db.String(255))
    friday = db.Column(db.String(255))
    
class notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=db.func.now())
    emp_name = db.Column(db.String(255))
    permission_type = db.Column(db.String(255))
    emp_id = db.Column(db.Integer)
    from_time = db.Column(db.String(150), nullable=False)
    to_time = db.Column(db.String(150), nullable=False)
    req_id = db.Column(db.Integer)
    
# Late Model (Example)
class late(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    emp_name = db.Column(db.String(150), nullable=False)
    reason = db.Column(db.String(150), nullable=False)
    from_time = db.Column(db.String(150), nullable=False)
    to_time = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(150), default='Pending')
    # hod_approval = db.Column(db.String(150), default='Pending')
    approved_by = db.Column(db.String(150), default='Pending')
    hr_approval = db.Column(db.String(150), default='Pending')
    date = db.Column(db.DateTime(timezone=True), default=func.now())
# Leave Model (Example)
    
class leave(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    emp_name = db.Column(db.String(150), nullable=False)
    reason = db.Column(db.String(150), nullable=False)
    from_time = db.Column(db.String(150), nullable=False)
    to_time = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(150), default='Pending')
    # hod_approval = db.Column(db.String(150), default='Pending')
    approved_by = db.Column(db.String(150), default='Pending')
    hr_approval = db.Column(db.String(150), default='Pending')
    date = db.Column(db.DateTime(timezone=True), default=func.now())



class Festival(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    holiday=db.Column(db.String(150), nullable=False)
    date=db.Column(db.String(150), nullable=False)

class user_edit(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    name = db.Column(db.String(150), nullable=False)
    old_data=db.Column(db.String(150), nullable=False)
    new_data=db.Column(db.String(150), nullable=False)
    data_type=db.Column(db.String(150), nullable=False)

class Week_off(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    date= db.Column(db.String(150), nullable=False)