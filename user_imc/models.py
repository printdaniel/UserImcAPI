from django.db import models

# Create your models here.
class Usuarios(models.Model):
    username = models.CharField(max_length=100)
    altura = models.FloatField()
    peso = models.FloatField()
    imc = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=[
            ('bajo', 'Bajo Peso'),
            ('normal', 'Peso Normal'),
            ('sobrepeso', 'Sobrepeso')
        ], blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcular el IMC 
        if self.altura and self.peso:
            self.imc = self.peso/(self.altura ** 2)
            self.estado = self.get_estado_imc()
            
        else:
            self.imc = None
            self.estado = None

        super(Usuarios, self).save(*args, **kwargs)

    def get_estado_imc(self):
        if self.imc < 18.5:
            self.estado = 'bajo'
        elif 18.5 <= self.imc < 25:
            self.estado = 'normal'
        else:
            self.estado = 'sobrepeso'
