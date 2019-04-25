from django.db import models
from datetime import datetime
import bcrypt


class UserManager(models.Manager):
    def reg_validator(self, data):
        errors = {}

        if len(data['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters long'

        if len(data['username']) < 3:
            errors['username'] = 'Username must be at least 3 characters long'

        else:
            if len(User.objects.filter(username=data['username'])) > 0:
                errors['username'] = 'Username already exists, please log in'

        if len(data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'

        elif data['password'] != data['confirmpw']:
            errors['password'] = 'Passwords must match'

        if len(str(data['datehired'])) < 1:
            errors['datehired'] = 'You must enter a date before submitting'

        elif datetime.strptime(data['datehired'], '%Y-%m-%d') > datetime.now():
            errors['datehired'] = 'You were already hired, please enter the appropriate date of when you were hired'
        return errors


    def login_validator(self, data):
        errors = {}

        if len(User.objects.filter(username=data['username'])) > 1:
            errors['username'] = 'Username already exists'

        elif len(User.objects.filter(username=data['username'])) == 0:
            errors['username'] = 'Please register with us before attempting to log in '

        else:
            user = User.objects.get(username=data['username'])
            if not bcrypt.checkpw(data['password'].encode(), user.password.encode()):
                errors['password'] = 'Your password was incorrect, Please try again'
        return errors

class ListManager(models.Manager):
    def list_validator(self, data):
        errors = {}

        if len(data['item']) == 0:
            errors['item'] = 'Item must not be empty'

        elif len(data['item']) < 3:
            errors['item'] = 'Item must be at least 3 characters long'
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username =  models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    datehired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class List(models.Model):
    item = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='list', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='lists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ListManager()
