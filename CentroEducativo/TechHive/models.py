
import re
from typing import Required
from django.db import models
from django import forms
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
ValidacionNumeros = RegexValidator(r'^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$',"No se puede ingresar números a este campo.")
ValidacionLetras = RegexValidator(r'^[0-9 ]*$',"No se puede ingresar letras a este campo.")
ValidacionTelefono = RegexValidator(r'^[[2,3,7,8,9]{1}[0-9]{3}[0-9]{4}]*$',
                         "No puede ingresar letras en este campo, este campo debe comenzar con 2,3,8,9, este campo debe tener 8 a 11 digitos")



from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def no_dos_espacios_validator(value):
    if '  ' in value:
        raise forms.ValidationError('No se permiten dos espacios en blanco seguidos.')

def no_tres_letras_iguales_validator(value):
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise forms.ValidationError('No se permiten tres letras iguales seguidas.')

def no_numeros_validator(value):
    if any(char.isdigit() for char in value):
        raise forms.ValidationError('No se permiten números en este campo.')
    
def no_dos_espacios_validator(value):
    if '  ' in value:
        raise forms.ValidationError('No se permiten dos espacios en blanco seguidos.')

def no_tres_letras_iguales_validator(value):
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise forms.ValidationError('No se permiten tres letras iguales seguidas.')

def no_numeros_validator(value):
    if any(char.isdigit() for char in value):
        raise models.ValidationError('Este campo no debe contener números.')

def no_letras_validator(value):
    if any(char.isalpha() for char in value):
        raise models.ValidationError('Este campo no debe contener letras.')

def no_dos_espacios_validator(value):
    if '  ' in value:
        raise ValidationError('No se permiten dos espacios en blanco seguidos.')

def no_tres_letras_iguales_validator(value):
    for i in range(len(value) - 2):
        if value[i] == value[i+1] == value[i+2]:
            raise ValidationError('No se permiten tres letras iguales seguidas.')

def no_repita_nombre_validator(value):
    if Empleado.objects.filter(NombresEmpleado__iexact=value).exists():
        raise ValidationError('Este nombre ya existe en la base de datos.')

def telefono_validator(value):
    if not value.isdigit():
        raise ValidationError('El teléfono debe contener solo dígitos numéricos.')

    if len(value) != 8:
        raise ValidationError('El teléfono debe tener 8 dígitos.')

    if not value.startswith(('9', '8', '3')):
        raise ValidationError('El teléfono debe iniciar con 9, 8 o 3.')

def dni_validator(value):
    if not value.isdigit():
        raise ValidationError('El DNI debe contener solo dígitos numéricos.')

    if len(value) != 13:
        raise ValidationError('El DNI debe tener 13 dígitos.')

    if Empleado.objects.filter(DPI=value).exists():
        raise ValidationError('Este DNI ya existe en la base de datos.')

def rtn_validator(value):
    if not value.isdigit():
        raise ValidationError('El RTN debe contener solo dígitos numéricos.')

    if len(value) != 14:
        raise ValidationError('El RTN debe tener 14 dígitos.')

def pasaporte_validator(value):
    if not value.isalnum():
        raise ValidationError('El pasaporte debe contener solo caracteres alfanuméricos.')

    if len(value) != 20:
        raise ValidationError('El pasaporte debe tener 20 caracteres.')


class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128, help_text="La contraseña debe tener al menos 8 caracteres y contener al menos un número, una letra mayúscula y una letra minúscula.")
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    intentos_fallidos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'


class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True, unique=True, null=False)
    Departamento = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-ZñÑ áéíóúÁÉÍÓÚ ]*$', "No se puede ingresar números a este campo.")])


    def __str__(self):
        return self.Departamento

class Municipio(models.Model):
    idMunicipio= models.AutoField(primary_key=True, unique=True, null= False)
    nombreMunicipio = models.CharField(max_length=100)
    Departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMunicipio

class TipoSanguineo(models.Model):
    TipoSanguineo = models.CharField(max_length=3)

    def __str__(self):
        return self.TipoSanguineo
    
class DocumentoDPI(models.Model):
    DocumentoDPI = models.CharField(max_length=30)

    def __str__(self):
        return self.DocumentoDPI
    

class HorariosNivelEducativo(models.Model):
    Horario = models.CharField(max_length=15, help_text='No debe contener numeros, caracteres 5-15')
    HoraEntrada = models.TimeField()
    HoraSalida = models.TimeField()

    def __str__(self):
        return f"Horario: {self.Horario} , {self.HoraEntrada} - {self.HoraSalida}"

