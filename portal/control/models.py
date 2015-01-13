from django.db import models

# Create your models here.
class Perodic_Type (models.Model):
    Name=CharField(max_length=50,verbose_name=u'Название')
class Order_Kind (models.Model):
    Name=CharField(max_length=100,verbose_name=u'Название')
class Assignment (models.Model):
    Is_Active = models.BooleanField(verbose_name=u'Активно (периодическое)')
    Is_Archive = models.BooleanField(verbose_name=u'Архивное')
    Doc_Date=models.DateField(verbose_name=u'Дата документа')
    Doc_Name=CharField(max_length=400,verbose_name=u'Название документа')
    Create_Date=models.DateTimeField(verbose_name=u'Дата создания')
    Dep_Code=CharField(max_length=400,verbose_name=u'Код подразделения')
    Is_Periodic=CharField(max_length=400,verbose_name=u'Периодическое')
    Perodic_Type=models.ForeignKey( Perodic_Type,verbose_name=u'Тип периода')
    Periodic_Size=IntegerField(verbose_name=u'Периодичноcть')
    Suser_Fio=CharField(max_length=400,verbose_name=u'Кто создал')
    Order_Kind=models.ForeignKey(Order_Kind,verbose_name=u'Тип документа')

