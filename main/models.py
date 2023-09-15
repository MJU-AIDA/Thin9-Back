from django.db import models
from accounts.models import Account
# Create your models here.

# 사용자별 업로드 정보
class Gallery(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE) # 유저의 id(Account의 primary key('id' 필드)와 연결)
    image_id = models.AutoField(primary_key=True) # 음식 이미지 번호
    name = models.CharField(max_length=30, blank=True, null=False) # 음식 이름
    total = models.IntegerField(blank=True, null=True) # 음식 총량
    kcal = models.IntegerField(blank=True, null=True) # 칼로리
    carbon = models.IntegerField(blank=True, null=True) # 탄수화물
    pro = models.IntegerField(blank=True, null=True) # 단백질
    fat = models.IntegerField(blank=True, null=True) # 지방
    upload_date = models.DateTimeField(auto_now_add=True) # 이미지 업로드 날짜
    food_image = models.ImageField(upload_to="media/", blank=True, null=True) # 음식 이미지 파일


    class Meta:
        managed = True

    def __str__(self):
        return self.name or ''

# 식품영양정보 DB의 음식
class Food(models.Model):
    name = models.CharField(max_length=30) # 음식 이름
    total = models.IntegerField() # 음식 총량
    kcal = models.IntegerField() # 칼로리
    carbon = models.IntegerField() # 탄수화물
    pro = models.IntegerField() # 단백질
    fat = models.IntegerField() # 지방


    class Meta:
        managed = True