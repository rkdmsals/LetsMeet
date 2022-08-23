from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User모델과 Profile을 1:1로 연결
    description = models.TextField(blank=True)      # 자기소개 칸
    nickname = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def get_absolute_url(self):
        return reverse('user_posts', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.username