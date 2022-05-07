from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

"""
class Creators(models.Model):
    text_id = models.BigAutoField() # ID of text in the Text DB
    owner = models.BigAutoField() # ID of owner in the User DB
    def __str__(self):
        if Text.objects.filter(id = self.text_id).exists():
            text = Text.objects.get(id = self.text_id)
            return_file_str = "{} (ID {})".format(text.location,self.text_id)
        else:
            return_file_str = "Unknown (ID {})".format(self.text_id)
        if User.objects.filter(id = self.owner):
            user = User.objects.get(id = self.owner)
            return_user_str = "created by {} (ID {})".format(user.username,self.owner)
        else:
            return_user_str = "unknown creators"
        return return_file_str + ", " + return_user_str
"""

class Text(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE,help_text="The owner of this text")
    location = models.CharField(max_length=200,help_text="Location of the file",primary_key=True)
    content = models.TextField(help_text="Content of the file")
    MMIE_choices = (
        ("text/plain", "Plain Text"),
        ("text/html", "HTML"),
        ("text/css", "CSS"),
        ("text/javascript", "Javascript"),
    )
    MMIE = models.CharField(max_length=200,default="text/plain",choices=MMIE_choices,help_text="MMIE of the file, choose Plain Text if you don't know what to do")



