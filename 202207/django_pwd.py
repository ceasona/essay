# https://www.qttc.net/427-django-crypt.html
from django.conf import settings

settings.configure()
from django.contrib.auth.hashers import make_password, check_password

pwd = 'shucangdao123'
mpwd = make_password(pwd, None, 'pbkdf2_sha256')  # 创建django密码，第三个参数为加密算法
print(mpwd)
pwd_bool = check_password(pwd, mpwd)
print(pwd_bool)

db_pwd = "pbkdf2_sha256$260000$o7g1mO3rLbSEKbF9VCVNoP$pCFDqwk6kXmhU0OCsXbVGmC2ZvpCSbWlZjA1OOIdvuM="
print(check_password(pwd, db_pwd))


