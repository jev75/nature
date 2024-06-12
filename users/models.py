from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        verbose_name='Avataras',
        upload_to='images/avatars/%Y/%m/%d/',
        default='images/avatars/default.jpg',
        blank=True,
    )

    class Meta:
        verbose_name = 'Profilis'
        verbose_name_plural = 'Profiliai'

    def __str__(self):
        return self.user.username

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return settings.STATIC_URL + 'images/avatars/default.jpg'


