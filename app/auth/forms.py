#! -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(Form):
    email = StringField(u'电子邮箱', validators = [Required(), Length(1, 64), 
                                               Email()])
    username = StringField(u'用户名', validators = [
        Required(), Length(1, 64), Regexp('^[A-Za-z0-9_.]*$', 0, 
                                          u'用户名必须为字母， ' 
                                          u'数字，点或者下划线')])
    password = PasswordField(u'密码', validators = [
        Required(), EqualTo('password2', message = 'Passwords must match.')])
    password2 = PasswordField(u'密码确认', validators = [Required()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError(u'邮箱已经被注册')
            
    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError(u'用户名已经被使用')

class LoginForm(Form):
    email = StringField(u'邮箱', validators = [Required(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators = [Required()])
    remember_me = BooleanField(u'保持登录')
    submit= SubmitField(u'登录')
    
class ChangePasswordForm(Form):
    old_password = PasswordField(u'旧密码', validators = [Required()])
    password = PasswordField(u'新密码', validators = [
        Required(), EqualTo('password2', message = 'Passwords must match')])
    password2 = PasswordField(u'新密码确认', validators = [Required()])
    submit = SubmitField(u'修改密码')
    
class PasswordResetRequestForm(Form):
    email = StringField(u'邮箱', validators = [Required(), Length(1, 64),
                                               Email()])
    submit = SubmitField(u'重置密码')
    
class PasswordResetForm(Form):
    email = StringField(u'邮箱', validators = [Required(), Length(1, 64),
                                               Email()])
    password = PasswordField(u'新密码', validators = [
        Required(), EqualTo('password2', message = 'Passwords must match()')])
    password2 = PasswordField(u'新密码确认', validators = [Required()])
    submit = SubmitField(u'重置密码')
    
    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first() is None:
            raise ValidationError('Unknown email address.')
            
class ChangeEmailForm(Form):
    email = StringField(u'新邮箱', validators = [Required(), Length(1, 64),
                                                   Email()])
    password = PasswordField(u'密码', validators = [Required()])
    submit = SubmitField(u'修改邮箱')
    
    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError(u'邮箱已经被注册')