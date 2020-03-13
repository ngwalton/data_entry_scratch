import uuid
from django.db import models

# need additional tables for type and minute
class Bird(models.Model):
    obs_id = models.AutoField(primary_key=True, db_index=True, editable=False, help_text="Observation id")
    entry_id = models.ForeignKey("Site", on_delete=models.CASCADE, help_text="Foreign key on Site entry_id")
    spec_id = models.ForeignKey("Alpha", on_delete=models.PROTECT, help_text="Foreign key on Alpha spec (alpha code)")
    type_choices = [("S", "singing"), ("C", "calling"), ("O", "observed"), ("F", "flyover")]
    type = models.CharField(max_length=1, choices=type_choices, null=False, help_text="Type of detection")
    minute = models.PositiveSmallIntegerField(null=False, help_text="Minute of first detection")

# need additional tables for observer, sid?, entry, sky, and tempc
class Site(models.Model):
    entry_id = models.AutoField(primary_key=True, db_index=True, editable=False)
    observer = models.CharField(max_length=200, null=False, help_text="Name of observer")
    sid = models.CharField(max_length=10, null=False, help_text="Site id")
    day = models.DateTimeField(null=False, help_text="Date of count")
    entry = models.PositiveSmallIntegerField(null=False, help_text="First or second entry")
    sky = models.PositiveSmallIntegerField(null=False, help_text="Sky condition")
    tempc = models.PositiveSmallIntegerField(null=False, help_text="Temperature degrees C")

class Alpha(models.Model):
    spec_id = models.AutoField(primary_key=True, db_index=True, editable=False)
    spec = models.CharField(max_length=4,  null=False, unique=True, help_text="Four letter alpha code")
    common = models.CharField(max_length=200, null=False, unique=True, help_text="Common name")
    sci = models.CharField(max_length=200, null=False, unique=True, help_text="Scientific name")

