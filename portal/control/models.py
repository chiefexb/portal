#coding: utf-8
from django.db import models

# Create your models here.
class Perodic_Type (models.Model):
    Name=models.CharField(max_length=50,verbose_name=u'Название')
    def __unicode__(self):
        return self.Name
class Order_Kind (models.Model):
    Name=models.CharField(max_length=100,verbose_name=u'Название')
    def __unicode__(self):
        return self.Name
class Departament (models.Model):
    Dept_Code=models.CharField(max_length=5,verbose_name=u'Код подразделения')
    Dept_Name=models.CharField(max_length=400,verbose_name=u'Название подразделения')
    def __unicode__(self):
        return self.Dept_Name
class Assignment (models.Model):
    Is_Active = models.BooleanField(verbose_name=u'Активно (периодическое)')
    Is_Archive = models.BooleanField(verbose_name=u'Архивное')
    Doc_Date=models.DateField(verbose_name=u'Дата документа')
    Doc_Name=models.CharField(max_length=400,verbose_name=u'Название документа')
    Create_Date=models.DateTimeField(verbose_name=u'Дата создания')
    Dep_Code=models.CharField(max_length=400,verbose_name=u'Код подразделения')
    Is_Periodic=models.CharField(max_length=400,verbose_name=u'Периодическое')
    Perodic_Type=models.ForeignKey(Perodic_Type,blank=True,null=True,verbose_name=u'Тип периода')
    Period_End_Date=models.DateTimeField(blank=True,null=True,verbose_name=u'Дата окончания периодичности')
    Periodic_Size=models.IntegerField(blank=True,null=True,verbose_name=u'Периодичноcть')
    Executor=models.ManyToManyField(Departament,verbose_name=u'Исполнител(и)')
    Suser_Fio=models.CharField(max_length=400,verbose_name=u'Кто создал')
    Order_Kind=models.ForeignKey(Order_Kind,verbose_name=u'Тип документа')

