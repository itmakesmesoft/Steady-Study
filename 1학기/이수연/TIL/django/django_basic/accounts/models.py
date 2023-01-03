from django.db import models
from django.contrib.auth.models import AbstractUser

# 우리만의 유저 만듦. 상속만 받아놓음
class User(AbstractUser):
    pass
