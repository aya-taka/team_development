from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError(u'ユーザー名を入力してください！')
        if not password:
            raise ValueError(u'パスワードを入力してください！')
        user = self.model(username=username, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, **extra_fields)


# django既定のユーザーテーブルをもとに、自作できるようAbstractBaseUserとPermissionsMixinを継承
class User(AbstractBaseUser, PermissionsMixin):
    # ユーザーテーブルの要素を定義
    # idは自動生成されるものを使用
    username = models.CharField('ユーザー名', max_length=30, unique=True)
    mailaddress = models.EmailField('メールアドレス', unique=True, blank=True)
    is_staff = models.BooleanField('スタッフ', default=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = verbose_name

    # 必須メソッドを定義
    def get_full_name(self):
        return self.__str__()

    get_short_name = get_full_name