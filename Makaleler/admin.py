from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField


# Create your models here.
class Yetenekler(models.Model):
    yetenek_adi = models.CharField(max_length = 200,verbose_name = "Yetenek Adı")
    yetenekyuzdesi = models.IntegerField(verbose_name = "Yetenek Yüzdesi")

    def __str__(self):
        return self.yetenek_adi

class İsDeneyimi(models.Model):
    firma_adi = models.CharField(max_length = 200,verbose_name = "Firma Adı")
    baslangic_tarihi: models.DateTimeField(verbose_name="baslama_tarihi Tarihi")
    bitis_tarihi: models.DateTimeField(verbose_name="bitis_tarihi Tarihi")
    görev=models.CharField(max_length = 200,verbose_name = "Görev Adı")
    aciklama=RichTextField()
    firmaicon = models.FileField(blank=True,null=True, verbose_name="eklemek isterseniz fotograf seçin ")
    def __str__(self):
        return self.firma_adi
    
class Summary (models.Model):
    ozet=  models.TextField(max_length=None)

class KisiselBilgiler(models.Model):
    fotograf= models.FileField(blank=True,null=True, verbose_name="eklemek isterseniz fotograf seçin ")
    lokasyon=models.TextField(blank=True,null=True, verbose_name="Lokasyon")
    aktiflokasyon=models.TextField(blank=True,null=True, verbose_name="şuanki lokasyonunuz ( Boş Geçilebilir )")
    telefon=models.TextField(blank=True,null=True, verbose_name="telefon numarası giriniz")
    telefon2=models.TextField(blank=True,null=True, verbose_name="ikinci telefon numarası giriniz")
    eposta1=models.TextField(blank=True,null=True, verbose_name="eposta 1 i  giriniz")
    eposta2=models.TextField(blank=True,null=True, verbose_name="eposta 2 i  giriniz")

class projeler(models.Model):
    proje_ismi=models.TextField(verbose_name="proje ismi")
    platform = models.TextField(verbose_name="Platform")
    acıklama=RichTextField(verbose_name="Platform")

class badget(models.Model):
    badget=models.TextField(verbose_name="Badget İsmi")
class ozellikler(models.Model):
    baslik=models.TextField(verbose_name="proje ismi")
    aciklama=RichTextField()

    
