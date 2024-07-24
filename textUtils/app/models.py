from django.db import models

# Create your models here.
class Contact(models.Model):
    FirstName=models.CharField(max_length=122)
    LastName=models.CharField(max_length=122)
    Email=models.CharField(max_length=122)
    Phone=models.CharField(max_length=122)
    desc=models.CharField(max_length=122)
    City=models.CharField(max_length=122)
    state_choice=[
        ("AP","Aunachal Pradesh"),
        ("UP","Uttar Pradesh"),
        ("Mp","Madhya Pradesh")
    ]
    inputState=models.CharField(max_length=122,choices=state_choice,default="UP")
    inputZip=models.CharField(max_length=122)

    def __str__(self) -> str:
        return self.FirstName
    
    

