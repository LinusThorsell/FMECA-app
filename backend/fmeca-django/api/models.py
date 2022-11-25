from audioop import maxpp
from email.mime import application
from email.policy import default
from functools import partial
from logging import critical
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# All models except "Project" has
# auto-incremented integer primary key.

class Project(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

class Node(models.Model):
    name = models.CharField(max_length=50, blank=True)
    platform = models.CharField(max_length=50, blank=True, null=True)
    load_set_type = models.CharField(max_length=50, blank=True, null=True)
    redundant = models.CharField(max_length=20, blank=True, null=True)
    sync_loss = models.CharField(max_length=20, blank=True, null=True)
    # ForeignKeys
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True)

class CPU(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=10, default="")
    unit_id = models.CharField(max_length=10, blank=True, null=True)
    iop_ref = models.CharField(max_length=10, blank=True, null=True)
    accs_sync_master = models.CharField(max_length=10, blank=True, null=True)
    domain_border = models.CharField(max_length=20, blank=True, null=True)
    # ForeignKeys
    node = models.ForeignKey(Node, on_delete=models.CASCADE, blank=True, null=True)

class Partition(models.Model):
    name = models.CharField(max_length=20, blank=True)
    is_ltm = models.CharField(max_length=20, blank=True, null=True)
    fixed_start = models.BigIntegerField(default=None, null=True)
    partition_id = models.IntegerField(default=None, null=True)
    # ForeignKeys
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, blank=True, null=True)

class Application(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    partition = models.ForeignKey(Partition, on_delete=models.CASCADE, blank=True, null=True)
    # ForeignKeys
    project = models.ForeignKey(Project, related_name="app_project_set", on_delete=models.CASCADE, blank=True, null=True)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE, blank=True, null=True)

class ApplicationInstance(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    # ForeignKeys
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)

class Connection(models.Model):
    # ForeignKeys
    requirer = models.ForeignKey(Application, related_name="requirer_set", on_delete=models.CASCADE, blank=True, null=True)
    provider = models.ForeignKey(Application, related_name="provider_set", on_delete=models.CASCADE, blank=True, null=True)

class Thread(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    rategroup = models.CharField(max_length=20, blank=True, null=True)
    #ForeignKeys
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)
    
class PacPort(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    interface = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    #ForeignKeys
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, blank=True, null=True)

#----------------------------------------------------------------

class CommentsDict(models.Model):
    # ForeignKeys
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class KeyVal(models.Model):
    key = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True) 
    # ForeignKeys
    container = models.ForeignKey(CommentsDict, on_delete=models.CASCADE)