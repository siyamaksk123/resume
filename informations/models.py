from django.db import models
from django.core.exceptions import ValidationError
import os , random

# Create your models here.
def get_file_extension(file):
    base_name = os.path.basename(file)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_image(instance, filename):
    rand_name = random.randint(1, 9999999999999999999)
    name , ext = get_file_extension(filename)
    final_name = f"{instance.id}-{rand_name}{ext}"
    return f"products/{final_name}"

def validate_text(value):
    if len(value) < 2 :
        raise ValidationError('مقدار معتبر وارد کنید')

class InformationsModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام', validators=[validate_text])
    family= models.CharField(max_length=50, verbose_name='نام خانوادگی', validators=[validate_text])
    phone = models.IntegerField(verbose_name='تلفن همراه')
    email = models.EmailField(verbose_name='ایمیل')
    address = models.TextField(verbose_name='آدرس')
    university = models.CharField(max_length=75, verbose_name='دانشگاه محل تحصیل', validators=[validate_text])
    field_of_study = models.CharField(max_length=100, verbose_name='رشته تحصیلی', validators=[validate_text])
    graduation_year = models.CharField(verbose_name='سال فراغت از تحصیل')
    job_title = models.CharField(max_length=100, verbose_name='عنوان شغلی', validators=[validate_text])
    company = models.CharField(max_length=75, verbose_name='نام شرکت', validators=[validate_text])
    start_date = models.CharField(verbose_name='تاریخ شروع')
    end_date = models.CharField(verbose_name='تاریخ پایان')
    job_descriptions = models.TextField(verbose_name='شرح وظایف')
    skills = models.TextField(verbose_name='مهارت ها', blank=True, null=True)
    certificates = models.TextField(blank=True, null=True, verbose_name='گواهینامه')
    profile_photo = models.ImageField(upload_to=upload_image, verbose_name='عکس پروفایل', blank=True, null=True)

    class Meta:
        verbose_name ='مشخصات رزومه'
        verbose_name_plural ='مشخصات رزومه ها'

    def __str__(self):
        return self.name