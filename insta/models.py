from django.db import models

# Create your models here.
class post(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=300)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
