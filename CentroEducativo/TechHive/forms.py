import re
from django import forms
from django.forms import Select, DateInput
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
                attrs={'class': 'form-control',
                       'pattern':'[0,9].{12,15}'}),
            'FechaNacimientoEmpleado': forms.DateInput(
                attrs={'class': 'form-control', 
                       'placeholder': 'YYYY-MM-DD', 
                       'type': 'date',
                       'min': '1974-01-01',
                       'max': '2004-01-01'}),
            'CategoriaEmpleado': forms.Select(
                attrs={'class': 'form-control'}),
            'Tel_Empleado': forms.TextInput(
                attrs={'class': 'form-control',
                    'pattern': '[389]\d{7}',
                    'placeholder': '########'}),
        }


def clean_NombresEmpleado(self):
    nombres_empleado = self.cleaned_data.get('NombresEmpleado')

    if any(char.isdigit() for char in nombres_empleado):
        raise forms.ValidationError('El nombre no debe contener números.')

    if len(nombres_empleado) < 3 or len(nombres_empleado) > 10:
        raise forms.ValidationError('La longitud del nombre debe ser entre 3 y 10 caracteres.')

    if re.search(r'(\w)\1', nombres_empleado):
        raise forms.ValidationError('El nombre no puede contener letras repetidas.')

    if '  ' in nombres_empleado:
        raise forms.ValidationError('El nombre no puede contener espacios dobles.')

    return nombres_empleado.capitalize()

def clean_ApellidosEmpleado(self):
    apellidos_empleado = self.cleaned_data.get('ApellidosEmpleado')

    if any(char.isdigit() for char in apellidos_empleado):
        raise forms.ValidationError('Los apellidos no deben contener números.')

    if len(apellidos_empleado) < 2 or len(apellidos_empleado) > 40:
        raise forms.ValidationError('La longitud de los apellidos debe ser entre 2 y 40 caracteres.')

    if re.search(r'(\w)\1', apellidos_empleado):
        raise forms.ValidationError('Los apellidos no pueden contener letras repetidas.')

    if '  ' in apellidos_empleado:
        raise forms.ValidationError('Los apellidos no pueden contener espacios dobles.')

    return apellidos_empleado.capitalize()




class CatedraticoForm(forms.ModelForm):
    
    def clean_NombresCatedratico(self):
        nombres_catedratico = self.cleaned_data.get('NombresCatedratico')

        if any(char.isdigit() for char in nombres_catedratico):
            raise forms.ValidationError('El nombre no debe contener números.')

        if len(nombres_catedratico) < 3 or len(nombres_catedratico) > 20:
            raise forms.ValidationError('La longitud del nombre debe ser entre 3 y 20 caracteres.')

        if re.search(r'(\w)\1', nombres_catedratico):
            raise forms.ValidationError('El nombre no puede contener letras repetidas.')

        if '  ' in nombres_catedratico:
            raise forms.ValidationError('El nombre no puede contener espacios dobles.')

        return nombres_catedratico.capitalize()

    def clean_ApellidosCatedratico(self):
        apellidos_catedratico = self.cleaned_data.get('ApellidosCatedratico')

        if any(char.isdigit() for char in apellidos_catedratico):
            raise forms.ValidationError('Los apellidos no deben contener números.')

        if len(apellidos_catedratico) < 2 or len(apellidos_catedratico) > 30:
            raise forms.ValidationError('La longitud de los apellidos debe ser entre 2 y 30 caracteres.')

        if re.search(r'(\w)\1', apellidos_catedratico):
            raise forms.ValidationError('Los apellidos no pueden contener letras repetidas.')

        if '  ' in apellidos_catedratico:
            raise forms.ValidationError('Los apellidos no pueden contener espacios dobles.')

        return apellidos_catedratico.capitalize()
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
                       'type': 'date',
                       'min': '1974-01-01',
                       'max': '2004-01-01'}),
            'Tel_Catedratico': forms.TextInput(
                attrs={'class': 'form-control',
                    'pattern': '[389]\d{7}',
                    'placeholder': '########'}),

        }

   

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
                    'pattern': '[389]\d{7}',
                    'placeholder': '########'}),
            'Parentesco': forms.TextInput(
                attrs={'class': 'form-control',
                       'pattern':'[a-zA-Z].{2,15}',}),
        }

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
    username = forms.CharField(
        label='Usuario',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        label='Contraseña',
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Credenciales incorrectas. Por favor, verifique sus datos.')

        return cleaned_data
    

from django import forms
from .models import Usuario

from django import forms
from .models import Usuario

from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )
    ACTIVO_CHOICES = [
        (1, 'Sí'),
        (0, 'No'),
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
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'
        self.fields['confirm_password'].label = 'Confirmar contraseña'
        self.fields['username'].widget.attrs.pop('readonly', None)  # Remover el atributo de solo lectura

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")

        return cleaned_data






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
                       'pattern':'[a-zA-Z].{4,20}',}),
            'NivelEducativo': forms.Select(
                attrs={'class': 'form-control'}),
        }

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