from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

from users.managers.user_manager import UserManager


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(
        verbose_name="Имя пользователя",
        max_length=150,
        unique=True,
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', ]

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        
    def has_module_perm(self, app_label):
        if self.is_active and self.is_superuser:
            return True
        
    def __str__(self) -> str:
        return str(f"{self.email}")
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def update_fields(self, **kwargs):
        for field, value in kwargs.items():
            if field == 'password':
                self.set_password(value)
            else:
                setattr(self, field, value)

        self.save()
