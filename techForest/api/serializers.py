from rest_framework import serializers
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'nombres', 'apellidos', 'correo', 'contraseña', 'imagen_perfil')

    def create(self, validated_data):
        """
        Create and return a new `Usuarios` instance, given the validated data.
        """
        return Usuarios.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Usuarios` instance, given the validated data.
        """
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.contraseña = validated_data.get('contraseña', instance.contraseña)
        instance.imagen_perfil = validated_data.get('imagen_perfil', instance.imagen_perfil)
        instance.save()
        return instance

class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = ('id', 'plan', 'tipo', 'usuario_id')

    def create(self, validated_data):
        """
        Create and return a new `Planes` instance, given the validated data.
        """
        return Planes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Planes` instance, given the validated data.
        """
        instance.plan = validated_data.get('plan', instance.plan)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.usuario_id = validated_data.get('usuario_id', instance.usuario_id)
        instance.save()
        return instance

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = ('id', 'boleta', 'costo', 'fecha_pago', 'planes_id')

    def create(self, validated_data):
        """
        Create and return a new `Pagos` instance, given the validated data.
        """
        return Pagos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Pagos` instance, given the validated data.
        """
        instance.boleta = validated_data.get('boleta', instance.boleta)
        instance.costo = validated_data.get('costo', instance.costo)
        instance.fecha_pago = validated_data.get('fecha_pago', instance.fecha_pago)
        instance.planes_id = validated_data.get('planes_id', instance.planes_id)
        instance.save()
        return instance
    
class ErroresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errores
        fields = ('id', 'titulo', 'mensaje', 'fecha_envio', 'usuario_id')

    def create(self, validated_data):
        """
        Create and return a new `Errores` instance, given the validated data.
        """
        return Errores.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Errores` instance, given the validated data.
        """
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.mensaje = validated_data.get('mensaje', instance.mensaje)
        instance.fecha_envio = validated_data.get('fecha_envio', instance.fecha_envio)
        instance.usuario_id = validated_data.get('usuario_id', instance.usuario_id)
        instance.save()
        return instance

class DiapositivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diapositivos
        fields = ('id', 'nombre', 'estado', 'fecha_adquisicion', 'imagen', 'usuario_id')

    def create(self, validated_data):
        """
        Create and return a new `Diapositivos` instance, given the validated data.
        """
        return Diapositivos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Diapositivos` instance, given the validated data.
        """
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.fecha_adquisicion = validated_data.get('fecha_adquisicion', instance.fecha_adquisicion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.usuario_id = validated_data.get('usuario_id', instance.usuario_id)
        instance.save()
        return instance

class ValvulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valvula
        fields = ('id', 'estado', 'diapositivos_id')

    def create(self, validated_data):
        """
        Create and return a new `Valvula` instance, given the validated data.
        """
        return Valvula.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Valvula` instance, given the validated data.
        """
        instance.estado = validated_data.get('estado', instance.estado)
        instance.diapositivos_id = validated_data.get('diapositivos_id', instance.diapositivos_id)
        instance.save()
        return instance

class OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = ('id', 'valor_maximo', 'valor_minimo', 'humedad', 'fecha_adquisicion','diapositivos_id')

    def create(self, validated_data):
        """
        Create and return a new `Opciones` instance, given the validated data.
        """
        return Opciones.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Opciones` instance, given the validated data.
        """
        instance.valor_maximo = validated_data.get('valor_maximo', instance.valor_maximo)
        instance.valor_minimo = validated_data.get('valor_minimo', instance.valor_minimo)
        instance.humedad = validated_data.get('humedad', instance.humedad)
        instance.fecha_adquisicion = validated_data.get('fecha_adquisicion', instance.fecha_adquisicion)
        instance.diapositivos_id = validated_data.get('diapositivos_id', instance.diapositivos_id)
        instance.save()
        return instance

class AdministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradores
        fields = ('id', 'nombres', 'apellidos', 'correo', 'contraseña', 'imagen_perfil')

    def create(self, validated_data):
        """
        Create and return a new `Administradores` instance, given the validated data.
        """
        return Administradores.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Administradores` instance, given the validated data.
        """
        instance.nombres = validated_data.get('nombres', instance.nombres)
        instance.apellidos = validated_data.get('apellidos', instance.apellidos)
        instance.correo = validated_data.get('correo', instance.correo)
        instance.contraseña = validated_data.get('contraseña', instance.contraseña)
        instance.imagen_perfil = validated_data.get('imagen_perfil', instance.imagen_perfil)
        instance.save()
        return instance