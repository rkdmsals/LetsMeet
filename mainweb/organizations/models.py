from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Moim(models.Model):
    name = models.CharField(max_length=100, unique=True)
    detail = models.TextField(null=True)

    join_users = models.ManyToManyField('auth.User', verbose_name=u'참여자', blank=True, related_name='moim_users')
    # 모임을 만든 사람이 모임장이 될 수 있게 설정
    admin_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True) #모임장 삭제되면 모임 삭제
    #admin_user = models.OneToOneField('auth.User', verbose_name=u'모임장', null=False) 

    created_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    slug = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    # def num_users(self):
    #     """모임에 참여하는 인원수를 return --> 지금은 유저 이름만 리턴된다."""
    #     return self.join_users

    # @models.permalink
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the Moim model"""
        #return reverse('moim-detail-view', args=[str(self.name)])
        #return reverse('', kwargs={"pk": self.id})
        #return ('moim-detail-view', (), {'slug': self.slug})
        return reverse('organizations:moim-detail-view', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Moim, self).save(*args, **kwargs)