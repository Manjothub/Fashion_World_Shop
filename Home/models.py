from django.db import models

class Banners(models.Model):
    banner_img = models.ImageField(upload_to='uploads/banner-img/')
    banner_name = models.CharField(max_length=100,null=True)
    banner_taglines = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.banner_name
    