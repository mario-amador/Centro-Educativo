import re
from django import forms
from django.forms import Select, DateInput
from .models import Usuario ,Alumno,Empleado,Catedratico, ExpedienteEscolar, Grado, Municipio,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Departamento, ParametrosSAR, Pagos, Meses, CategoriaEmpleado, DocumentoDPI, Facturacion
from datetime import datetime 
import re
from django import forms


from django.core.exceptions import ValidationError



def password_validator(password):
    # Verificar si la contraseña tiene al menos 8 caracteres
    if len(password) < 8:
        raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
    
    # Verificar si la contraseña contiene al menos un número
    if not any(char.isdigit() for char in password):
        raise ValidationError("La contraseña debe contener al menos un número.")
    
    # Verificar si la contraseña contiene al menos una letra en mayúscula
    if not any(char.isupper() for char in password):
        raise ValidationError("La contraseña debe contener al menos una letra en mayúscula.")
    
    # Verificar si la contraseña contiene al menos una letra en minúscula
    if not any(char.islower() for char in password):
        raise ValidationError("La contraseña debe contener al menos una letra en minúscula.")

def no_numeros_ni_especiales_validator(value):
    if re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', value):
        raise forms.ValidationError('El campo no adminite caracteres especiales.')

def dni_longitud_validator(value):
    if not value.isdigit() or len(value) != 13:
        raise forms.ValidationError('El DNI debe contener solo números y tener exactamente 13 dígitos.')
    return value

def rtn_longitud_validator(value):
    if len(value) != 14:
        raise forms.ValidationError('El RTN debe contener exactamente 14 dígitos numéricos.')

def pasaporte_longitud_validator(value):
    if len(value) != 20:
        raise forms.ValidationError('El pasaporte debe contener exactamente 20 caracteres alfanuméricos.')



def no_campos_vacios_validator(value):
    if not value.strip():
        raise forms.ValidationError('Este campo no puede estar vacío.')


def no_letras_ni_numeros_ni_especiales_validator(value):
    if re.search(r'[a-zA-Z\d!@#$%^&*(),.?":{}|<>]', value):
        raise forms.ValidationError('El campo no debe contener letras, números o caracteres especiales al mismo tiempo.')




def telefono_validator(value):
    if not value.isdigit():
        raise forms.ValidationError('El teléfono debe contener solo dígitos numéricos.')

    if len(value) != 8:
        raise forms.ValidationError('El teléfono debe tener 8 dígitos.')

    if not value.startswith(('9', '8', '3')):
        raise forms.ValidationError('El número de teléfono debe tener 8 dígitos y comenzar con 9, 8 o 3.')

def fecha_rango_validator(value):
    min_fecha = datetime.strptime('1974-01-01', '%Y-%m-%d').date()
    max_fecha = datetime.strptime('2004-01-01', '%Y-%m-%d').date()

    if value < min_fecha or value > max_fecha:
        raise forms.ValidationError(' Tienes que ser mayor a 18 Años.')


def solo_letras_validator(value):
    if not re.match(r'^[a-zA-Z ]*$', value):
        raise forms.ValidationError('El campo solo puede contener letras y un solo espacio.')


def solo_letras_y_un_espacio_validator(value):
    if not re.match(r'^[a-zA-Z]+( [a-zA-Z]+)?$', value):
        raise forms.ValidationError('El campo solo puede contener letras y un solo espacio.')

def no_letras_ni_numeros_ni_especiales_validator(value):
    if re.search(r'[a-zA-Z\d!@#$%^&*(),.?":{}|<>]', value):
        raise forms.ValidationError('El campo no debe contener letras, números o caracteres especiales al mismo tiempo.')
    
def no_campos_vacios_validator(value):
    if not value.strip():
        raise forms.ValidationError('Este campo no puede estar vacío.')
    
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

    


