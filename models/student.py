from odoo import fields, models


class Student(models.Model):
    _name = 'student.info'
    _rec_name = 'student_name'
    _description = 'Student'

    student_name = fields.Char(string="Student Name",required=True)
    email = fields.Char(string="Email",required=True)
    mobile = fields.Char(string="Mobile",required=True)
    secondary_mobile = fields.Char(string="Alternative Mobile")

    age = fields.Integer(string="Age")
    address = fields.Text(string="Address")

