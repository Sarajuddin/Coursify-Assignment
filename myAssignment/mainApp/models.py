from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=15)
    role = models.CharField(max_length=100)
    current_ctc = models.CharField(max_length=10, default=0, null=True)
    expected_ctc = models.CharField(max_length=10, default=0, null=True)
    notice_period = models.CharField(max_length=50)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    resume = models.FileField(upload_to="media/", max_length=100)

    def __str__(self) -> str:
        return f"{self.id} / {self.name} / {self.email} / {self.role}"