from .models import Alumno,Empleado,Catedratico,TipoSanguineo,TipoReporte,TipoPago, ExpedienteEscolar, Grado, Municipio,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos, Departamento, ParametrosSAR, Pagos, Meses, CategoriaEmpleado, DocumentoDPI
class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ['NombresAlumno', 'ApellidosAlumno', 'DocumentoDPI', 'DPI', 'FechaNacimientoAlumno', 'DireccionAlumno', 'Departamento', 'Municipio', 'Grado', 'Seccion', 'TipoSanguineo']
        labels = {
            'NombresAlumno': 'Nombres del Alumno:',
            'ApellidosAlumno': 'Apellidos del Alumno',
            'DocumentoDPI': 'Tipo de Documento',
            'DPI': 'Documento',
            'FechaNacimientoAlumno': 'Fecha de Nacimiento del Alumno',
            'DireccionAlumno': 'Dirección del Alumno',
            'Departamento': 'Departamento nativo',
            'Municipio': 'Municipio nativo',
            'Grado': 'Grado al que aspira',
            'Seccion': 'Sección',
            'TipoSanguineo': 'Tipo de Sangre del Alumno',
        }
        widgets = {
            'NombresAlumno': forms.TextInput(
                attrs={'class': 'form-control'}),
            'ApellidosAlumno': forms.TextInput(
                attrs={'class': 'form-control'}),
            'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'DPI': forms.TextInput(
                attrs={'class': 'form-control'}),
            'FechaNacimientoAlumno': forms.DateInput(
                attrs={'class': 'form-control', 
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date',
                       'min': '1974-01-01',
                       'max': '2019-01-01'}),
            'DireccionAlumno': forms.TextInput(
    attrs={
        'class': 'form-control',
        'required': 'required',
        'id': 'DireccionAlumno',
        'type': 'text',
        'min_length': '4',
        'max_length': '30',
        'pattern': '^(?!.*\s{2}).*$'  # Expresión regular para no permitir dos espacios en blanco consecutivos
    }
),


            'Departamento': forms.Select(
                attrs={'class': 'form-control'}),
            'Grado': forms.Select(
                attrs={'class': 'form-control'}),
            'Seccion': forms.Select(
                attrs={'class': 'form-control'}),
            'TipoSanguineo': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def _init_(self, *args, **kwargs):
      super()._init_(*args, **kwargs)
      self.fields['Municipio'].queryset = Municipio.objects.none()

    def clean_DPI(self):
        dpi = self.cleaned_data.get('DPI')
        documento_dpi = self.cleaned_data.get('DocumentoDPI')

        if documento_dpi == 'DNI' and len(dpi) != 13:
            raise forms.ValidationError('El DNI debe tener 13 dígitos.')

        if documento_dpi == 'RTN' and len(dpi) != 14:
            raise forms.ValidationError('El RTN debe tener 14 dígitos.')

        return dpi

    
    def clean_NombresAlumno(self):
        nombres_alumno = self.cleaned_data.get('NombresAlumno')

        if any(char.isdigit() for char in nombres_alumno):
            raise forms.ValidationError('El nombre no debe contener números.')

        if len(nombres_alumno) < 3 or len(nombres_alumno) > 20:
            raise forms.ValidationError('La longitud del nombre debe ser entre 3 y 20 caracteres.')

        if re.search(r'(\w)\1', nombres_alumno):
            raise forms.ValidationError('El nombre no puede contener letras repetidas.')

        if '  ' in nombres_alumno:
            raise forms.ValidationError('El nombre no puede contener espacios dobles.')

        return nombres_alumno.capitalize()

    def clean_ApellidosAlumno(self):
        apellidos_alumno = self.cleaned_data.get('ApellidosAlumno')

        if any(char.isdigit() for char in apellidos_alumno):
            raise forms.ValidationError('Los apellidos no deben contener números.')

        if len(apellidos_alumno) < 2 or len(apellidos_alumno) > 30:
            raise forms.ValidationError('La longitud de los apellidos debe ser entre 2 y 30 caracteres.')

        if re.search(r'(\w)\1', apellidos_alumno):
            raise forms.ValidationError('Los apellidos no pueden contener letras repetidas.')

        if '  ' in apellidos_alumno:
            raise forms.ValidationError('Los apellidos no pueden contener espacios dobles.')

        return apellidos_alumno.capitalize()


        

    
   
    
#Validaciones especificas

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['NombresEmpleado', 'ApellidosEmpleado', 'DocumentoDPI', 'DPI', 'FechaNacimientoEmpleado', 'CategoriaEmpleado', 'Tel_Empleado']
        labels = {
            'NombresEmpleado': 'Nombres del Empleado',
            'ApellidosEmpleado': 'Apellidos del Empleado',
            'DocumentoDPI': 'Tipo de Documento',
            'DPI': 'Documento',
            'FechaNacimientoEmpleado': 'Fecha de Nacimiento del Empleado',
            'CategoriaEmpleado': 'Categoría del Empleado',
            'Tel_Empleado': 'Teléfono del Empleado',
        }
        widgets = {
            'NombresEmpleado': forms.TextInput(
                attrs={'class': 'form-control',
                       'Required':'Required',
                       'id':'NombresEmpleado',
                       'Type':'text',
                       'min_length':'3',
                       'max_length':'10' ,
                       'pattern':'[a-zA-Z].{2,20}' }),
            'ApellidosEmpleado': forms.TextInput(
                attrs={'class': 'form-control',
                       'Required':'Required',
                       'id':'ApellidosEmpleado',
                       'Type':'text',
                       'min_length':'1',
                       'max_length':'40' ,
                       'pattern':'[a-zA-Z].{3,30}', }),
           'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'DPI': forms.TextInput(
                attrs={'class': 'form-control'}),
            'FechaNacimientoEmpleado': forms.DateInput(
                attrs={'class': 'form-control', 
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date',
                       }),
            'CategoriaEmpleado': forms.Select(
                attrs={'class': 'form-control'}),
            'Tel_Empleado': forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': '########',
               'title': 'El número de teléfono debe tener 8 dígitos y comenzar con 9, 8 o 3.'}),
        }

    


    def clean_Tel_Empleado(self):
        telefono_empleado = self.cleaned_data['Tel_Empleado']
        telefono_validator(telefono_empleado)
        return telefono_empleado



    def clean_FechaNacimientoEmpleado(self):
        fecha_nacimiento = self.cleaned_data.get('FechaNacimientoEmpleado')
        fecha_rango_validator(fecha_nacimiento)
        return fecha_nacimiento
    

    
    def clean_NombresEmpleado(self):
        nombres_empleado = self.cleaned_data.get('NombresEmpleado')
        solo_letras_validator(nombres_empleado)
        no_campos_vacios_validator(nombres_empleado)
        no_dos_espacios_validator(nombres_empleado)
        no_numeros_validator(nombres_empleado)
        no_tres_letras_iguales_validator(nombres_empleado)
        return nombres_empleado.capitalize()
    
    def clean_ApellidosEmpleado(self):
        nombres_empleado = self.cleaned_data.get('ApellidosEmpleado')
        solo_letras_validator(nombres_empleado)
        no_campos_vacios_validator(nombres_empleado)
        no_dos_espacios_validator(nombres_empleado)
        no_numeros_validator(nombres_empleado)
        no_tres_letras_iguales_validator(nombres_empleado)
        return nombres_empleado.capitalize()
    

    def clean_DPI(self):
        documento_dpi = self.cleaned_data.get('DocumentoDPI')
        dpi = self.cleaned_data.get('DPI')

        if documento_dpi == 'DNI':
            if not dpi.isdigit() or len(dpi) != 13:
                raise forms.ValidationError('El DNI debe contener solo números y tener exactamente 13 dígitos.')
        elif documento_dpi == 'RTN':
            if not dpi.isdigit() or len(dpi) != 14:
                raise forms.ValidationError('El RTN debe contener solo números y tener exactamente 14 dígitos.')
        elif documento_dpi == 'Pasaporte':
            if len(dpi) != 20 or not dpi.isalnum():
                raise forms.ValidationError('El pasaporte debe contener 20 caracteres alfanuméricos.')
        else:
            raise forms.ValidationError('Tipo de documento no válido.')

        return dpi


