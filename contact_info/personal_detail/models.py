from django.db import models


class AddContact(models.Model):

    gender_choice = (
        ('male','male'),
        ('female','female')
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    dob = models.DateField()
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    gender  = models.CharField(choices=gender_choice, max_length=100, default=None)
    image = models.ImageField(upload_to='profile_picture/', default=None, blank=True)
    # created_at = models. DateTimeField()
    def __str__(self):
        return self.name
# Create your models here.
