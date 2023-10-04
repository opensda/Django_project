from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')


    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# class EmailVerification(models.Model):
#     code = models.UUIDField(unique=True)
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     expiration = models.DateTimeField()
#
#     def __str__(self):
#         return f'EmailVerification object for {self.user.email}'
#
#     def send_verification_email(self):
#         link = reverse('user:email_verification', kwargs={'email': self.user.email, 'code': self.code})
#         verification_link = settings.DOMAIN_NAME + link
#         subject = 'Подтверждение учетной записи'
#         message = f'Для подтверждения перейдите по ссылке: {verification_link}'
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[self.user.email],
#             fail_silently=False,
#         )
#
#     def is_expired(self):
#         return now() >= self.expiration