class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = ['NombresCatedratico', 'ApellidosCatedratico', 'DocumentoDPI', 'DPI', 'FechaNacimientoCatedratico', 'Tel_Catedratico']
        labels = {
            'NombresCatedratico': 'Nombres del Catedrático',
            'ApellidosCatedratico': 'Apellidos del Catedrático',
            'DocumentoDPI': 'Tipo de Documento',
            'DPI': 'Documento',
            'FechaNacimientoCatedratico': 'Fecha de Nacimiento del Catedrático',
            'Tel_Catedratico': 'Teléfono del Catedrático',
        }
        widgets = {
            
            'NombresCatedratico': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'ApellidosCatedratico': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{3,30}',}),
            'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'DPI': forms.TextInput(
                attrs={'class': 'form-control',
                       'Type':'number',
                       'pattern':'[0,9].{12,15}'}),
            'FechaNacimientoCatedratico': forms.DateInput(
                attrs={'class': 'form-control', 
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date',}),
            'Tel_Catedratico': forms.TextInput(
                attrs={'class': 'form-control',
                    'placeholder': '########'}),

        }

    def clean_Tel_Catedratico(self):
        telefono_catedratico = self.cleaned_data['Tel_Catedratico']
        telefono_validator(telefono_catedratico)
        return telefono_catedratico

    def clean_FechaNacimientoCatedratico(self):
        fecha_nacimiento = self.cleaned_data.get('FechaNacimientoCatedratico')
        fecha_rango_validator(fecha_nacimiento)
        return fecha_nacimiento
    
    def clean_NombresCatedratico(self):
        nombres_catedratico = self.cleaned_data.get('NombresCatedratico')
        solo_letras_validator(nombres_catedratico)
        no_campos_vacios_validator(nombres_catedratico)
        no_dos_espacios_validator(nombres_catedratico)
        no_numeros_validator(nombres_catedratico)
        no_tres_letras_iguales_validator(nombres_catedratico)
        return nombres_catedratico.capitalize()
    
    def clean_ApellidosCatedratico(self):
        apellidos_catedratico = self.cleaned_data.get('ApellidosCatedratico')
        solo_letras_validator(apellidos_catedratico)
        no_campos_vacios_validator(apellidos_catedratico)
        no_dos_espacios_validator(apellidos_catedratico)
        no_numeros_validator(apellidos_catedratico)
        no_tres_letras_iguales_validator(apellidos_catedratico)
        return apellidos_catedratico.capitalize()




class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['NombresTutor', 'ApellidosTutor', 'DocumentoDPI', 'DPI', 'Tel_Tutor', 'Parentesco']
        labels = {
            'NombresTutor': 'Nombres del Tutor',
            'ApellidosTutor': 'Apellidos del Tutor',
            'DocumentoDPI': 'Tipo de Documento',
            'DPI': 'Documento',
            'Tel_Tutor': 'Teléfono del Tutor',
            'Parentesco': 'Parentesco',
        }
        widgets = {
            'NombresTutor': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'ApellidosTutor': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{3,30}',}),
            'DocumentoDPI': forms.Select(
                attrs={'class': 'form-control'}),
            'DPI': forms.TextInput(
                attrs={'class': 'form-control',
                       'Type':'Number',
                       'pattern':'[0,9].{12,15}'}),
            'Tel_Tutor': forms.TextInput(
                attrs={'class': 'form-control',
                
                    'placeholder': '########'}),
            'Parentesco': forms.TextInput(
                attrs={'class': 'form-control',
                       }),
        }

    def clean_NombresTutor(self):
        nombres_tutor = self.cleaned_data.get('NombresTutor')
        solo_letras_validator(nombres_tutor)
        no_campos_vacios_validator(nombres_tutor)
        no_tres_letras_iguales_validator(nombres_tutor)
        return nombres_tutor.capitalize()

    def clean_ApellidosTutor(self):
        apellidos_tutor = self.cleaned_data.get('ApellidosTutor')
        solo_letras_validator(apellidos_tutor)
        no_campos_vacios_validator(apellidos_tutor)
        no_tres_letras_iguales_validator(apellidos_tutor)
        return apellidos_tutor

    def clean_Tel_Tutor(self):
        telefono_tutor = self.cleaned_data.get('Tel_Tutor')
        telefono_validator(telefono_tutor)
        return telefono_tutor



    def clean_Parentesco(self):
        parentesco = self.cleaned_data.get('Parentesco')
        solo_letras_validator(parentesco)
        no_campos_vacios_validator(parentesco)
        no_tres_letras_iguales_validator(parentesco)
        return parentesco.capitalize()

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['Asignatura', 'Catedratico', 'NivelEducativo']
        labels = {
            'Asignatura': 'Nombre de la Asignatura',
            'Catedratico': 'Nombre del Catedratico',
            'NivelEducativo': 'Nivel Educativo',
        }
        widgets = {
            'Asignatura': forms.TextInput(
                attrs={'class': 'form-control',
                       
                       'pattern':'[a-zA-Z].{4,25}',}),
            'Catedratico': forms.Select(
                attrs={'class': 'form-control'}),
            'NivelEducativo': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_Asignatura(self):
        asignatura = self.cleaned_data.get('Asignatura')
        solo_letras_validator(asignatura)
        no_campos_vacios_validator(asignatura)
        no_dos_espacios_validator(asignatura)
        no_numeros_validator(asignatura)
        no_tres_letras_iguales_validator(asignatura)
        return asignatura.capitalize()

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['Pagos', 'Usuario', 'FechaMatricula']
        labels = {
            'Pagos': 'Pagos',
            'Usuario': 'Nombre del Usuario',
            'FechaMatricula': 'Fecha de la Matrícula',
        }
        widgets = {
            'Pagos': forms.Select(
                attrs={'class': 'form-control'}),
            'Usuario': forms.Select(
                attrs={'class': 'form-control'}),
            'FechaMatricula': forms.DateInput(
                attrs={'class': 'form-control', 
                       'placeholder': 'YYYY-MM-DD',
                        'type': 'date'}),
        }

class ReportesForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['TipoReporte', 'Alumno', 'DescripcionReporte', 'FechaReporte']
        labels = {
            'TipoReporte': 'Tipos de Reportes',
            'Alumno': 'Nombre del Alumno',
            'DescripcionReporte': 'Descripción del Reporte',
            'FechaReporte': 'Fecha del Reporte',
        }
        widgets = {
            'TipoReporte': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'DescripcionReporte': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{5,150}'}),
            'FechaReporte': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
        }

    def clean_FechaReporte(self):
        fecha_reporte = self.cleaned_data.get('FechaReporte')
        fecha_rango_validator(fecha_reporte)
        return fecha_reporte
    
    def clean_DescripcionReporte(self):
        descripcion_reporte = self.cleaned_data.get('DescripcionReporte')
        solo_letras_validator(descripcion_reporte)
        no_campos_vacios_validator(descripcion_reporte)
        no_dos_espacios_validator(descripcion_reporte)
        no_numeros_validator(descripcion_reporte)
        no_tres_letras_iguales_validator(descripcion_reporte)
        return descripcion_reporte.capitalize()
    
    def clean_TipoReporte(self):
        tipo_reporte = self.cleaned_data.get('TipoReporte')
        solo_letras_validator(tipo_reporte)
        no_campos_vacios_validator(tipo_reporte)
        no_dos_espacios_validator(tipo_reporte)
        no_numeros_validator(tipo_reporte)
        no_tres_letras_iguales_validator(tipo_reporte)
        return tipo_reporte.capitalize()
    
class ExpedienteMedicoForm(forms.ModelForm):
    class Meta:
        model = ExpedienteMedico
        fields = ['Grado', 'Alumno', 'Tutor', 'EnfermedadCronica1', 'EnfermedadCronica2', 'EnfermedadCronica3', 'MedicamentoUsoDiario1', 'MedicamentoUsoDiario2', 'Alergia1', 'Alergia2', 'Alergia3']
        labels = {
            'Grado': 'Grado',
            'Alumno': 'Nombre del Alumno',
            'Tutor': 'Nombre del Tutor',
            'EnfermedadCronica1': 'Nombre de la Enfermedad Cronica1',
            'EnfermedadCronica2': 'Nombre de la Enfermedad Cronica2',
            'EnfermedadCronica3': 'Nombre de la Enfermedad Cronica3',
            'MedicamentoUsoDiario1': 'Nombre del Medicamento Uso Diario1',
            'MedicamentoUsoDiario2': 'Nombre del Medicamento Uso Diario2',
            'Alergia1': 'Nombre de la Alergia1',
            'Alergia2': 'Nombre de la Alergia2',
            'Alergia3': 'Nombre de la Alergia3',
            
        }
        widgets = {
            'Grado': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'Tutor': forms.Select(
                attrs={'class': 'form-control'}),
            'EnfermedadCronica1': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'EnfermedadCronica2': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'EnfermedadCronica3': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'MedicamentoUsoDiario1': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'MedicamentoUsoDiario2': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'Alergia1': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'Alergia2': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
            'Alergia3': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,20}',}),
        }

    def clean_EnfermedadCronica1(self):
        enfermedad_cronica1 = self.cleaned_data.get('EnfermedadCronica3')
        solo_letras_validator(enfermedad_cronica1)
        no_campos_vacios_validator(enfermedad_cronica1)
        no_dos_espacios_validator(enfermedad_cronica1)
        no_numeros_validator(enfermedad_cronica1)
        no_tres_letras_iguales_validator(enfermedad_cronica1)
        return enfermedad_cronica1.capitalize()
    
    def clean_EnfermedadCronica2(self):
        enfermedad_cronica2 = self.cleaned_data.get('EnfermedadCronica3')
        solo_letras_validator(enfermedad_cronica2)
        no_campos_vacios_validator(enfermedad_cronica2)
        no_dos_espacios_validator(enfermedad_cronica2)
        no_numeros_validator(enfermedad_cronica2)
        no_tres_letras_iguales_validator(enfermedad_cronica2)
        return enfermedad_cronica2.capitalize()
    
    def clean_EnfermedadCronica3(self):
        enfermedad_cronica3 = self.cleaned_data.get('EnfermedadCronica3')
        solo_letras_validator(enfermedad_cronica3)
        no_campos_vacios_validator(enfermedad_cronica3)
        no_dos_espacios_validator(enfermedad_cronica3)
        no_numeros_validator(enfermedad_cronica3)
        no_tres_letras_iguales_validator(enfermedad_cronica3)
        return enfermedad_cronica3.capitalize()
    
    def clean_MedicamentoUsoDiario1(self):
        medicamento_uso_diario1 = self.cleaned_data.get('MedicamentoUsoDiario1')
        solo_letras_validator(medicamento_uso_diario1)
        no_campos_vacios_validator(medicamento_uso_diario1)
        no_dos_espacios_validator(medicamento_uso_diario1)
        no_numeros_validator(medicamento_uso_diario1)
        no_tres_letras_iguales_validator(medicamento_uso_diario1)
        return medicamento_uso_diario1.capitalize()
    
    def clean_MedicamentoUsoDiario2(self):
        medicamento_uso_diario2 = self.cleaned_data.get('MedicamentoUsoDiario2')
        solo_letras_validator(medicamento_uso_diario2)
        no_campos_vacios_validator(medicamento_uso_diario2)
        no_dos_espacios_validator(medicamento_uso_diario2)
        no_numeros_validator(medicamento_uso_diario2)
        no_tres_letras_iguales_validator(medicamento_uso_diario2)
        return medicamento_uso_diario2.capitalize()
    
    def clean_Alergia1(self):
        alergia1 = self.cleaned_data.get('Alergia1')
        solo_letras_validator(alergia1)
        no_campos_vacios_validator(alergia1)
        no_dos_espacios_validator(alergia1)
        no_numeros_validator(alergia1)
        no_tres_letras_iguales_validator(alergia1)
        return alergia1.capitalize()
    
    def clean_Alergia2(self):
        alergia2 = self.cleaned_data.get('Alergia2')
        solo_letras_validator(alergia2)
        no_campos_vacios_validator(alergia2)
        no_dos_espacios_validator(alergia2)
        no_numeros_validator(alergia2)
        no_tres_letras_iguales_validator(alergia2)
        return alergia2.capitalize()
    
    def clean_Alergia3(self):
        alergia3 = self.cleaned_data.get('Alergia3')
        solo_letras_validator(alergia3)
        no_campos_vacios_validator(alergia3)
        no_dos_espacios_validator(alergia3)
        no_numeros_validator(alergia3)
        no_tres_letras_iguales_validator(alergia3)
        return alergia3.capitalize()

class HorariosForm(forms.ModelForm):
    class Meta:
        model = HorariosNivelEducativo
        fields = ['Horario', 'HoraEntrada', 'HoraSalida']
        labels = {
            'Horario': 'Horario',
            'HoraEntrada': 'Hora de entrada',
            'HoraSalida': 'Hora de salida',
        }
        widgets = {
            'Horario': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{4,15}',}),
            'HoraEntrada': forms.TimeInput(
                attrs={'class': 'form-control'}),
            'HoraSalida': forms.TimeInput(
                attrs={'class': 'form-control'}),
        }

class NivelesForm(forms.ModelForm):
    class Meta:
        model = NivelEducativo
        fields = ['NivelEducativo', 'Horario']
        labels = {
            'NivelEducativo': 'Nivel Educativo',
            'Horario': 'Horario',
        }
        widgets = {
            'NivelEducativo': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{4,20}',}),
            'Horario': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_NivelEducativo(self):
        nivel_educativo = self.cleaned_data.get('NivelEducativo')
        solo_letras_validator(nivel_educativo)
        no_campos_vacios_validator(nivel_educativo)
        no_dos_espacios_validator(nivel_educativo)
        no_numeros_validator(nivel_educativo)
        no_tres_letras_iguales_validator(nivel_educativo)
        no_numeros_ni_especiales_validator(nivel_educativo)
        return nivel_educativo.capitalize()

class ParcialesForm(forms.ModelForm):
    class Meta:
        model = ParcialesAcademicos
        fields = ['ParcialAcademico', 'FechaInicio', 'FechaFinal', 'Año']
        labels = {
            'ParcialAcademico': 'Parcial Academico',
            'FechaInicio': 'Fecha de inicio del parcial',
            'FechaFinal': 'Fecha final del parcial',
            'Año':'Año',
        }
        widgets = {
            'ParcialAcademico': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{4,20}',}),
            'FechaInicio': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'FechaFinal': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'Año': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY', 
                       'type': 'date'}),
        }

