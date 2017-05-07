#from django.db import models

# Create your models here.
from django.db import models

class logs(models.Model):
    s_no= models.CharField(max_length=30)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=60)
    src_ip = models.CharField(max_length=30)
    src_mac = models.CharField(max_length=50)
    dst_ip = models.CharField(max_length=30)
    dst_mac = models.CharField(max_length=50)
    type= models.CharField(max_length=30)
    length= models.CharField(max_length=30)
    remarks= models.CharField(max_length=30)


class alerts(models.Model):
    s_no= models.CharField(max_length=30)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=60)
    message = models.CharField(max_length=30)
    attack = models.CharField(max_length=50)
    src_ip = models.CharField(max_length=30)
    src_mac = models.CharField(max_length=50)
    severity= models.CharField(max_length=30)



class iptables(models.Model):
    rule_no = models.CharField(max_length=10)
    interface = models.CharField(max_length=10)
    src_ip = models.CharField(max_length=30)
    src_port=models.CharField(max_length=10)
    target=models.CharField(max_length=10)
    chain=models.CharField(max_length=10)
    
