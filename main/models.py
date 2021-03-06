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
    content = models.TextField(max_length=40000,help_text="Content of the file")
    MMIE = models.CharField(max_length=200,default="text/plain",help_text="MMIE of the file, choose text/plain if you don't know what to do")
    b64 = models.BooleanField(default=False,help_text="If yes, the content will be treated as base64.")
    b64.short_description='B64'
    b64.description='base64'
    def __str__(self):
        return "File: " + self.location