class NotasForm(forms.ModelForm):
    class Meta:
        model = NotasAlumnos
        fields = ['Asignatura', 'ParcialAcademico', 'ApellidosAlumno',  'NotaAcumulativo', 'NotaExamen', 'NotaFinal', 'PromedioClase']
        labels = {
            'Asignatura': 'Asignatura', 
            'ParcialAcademico':'Parcial', 
            'ApellidosAlumno':'Apellidos del Alumno', 
            'NotaAcumulativo': 'Nota de Acumulativo', 
            'NotaExamen': 'Nota de Examen', 
            'NotaFinal':'Nota final',
            'PromedioClase':'Promedio de clase'
        }
        widgets = {
             'Asignatura': forms.Select(
                attrs={'class': 'form-control'}),
        
            'ParcialAcademico': forms.Select(
                attrs={'class': 'form-control'}),
            'ApellidosAlumno': forms.Select(
                attrs={'class': 'form-control'}),
            'NotaAcumulativo': forms.NumberInput(
                attrs={'class': 'form-control',
                       'min': '00,00',
                       'max':'70,00',
                       'step':'.1'}),
            'NotaExamen': forms.NumberInput(
                attrs={'class': 'form-control',
                       'min': '00,00',
                       'max':'30,00',
                       'step':'.1'}),
            'NotaFinal':forms.NumberInput(
                attrs={'class': 'form-control',
                       'min': '00,00',
                       'max':'100,00',
                       'step':'.1'}),
            'PromedioClase':forms.NumberInput(
                attrs={'class': 'form-control',
                       'min': '00,00',
                       'max':'100,00',
                       'step':'.1'}),
              

           }

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', max_length=100)