class NivelEducativo(models.Model):
    NivelEducativo = models.CharField(max_length=20, help_text='No debe contener numeros, caractreres: 5-20 ')
    Horario = models.ForeignKey(HorariosNivelEducativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.NivelEducativo

class Grado(models.Model):
    Grado = models.CharField(max_length=25)
    NivelEducativo = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE)

    def _str_(self):
        return self.Grado

class Seccion(models.Model):
    Seccion = models.CharField(max_length=1)

    def _str_(self):
        return self.Seccion


class TipoPago(models.Model):
    TipoPago = models.CharField(max_length=30)
    PrecioPago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.TipoPago


class Meses(models.Model):
    Meses = models.CharField(max_length=15)

    def __str__(self):
        return self.Meses
    
class Tutor(models.Model):
    NombresTutor = models.CharField(max_length=20,  help_text='No debe contener numeros, caracteres: 3-20 ')
    ApellidosTutor = models.CharField(max_length=30,  help_text='No debe contener numeros, caracteres: 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20,  help_text='No, debe contenes letras, digitos: 13-15 ')
    Tel_Tutor = models.CharField(max_length=8,  help_text='Longitud requerida: 8 digitos ')
    Parentesco = models.CharField(max_length=15, help_text='No debe contener numeros, caracteres 3-15 ')
    

    def __str__(self):
        return f"{self.NombresTutor} {self.ApellidosTutor} {self.Parentesco} "


class Alumno(models.Model):
    

    NombresAlumno = models.CharField(max_length=20, help_text='No debe contener numeros, caracteres: 3-20 ')
    ApellidosAlumno = models.CharField(max_length=30, help_text='No debe contener numeros, caracteres: 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20,  help_text='No, debe contenes letras, digitos: 13-15 ')
    FechaNacimientoAlumno = models.DateField()
    DireccionAlumno = models.CharField(max_length=30, help_text=' No se permiten espacios dobles, Longitud requerida: 5-30 ')
    Departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    Seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    TipoSanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.NombresAlumno} {self.ApellidosAlumno} {self.Grado}"    


class Catedratico(models.Model):
    NombresCatedratico = models.CharField(max_length=20, help_text='No debe contener numeros, caracteres 3-20 ')
    ApellidosCatedratico = models.CharField(max_length=30, help_text='No debe contener numeros, caracteres 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20,  help_text='No, debe contenes letras, digitos: 13-15 ')
    FechaNacimientoCatedratico = models.DateField()
    Tel_Catedratico = models.CharField(max_length=8, help_text='No debe contener letras, 8 digitos' )

    def __str__(self):
        return f"{self.NombresCatedratico} {self.ApellidosCatedratico}"


class CategoriaEmpleado(models.Model):
    CategoriaEmpleado = models.CharField(max_length=30)

    def __str__(self):
        return self.CategoriaEmpleado


class Empleado(models.Model):
    NombresEmpleado = models.CharField(max_length=20, validators=[
        RegexValidator(r'^[^\d]{3,20}$', 'No debe contener números, caracteres: 3-20'),
        no_numeros_validator
    ])
    ApellidosEmpleado = models.CharField(max_length=30, help_text='No debe contener numeros, caracteres 2-30 ')
    DocumentoDPI = models.ForeignKey(DocumentoDPI, on_delete=models.CASCADE)
    DPI = models.CharField(max_length=20,  help_text='No, debe contenes letras, digitos: 13-15 ')
    FechaNacimientoEmpleado = models.DateField()
    CategoriaEmpleado = models.ForeignKey(CategoriaEmpleado, on_delete=models.CASCADE)
    Tel_Empleado = models.CharField(max_length=8, help_text='No debe contener letras, 8 digitos ')

    def __str__(self):
        return f"{self.NombresEmpleado} {self.ApellidosEmpleado}"
    
       

class TipoReporte(models.Model):
    TipoReporte = models.CharField(max_length=40)

    def __str__(self):
        return self.TipoReporte


class Asignatura(models.Model):
    Asignatura = models.CharField(max_length=25, help_text='No debe contener numeros, caracteres 5-25 ')
    Catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    NivelEducativo = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE)

    def __str__(self):
        return self.Asignatura


class TutoresAlumnos(models.Model):
    Tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)


    def __str__(self):
        return f"Encargados de {self.Alumno} : {self.Tutor}"


    
