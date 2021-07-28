from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField


# Create your models here.
class ProfilFotografı(models.Model):
    ProfilFotografı =models.FileField(blank=True,null=True, verbose_name="eklemek isterseniz fotograf seçin ")
    def __str__(self):
        return "Profil Fotografı"


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


class Egitimler (models.Model):
    egitim_adi = models.CharField(max_length = 200,verbose_name = "Egitim Adı")
    baslangic_tarihi: models.DateTimeField(verbose_name="baslama_tarihi Tarihi")
    bitis_tarihi: models.DateTimeField(verbose_name="bitis_tarihi Tarihi")
    aciklama=RichTextField()
    firmaicon = models.FileField(blank=True,null=True, verbose_name="eklemek isterseniz fotograf seçin ")
    def __str__(self):
        return self.firma_adi
    
class Summary (models.Model):
    ozet=  models.TextField(max_length=None)
    def __str__(self):
        return "Açıklama Bölümü"

class KisiselBilgiler(models.Model):
    lokasyon=models.TextField(blank=True,null=True, verbose_name="Lokasyon")
    telefon=models.TextField(blank=True,null=True, verbose_name="telefon numarası giriniz")
    eposta=models.TextField(blank=True,null=True, verbose_name="E-posta yı giriniz")
    def __str__(self):
        return "Kisisel Bilgiler"

class projeler(models.Model):
    proje_ismi=models.TextField(verbose_name="proje ismi")
    platform = models.TextField(verbose_name="Platform")
    acıklama=RichTextField(verbose_name="Platform")
    def __str__(self):
        return self.proje_ismi

class badget(models.Model):
    badget=models.TextField(verbose_name="Badget İsmi")
    def __str__(self):
        return self.badget
class ozellikler(models.Model):
    baslik=models.TextField(verbose_name="proje ismi")
    aciklama=RichTextField()
    def __str__(self):
        return self.baslik
    
