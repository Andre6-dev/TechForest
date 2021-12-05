from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=200)
    imagen_perfil = models.ImageField(upload_to='usuarios',blank=True,null=True)

    def __str__(self):
        return self.nombres

class Planes(models.Model):
    DOMESTICO = 'domestico'
    EMPRESARIAL = 'empresarial'

    PLANES_CHOICES = (
        (DOMESTICO, 'Domestico'),
        (EMPRESARIAL, 'Empresarial'),
    )

    plan = models.CharField(max_length=200, default="0")
    tipo = models.CharField(max_length=100, choices=PLANES_CHOICES)
    usuario_id = models.OneToOneField(Usuarios, on_delete=models.CASCADE, default="0")

    def __str__(self):
        return self.plan

class Pagos(models.Model):
    boleta = models.CharField(max_length=100, unique=True)
    costo = models.FloatField()
    fecha_pago = models.DateTimeField()
    planes_id = models.ForeignKey(Planes, on_delete=models.CASCADE)

    def __str__(self):
        return self.boleta

class Errores(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField()
    usuario_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Diapositivos(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_adquisicion = models.DateTimeField()
    imagen = models.ImageField(upload_to='diapositivos',blank=True,null=True)
    usuario_id = models.OneToOneField(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Valvula(models.Model):
    class Estados(models.IntegerChoices):
        Activo = 1
        Inactivo = 2

    estado = models.IntegerField(choices=Estados.choices)
    diapositivos_id = models.OneToOneField(Diapositivos, on_delete=models.CASCADE)

class Opciones(models.Model):
    valor_maximo = models.CharField(max_length=200)
    valor_minimo = models.CharField(max_length=200)
    humedad = models.CharField(max_length=200)
    fecha_adquisicion = models.DateTimeField()
    diapositivos_id = models.OneToOneField(Diapositivos, on_delete=models.CASCADE)

class Administradores(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=200)
    imagen_perfil = models.ImageField(upload_to='usuarios',blank=True,null=True)

    def __str__(self):
        return self.nombres