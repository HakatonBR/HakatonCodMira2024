from django.contrib.auth.base_user import BaseUserManager
from django.db.transaction import atomic

import unicodedata


class UserManager(BaseUserManager):
    def _create_user(
            self, email, password=None, **extra_fields
    ):
        # if not username:
        #     raise ValueError("Имя пользователя должно быть указано")

        if not (email):
            raise ValueError("Почта или телефон должны быть указаны")

        if not password:
            raise ValueError("Пароль должен быть указан")

        if email:
            email = self.normalize_email(email)

        # if phone_number:
        #     phone_number = PhoneNumber.from_string(phone_number).as_e164

        user = self.model(
            # username=unicodedata.normalize("NFKC", username),
            email=email,

            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        print(user)
        return user

    
    @atomic
    def create_superuser(
        self, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        return self._create_user(
            email, password, **extra_fields
        )
    
    @atomic
    def create_account(
        self, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)

        return self._create_user(
            email, password, **extra_fields
        )