class Pagos(models.Model):
    idPago=models.AutoField(primary_key=True)
    Tutor= models.ForeignKey(Tutor, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    FechaPago = models.DateField()
    TipoPago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    Meses= models.ForeignKey(Meses, on_delete=models.CASCADE)
    HoraPago = models.TimeField()  
    
    def __str__(self):
        return f"{self.FechaPago}{self.Meses}"
    
    
class Matricula(models.Model):
    Pagos = models.ForeignKey(Pagos, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    FechaMatricula = models.DateField()

    def __str__(self):
        return f"{self.Pagos} {self.FechaMatricula}"
    
class CentroEducativo(models.Model):
    NombreCentro= models.CharField(max_length=100)
    CodigoCentro = models.IntegerField()
    Titularidad= models.CharField(max_length=100)
    Localidad = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Sucursal = models.CharField(max_length=100)
    Telefono=models.IntegerField()

    def __str__(self):
        return f"{self.NombreCentro}{self.Localidad}{self.Sucursal}{self.Telefono}"

class ParametrosSAR(models.Model):
    CAI = models.CharField(max_length=100)
    RTN = models.IntegerField()
    RangoInicial = models.IntegerField()
    RangoFinal = models.IntegerField()
    FechaEmision = models.DateField()
    FechaVencimiento = models.DateField()
    Correlativo=models.CharField(max_length=100)
    
    def __str__(self):
        return self.CAI

class Facturacion(models.Model):
    NumeroFactura = models.CharField(max_length=20)
    Fecha = models.DateField()
    ParametrosSAR = models.ForeignKey(ParametrosSAR, on_delete=models.CASCADE)
    CentroEducativo = models.CharField(max_length=100)
    Pagos = models.ForeignKey(Pagos, on_delete=models.CASCADE)
    ImporteExonerado = models.DecimalField(max_digits=6, decimal_places=2)
    ImporteExcento = models.DecimalField(max_digits=6, decimal_places=2)
    ImporteGravado15 = models.DecimalField(max_digits=6, decimal_places=2)
    ImporteGravado18 = models.DecimalField(max_digits=6, decimal_places=2)
    ImpuestoSobreVenta15 = models.DecimalField(max_digits=6, decimal_places=2)
    ImpuestoSobreVenta18 = models.DecimalField(max_digits=6, decimal_places=2)
    Total = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.CentroEducativo} {self.ParametrosSAR} {self.NumeroFactura} {self.Pagos} {self.ImporteExonerado} {self.ImporteExcento} {self.ImporteGravado15} {self.ImporteGravado18} {self.ImpuestoSobreVenta15} {self.ImpuestoSobreVenta18} {self.Total}"
    
class Reportes(models.Model):
    TipoReporte = models.ForeignKey(TipoReporte, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    DescripcionReporte = models.CharField(max_length=150, help_text='Longitud requerida: caracteres 6-150 ')
    FechaReporte = models.DateField()
    
    
    def __str__(self):
        return self.TipoReporte
    
class Actitud(models.Model):
    Actitud = models.CharField(max_length=15)

    def __str__(self):
        return self.Actitud
    
class ExpedienteEscolar(models.Model):
    Actitud = models.ForeignKey(Actitud, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    InstitutoAnterior = models.CharField(max_length=60)
    PromedioAnualAnterior=models.IntegerField()
    Tutor= models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Alumno

class ExpedienteMedico(models.Model):
    Grado = models.ForeignKey(Grado,  on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    EnfermedadCronica1 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres')
    EnfermedadCronica2 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    EnfermedadCronica3 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    MedicamentoUsoDiario1 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    MedicamentoUsoDiario2 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    Alergia1 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    Alergia2 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
    Alergia3 = models.CharField(max_length=20, help_text='Longitud requerida: 3-30 caracteres ')
  
    
    def __str__(self):
        return f"{self.Alumno}{self.Tutor}"

class ParcialesAcademicos(models.Model):
    ParcialAcademico = models.CharField(max_length=20, help_text='Longitud requerida: 5-20 caracteres ')
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    Año= models.DateField()

    def __str__(self):
        return f"{self.ParcialAcademico}, {self.Año}"
    
class NotasAlumnos(models.Model):
    Asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    ParcialAcademico = models.ForeignKey(ParcialesAcademicos, on_delete=models.CASCADE)
    ApellidosAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    NotaAcumulativo= models.DecimalField(max_digits=4, decimal_places=2,  help_text='Maximo valor para Nota de Acumulativo: 2 caracteres, 70.00 ')
    NotaExamen = models.DecimalField(max_digits=4, decimal_places=2,   help_text='Maximo valor para Nota de Examen 2 caracteres, 30.00 ')
    NotaFinal= models.DecimalField(max_digits=4, decimal_places=2,   help_text='Maximo valor para Nota final 2 caracteres, 100.00 ')
    PromedioClase= models.DecimalField(max_digits=4,  decimal_places=2,  help_text='Maximo valor para promedio de clase 2 caracteres, 100.00 ')


    def __str__(self):
        return f"{self.ApellidosAlumno},{self.NotaFinal}"

