from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(max_length=250)
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name if self.name else self.email} from {self.creation_date.date()}'
    