from django import forms

from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    usuario = forms.CharField(
        label='Usuario',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    contraseña = forms.CharField(
        label='Contraseña',
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')
        contraseña = cleaned_data.get('contraseña')

        if usuario and contraseña:
            user = authenticate(username=usuario, password=contraseña)
            if not user:
                raise forms.ValidationError('Credenciales incorrectas. Por favor, verifique sus datos.')

        return cleaned_data
    

from django import forms
from .models import Usuario

from django import forms
from .models import Usuario

from django import forms


    


from django import forms
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    password = forms.CharField(
        label='contraseña',  # Cambio del atributo label a español
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
       help_text="La contraseña debe tener al menos 8 caracteres y contener al menos un número, una letra mayúscula y una letra minúscula."
    )
    confirm_password = forms.CharField(
        label='Confirmar contraseña',  # Cambio del atributo label a español
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )

    ACTIVO_CHOICES = [
        (True, 'Sí'),
        (False, 'No'),
    ]
    activo = forms.ChoiceField(
        choices=ACTIVO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'confirm_password', 'rol', 'activo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['username'].widget.attrs['readonly'] = True

    def clean_activo(self):
        activo = self.cleaned_data.get('activo')
        if activo == 'True':
            # Si el campo activo se cambia a True, restablecer los intentos fallidos a 0
            self.instance.intentos_fallidos = 0
            self.instance.save()
        return activo

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.')
        return confirm_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password

import re
import re


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )
    ACTIVO_CHOICES = [
        (True, 'Sí'),
        (False, 'No'),
    ]
    activo = forms.ChoiceField(
        choices=ACTIVO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'confirm_password', 'rol', 'activo']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'
        self.fields['confirm_password'].label = 'Confirmar Contraseña'




    def clean_username(self):
            username = self.cleaned_data['username']
            username = username.strip()  # Eliminar espacios en blanco al inicio y al final

            # Validar longitud mínima y máxima del nombre de usuario
            if len(username) < 5:
                raise forms.ValidationError('El nombre de usuario debe tener al menos 5 caracteres.')
            if len(username) > 30:
                raise forms.ValidationError('El nombre de usuario no puede tener más de 30 caracteres.')

            # Validar caracteres permitidos (letras, números y guiones bajos)
            if not re.match(r'^[a-zA-Z0-9_]+$', username):
                raise forms.ValidationError('El nombre de usuario solo puede contener letras, números y guiones bajos (_).')

            # Validar que no haya dobles espacios o dos letras seguidas
            if re.search(r'\s{2}', username) or re.search(r'(.)\1{1}', username):
                raise forms.ValidationError('El nombre de usuario no puede contener dobles espacios ni dos letras seguidas.')

            # Verificar si el nombre de usuario ya está en uso
            base_username = username.lower()
            counter = 1
            while Usuario.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
                if counter > 100:
                    raise forms.ValidationError('No se pudo generar un nombre de usuario único. Por favor, elige otro.')
            
            # Si el nombre de usuario original estaba disponible, mostrar una sugerencia con un número al final
            if username != self.cleaned_data['username']:
                raise forms.ValidationError(f"El nombre de usuario {self.cleaned_data['username']} ya está en uso. ¿Qué tal {username}?")
            
            return username
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.')
        return confirm_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password




class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['Grado', 'NivelEducativo']
        labels = {
            'Grado': 'Nombre del Grado',
            'NivelEducativo': 'Nivel Educativo',
        }
        widgets = {
            'Grado': forms.TextInput(
                attrs={'class': 'form-control',
                       }),
            'NivelEducativo': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_Grado(self):
        grado = self.cleaned_data.get('Grado')
        solo_letras_validator(grado)
        no_campos_vacios_validator(grado)
        no_dos_espacios_validator(grado)
        no_numeros_validator(grado)
        no_tres_letras_iguales_validator(grado)
        return grado.capitalize()
    

class ExpedienteEscolarForm(forms.ModelForm):
    class Meta:
        model = ExpedienteEscolar
        fields = ['Actitud', 'Alumno', 'InstitutoAnterior', 'PromedioAnualAnterior', 'Tutor']
        labels = {
            'Actitud': 'Actitud del Alumno',
            'Alumno': 'Nombre del Alumno',
            'InstitutoAnterior': 'Instituto Anterior del Alumno',
            'PromedioAnualAnterior': 'Promedio Anual Anterior del Alumno',
            'Tutor': 'Nombre del Tutor',
        }
        widgets = {
            'Actitud': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'InstitutoAnterior': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{3,20}'}),
            'PromedioAnualAnterior': forms.IntegerField(),
            'Tutor': forms.Select(
                attrs={'class': 'form-control'}),
        }
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['Departamento']
        labels = {
            'Departamento': 'Departamento',
        }
        widgets = {
            'Departamento': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }
   
    def clean_Departamento(self):
        departamento = self.cleaned_data['Departamento']
        # Validar que no haya dobles espacios en blanco seguidos
        if '  ' in departamento:
            raise forms.ValidationError("No se permiten dobles espacios en blanco seguidos.")
        # Validar que el campo no esté vacío
        if not departamento.strip():
            raise forms.ValidationError("El campo Departamento no puede estar vacío.")
        # Validar si el nombre del departamento ya está registrado en la base de datos
        if Departamento.objects.filter(Departamento__iexact=departamento).exists():
            raise forms.ValidationError("Este nombre de departamento ya está registrado.")
        # Validar que no haya 3 letras iguales repetidas
        no_tres_letras_iguales_validator(departamento)
        # Validar que solo contenga letras y acentos
        no_numeros_ni_especiales_validator(departamento)
        return departamento
    def get_error_list(self):
        errors = []
        for field, error_list in self.errors.items():
            for error in error_list:
                errors.append(f"{self[field].label}: {error}")
        return errors


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombreMunicipio', 'Departamento']
        labels = {
            'nombeMunicipio': 'Municipio',
            'Departamento': 'Departamento',
        }
        widgets = {
            'nombreMunicipio': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{4,20}',}),
            'Departamento': forms.Select(
                attrs={'class': 'form-control'}),
        }


class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = ['Tutor', 'Alumno', 'FechaPago','TipoPago', 'Meses', 'HoraPago']
        labels = {
            'Tutor': 'Tutor',
            'Alumno': 'Alumno',
            'FechaPago': 'Fecha de pago',
            'TipoPago': 'Tipo de pago, precio',
            'Meses': 'Mes a pagar',
            'HoraPago': 'Hora de pago',
        }
        widgets = {
            'Tutor': forms.Select(
                attrs={'class': 'form-control'}),
            'Alumno': forms.Select(
                attrs={'class': 'form-control'}),
            'FechaPago': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'TipoPago': forms.Select(
                attrs={'class': 'form-control'}),
            'Meses': forms.Select(
                attrs={'class': 'form-control'}),
            'HoraPago': forms.TimeInput(
                attrs={'class': 'form-control'}),
        }
class MensualidadForm(forms.ModelForm):
    class Meta:
        model = Meses
        fields = ['Meses']
        labels = {
            'Meses': 'Mes.',
        }
        widgets = {
            'Meses': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }

    def clean_Meses(self):
        mes = self.cleaned_data.get('Meses')
        solo_letras_validator(mes)
        no_campos_vacios_validator(mes)
        no_dos_espacios_validator(mes)
        no_numeros_validator(mes)
        no_tres_letras_iguales_validator(mes)
        return mes.capitalize()
    
class ParametrosSARForm(forms.ModelForm):
    class Meta:
        model = ParametrosSAR
        fields = ['CAI', 'RTN', 'RangoInicial', 'RangoFinal', 'FechaEmision', 'FechaVencimiento', 'Correlativo']
        labels = {
            'CAI': 'CAI:',
            'RTN': 'RTN:',
            'RangoInicial': 'Rango Inicial:',
            'RangoFinal': 'Rango Final:',
            'FechaEmision': 'Fecha de emision:',
            'FechaVencimiento': 'Fecha de vencimiento',
            'Correlativo': 'Correlativo'
        }
        widgets = {
            'CAI': forms.TextInput(
                attrs={'class': 'form-control'}),
            'RTN': forms.TextInput(
                attrs={'class': 'form-control'}),
            'RangoInicial': forms.TextInput(
                attrs={'class': 'form-control'}),
            'RangoFinal': forms.TextInput(),
            'FechaEmision': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'FechaVencimiento': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date'}),
            'Correlativo': forms.DateInput(
                attrs={'class': 'form-control'}),
        }
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaEmpleado
        fields = ['CategoriaEmpleado']
        labels = {
            'CategoriaEmpleado': 'Categoria de empleado',
        }
        widgets = {
            'CategoriaEmpleado': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_CategoriaEmpleado(self):
        categoria_empleado = self.cleaned_data.get('CategoriaEmpleado')
        solo_letras_validator(categoria_empleado)
        no_campos_vacios_validator(categoria_empleado)
        no_dos_espacios_validator(categoria_empleado)
        no_numeros_validator(categoria_empleado)
        no_tres_letras_iguales_validator(categoria_empleado)
        return categoria_empleado.capitalize()
    
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = DocumentoDPI
        fields = ['DocumentoDPI']
        labels = {
            'DocumentoDPI': 'Documento de identificacion personal:',
        }
        widgets = {
            'DocumentoDPI': forms.TextInput(
                attrs={'class': 'form-control'}),
            
        }

class TipoPagoForm(forms.ModelForm):
    class Meta:
        model=TipoPago
        fields=['TipoPago', 'PrecioPago']
        labels={'TipoPago':'Nombre del pago',
                'PrecioPago':'Precio del pago'}
        widgets={
            'TipoPago': forms.TextInput(
                 attrs={'class': 'form-control',
                        'pattern':'[a-zA-Z].{4,20}',}),
            'PrecioPago': forms.NumberInput(
                 attrs={'class': 'form-control',
                        'step':'.1'}),
            }
        
    def clean_TipoPago(self):
        tipopago = self.cleaned_data.get('TipoPago')
        solo_letras_validator(tipopago)
        no_campos_vacios_validator(tipopago)
        no_dos_espacios_validator(tipopago)
        no_numeros_validator(tipopago)
        no_tres_letras_iguales_validator(tipopago)
        return tipopago.capitalize()
        
class TipoSanguineoForm(forms.ModelForm):
    class Meta:
        model = TipoSanguineo
        fields = ['TipoSanguineo']
        labels = {
            'TipoSanguineo': 'Tipo Sanguineo',
        }
        widgets = {
            'TipoSanguineo': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_TipoSanguineo(self):
        tipo_sanguineo = self.cleaned_data.get('TipoSanguineo')
        solo_letras_validator(tipo_sanguineo)
        no_campos_vacios_validator(tipo_sanguineo)
        no_dos_espacios_validator(tipo_sanguineo)
        no_numeros_validator(tipo_sanguineo)
        no_tres_letras_iguales_validator(tipo_sanguineo)
        return tipo_sanguineo.capitalize()
    
class TipoReporteForm(forms.ModelForm):
    class Meta:
        model = TipoReporte
        fields = ['TipoReporte']
        labels = {
            'TipoReporte': 'Tipo de reporte',
        }
        widgets = {
            'TipoReporte': forms.TextInput(
                attrs={'class': 'form-control'}),   
        }

    def clean_TipoReporte(self):
        categoria_empleado = self.cleaned_data.get('CategoriaEmpleado')
        solo_letras_validator(categoria_empleado)
        no_campos_vacios_validator(categoria_empleado)
        no_dos_espacios_validator(categoria_empleado)
        no_numeros_validator(categoria_empleado)
        no_tres_letras_iguales_validator(categoria_empleado)
        return categoria_empleado.capitalize()
    
class FacturacionForm(forms.ModelForm):
    class Meta:
        model = Facturacion
        fields = ['NumeroFactura', 'Fecha', 'ParametrosSAR', 'CentroEducativo', 'Pagos', 'ImporteExonerado', 'ImporteExcento', 'ImporteGravado15', 'ImporteGravado18', 'ImpuestoSobreVenta15', 'ImpuestoSobreVenta18', 'Total']
        labels = {
            'NumeroFactura': 'Número de Factura',
            'Fecha': 'Fecha',
            'ParametrosSAR': 'Parámetros SAR',
            'CentroEducativo': 'Nombre del Centro Educativo',
            'Pagos': 'Pagos',
            'ImporteExonerado': 'Importe Exonerado',
            'ImporteExcento': 'Importe Excento',
            'ImporteGravado15': 'Importe Gravado 15%',
            'ImporteGravado18': 'Importe Gravado 18%',
            'ImpuestoSobreVenta15': 'Impuesto sobre Venta 15%',
            'ImpuestoSobreVenta18': 'Impuesto sobre Venta 18%',
            'Total': 'Total',
        }
        widgets = {
            'NumeroFactura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Factura'}),
            'Fecha': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
            'ParametrosSAR': forms.Select(attrs={'class': 'form-control'}),
            'CentroEducativo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Centro Educativo'}),
            'Pagos': forms.Select(attrs={'class': 'form-control'}),
            'ImporteExonerado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Importe Exonerado'}),
            'ImporteExcento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Importe Excento'}),
            'ImporteGravado15': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Importe Gravado 15%'}),
            'ImporteGravado18': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Importe Gravado 18%'}),
            'ImpuestoSobreVenta15': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Impuesto sobre Venta 15%'}),
            'ImpuestoSobreVenta18': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Impuesto sobre Venta 18%'}),
            'Total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),
        }
