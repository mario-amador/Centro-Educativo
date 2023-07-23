from imaplib import _Authenticator
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Alumno,Empleado,Catedratico, ExpedienteEscolar, Grado, Municipio,Tutor,Asignatura,Matricula,Reportes,ExpedienteMedico, HorariosNivelEducativo, NivelEducativo, ParcialesAcademicos, NotasAlumnos
from .forms import AlumnoForm,EmpleadoForm,CatedraticoForm, ExpedienteEscolarForm, GradoForm,TutorForm,AsignaturaForm,MatriculaForm,ReportesForm,ExpedienteMedicoForm, HorariosForm, NivelesForm, ParcialesForm, NotasForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Usuario

from django.contrib import messages

#login

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.db.models import F

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.db.models import F

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            user = None

        if user is not None and user.password == password:
            # Las credenciales son correctas
            if user.intentos_fallidos >= 3:
                # El usuario ha excedido el número máximo de intentos fallidos
                # Puedes bloquear al usuario aquí o aplicar alguna lógica adicional de seguridad
                messages.error(request, 'Ha excedido el número máximo de intentos fallidos. Por favor, contacte al administrador.')
                return redirect('login')  # Redirigir al formulario de inicio de sesión
            
            # Restablecer el número de intentos fallidos a 0
            user.intentos_fallidos = 0
            user.save()
            
            login(request, user)
            if user.rol.nombre == "Administrador":
                messages.success(request, f'Bienvenido, {user.username} (Administrador)')
                return redirect('bienvenida_administrador')
            elif user.rol.nombre == "Alumno":
                messages.success(request, f'Bienvenido, {user.username} (Alumno)')
                return redirect('bienvenida_alumno')
            elif user.rol.nombre == "Catedrático":
                messages.success(request, f'Bienvenido, {user.username} (Catedrático)')
                return redirect('bienvenida_catedratico')
            else:
                messages.error(request, 'Rol de usuario no válido')
                return redirect('login')  # Redirigir al formulario de inicio de sesión si el rol no es válido
        else:
            # Las credenciales son incorrectas
            if user is not None:
                # Incrementar el número de intentos fallidos
                user.intentos_fallidos += 1
                user.save()

            messages.error(request, 'Credenciales incorrectas')
            return redirect('login')  # Redirigir al formulario de inicio de sesión si las credenciales son incorrectas
    
    return render(request, 'base/login.html')






#View Municipios
def load_municipios(request):
    Departamento_id = request.GET.get('Departamento')
    municipios = Municipio.objects.filter(Departamento_id=Departamento_id).order_by('Departamento')
    return render(request, 'Municipios/municipios_dropdown_list.html', {'municipios':municipios})


 #inicios segun rol   
from django.views.generic import TemplateView

class BienvenidaAdministradorView(TemplateView):
    template_name = 'pantallas/administrador.html'

class BienvenidaAlumnoView(TemplateView):
    template_name = 'pantallas/alumno.html'

class BienvenidaCatedraticoView(TemplateView):
    template_name = 'pantallas/catedratico.html'
        

from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class InicioPantalla(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/index.html'
    login_url = 'base/login'

    def get_success_url(self):
        # Agrega aquí tu lógica personalizada para determinar la URL de éxito
        # Puedes utilizar self.request.user para acceder al usuario actual

        # Ejemplo: redirigir a una URL diferente según el rol del usuario
        if self.request.user.usuario.rol.nombre == 'Administrador':
            return reverse_lazy('bienvenida_administrador')
        elif self.request.user.usuario.rol.nombre == 'Alumno':
            return reverse_lazy('bienvenida_alumno')
        elif self.request.user.usuario.rol.nombre == 'Catedratico':
            return reverse_lazy('bienvenida_catedratico')
        else:
            return reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega aquí el contexto adicional que desees pasar a la plantilla
        # Puedes utilizar self.request.user para acceder al usuario actual
        return context



from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import UserForm
from .models import Usuario

#usuarios

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'Usuario/usuario_detalle.html'

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'Usuario/usuario_listar.html'
    context_object_name = 'usuarios'



class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UserForm
    template_name = 'Usuario/usuario_crear.html'
    success_url = reverse_lazy('usuario_listar')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UserForm
    template_name = 'Usuario/usuario_editar.html'
    success_url = reverse_lazy('usuario_listar')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'Usuario/usuario_eliminar.html'
    success_url = reverse_lazy('usuario_listar')


class AlumnoListView(ListView):
    model = Alumno
    template_name = 'Alumno/alumno_listar.html'
    context_object_name = 'alumnos'
    login_url='base/login'

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'Alumno/alumno_crear.html'
    success_url = reverse_lazy('alumno_listar')

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'success': True})
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse({'success': False})
        return response

class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'Alumno/alumno_detalle.html'

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'Alumno/alumno_editar.html'
    success_url = reverse_lazy('alumno_listar')

class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'Alumno/alumno_eliminar.html'
    success_url = reverse_lazy('alumno_listar')

#views de Empleado



class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'Empleado/Empleado_listar.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'Empleado/empleado_crear.html'
    success_url = reverse_lazy('listar_empleados')

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'Empleado/empleado_detalle.html'

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'Empleado/editar.html'
    success_url = reverse_lazy('listar_empleados')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'Empleado/eliminar.html'
    success_url = reverse_lazy('listar_empleados')

#views catedratico



class CatedraticoListView(ListView):
    model = Catedratico
    template_name = 'catedratico/catedratico_listar.html'
    context_object_name = 'catedraticos'

class CatedraticoCreateView(CreateView):
    model = Catedratico
    form_class = CatedraticoForm
    template_name = 'catedratico/catedratico_crear.html'
    success_url = reverse_lazy('listar_catedraticos')

    def agregar_catedratico(request):
        if request.method == 'POST':
            form = CatedraticoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Catedrático agregado exitosamente.')
                return redirect('listar_catedraticos')
            else:
                messages.error(request, 'Error: Algunos campos están incorrectos.')
        else:
            form = CatedraticoForm()
        
        context = {
            'form': form,
        }
        return render(request, 'Catedratico/catedratico_crear.html', context)


class CatedraticoDetailView(DetailView):
    model = Catedratico
    template_name = 'Catedratico/catedratico_detalle.html'

class CatedraticoUpdateView(UpdateView):
    model = Catedratico
    form_class = CatedraticoForm
    template_name = 'catedratico/catedratico_editar.html'
    success_url = reverse_lazy('listar_catedraticos')

class CatedraticoDeleteView(DeleteView):
    model = Catedratico
    template_name = 'catedratico/catedratico_eliminar.html'
    success_url = reverse_lazy('listar_catedraticos')

#views de Tutor

class TutorListView(ListView):
    model = Tutor
    template_name = 'Tutor/tutor_listar.html'
    context_object_name = 'tutores'
    login_url = 'base/login'

class TutorCreateView(CreateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'Tutor/tutor_crear.html'
    success_url = reverse_lazy('tutor_listar')

class TutorDetailView(DetailView):
    model = Tutor
    template_name = 'Tutor/tutor_detalle.html'

class TutorUpdateView(UpdateView):
    model = Tutor
    form_class = TutorForm
    template_name = 'Tutor/tutor_editar.html'
    success_url = reverse_lazy('tutor_listar')

class TutorDeleteView(DeleteView):
    model = Tutor
    template_name = 'Tutor/tutor_eliminar.html'
    success_url = reverse_lazy('tutor_listar')

#views Asignatura

class AsignaturaListView(ListView):
    model = Asignatura
    template_name = 'Asignatura/asignatura_listar.html'
    context_object_name = 'asignaturas'

class AsignaturaCreateView(CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'Asignatura/asignatura_crear.html'
    success_url = reverse_lazy('asignatura_listar')

def agregar_asignatura(request):
    if request.method == 'POST':
        # Lógica para guardar la asignatura
        messages.success(request, 'Asignatura guardada exitosamente.')
        return redirect('asignatura_listar')
    
    form = AsignaturaForm()
    return render(request, 'Asignatura/asignatura_crear.html', {'form': form})

class AsignaturaDetailView(DetailView):
    model = Asignatura
    template_name = 'Asignatura/asignatura_detalle.html'

class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'Asignatura/asignatura_editar.html'
    success_url = reverse_lazy('asignatura_listar')

class AsignaturaDeleteView(DeleteView):
    model = Asignatura
    template_name = 'Asignatura/asignatura_eliminar.html'
    success_url = reverse_lazy('asignatura_listar')

#views Matricula

class MatriculaListView(ListView):
    model = Matricula
    template_name = 'Matricula/matricula_listar.html'
    context_object_name = 'matriculas'

class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'Matricula/matricula_crear.html'
    success_url = reverse_lazy('matricula_listar')

class MatriculaDetailView(DetailView):
    model = Matricula
    template_name = 'Matricula/matricula_detalle.html'

class MatriculaUpdateView(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'Matricula/matricula_editar.html'
    success_url = reverse_lazy('matricula_listar')

class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = 'Matricula/matricula_eliminar.html'
    success_url = reverse_lazy('matricula_listar')

#views Reportes

class ReportesListView(ListView):
    model = Reportes
    template_name = 'Reporte/reporte_listar.html'
    context_object_name = 'reportes'

class ReportesCreateView(CreateView):
    model = Reportes
    form_class = ReportesForm
    template_name = 'Reporte/reporte_crear.html'
    success_url = reverse_lazy('reporte_listar')

class ReportesDetailView(DetailView):
    model = Reportes
    template_name = 'Reporte/reporte_detalle.html'

class ReportesUpdateView(UpdateView):
    model = Reportes
    form_class = ReportesForm
    template_name = 'Reporte/reporte_editar.html'
    success_url = reverse_lazy('reporte_listar')

class ReportesDeleteView(DeleteView):
    model = Reportes
    template_name = 'Reporte/reporte_eliminar.html'
    success_url = reverse_lazy('reporte_listar')

    
#views Expediente Médicos

class ExpedienteMedicoListView(ListView):
    model = ExpedienteMedico
    template_name = 'ExpedienteMedico/expedientemedico_listar.html'
    context_object_name = 'expedientemedicos'

class ExpedienteMedicoCreateView(CreateView):
    model = ExpedienteMedico
    form_class = ExpedienteMedicoForm
    template_name = 'ExpedienteMedico/expedientemedico_crear.html'
    success_url = reverse_lazy('expedientemedico_listar')

class ExpedienteMedicoDetailView(DetailView):
    model = ExpedienteMedico
    template_name = 'ExpedienteMedico/expedientemedico_detalle.html'

class ExpedienteMedicoUpdateView(UpdateView):
    model = ExpedienteMedico
    form_class = ExpedienteMedicoForm
    template_name = 'ExpedienteMedico/expedientemedico_editar.html'
    success_url = reverse_lazy('expedientemedico_listar')

class ExpedienteMedicoDeleteView(DeleteView):
    model = ExpedienteMedico
    template_name = 'ExpedienteMedico/expedientemedico_eliminar.html'
    success_url = reverse_lazy('expedientemedico_listar')

# views Horarios
class HorariosListView(ListView):
    model = HorariosNivelEducativo
    template_name = 'Horarios/horarios_listar.html'
    context_object_name = 'horarios'

class HorariosCreateView(CreateView):
    model = HorariosNivelEducativo
    form_class =    HorariosForm
    template_name = 'Horarios/horarios_crear.html'
    success_url = reverse_lazy('horarios_listar')

class HorariosUpdateView(UpdateView):
    model = HorariosNivelEducativo
    form_class = HorariosForm
    template_name = 'Horarios/horarios_editar.html'
    success_url = reverse_lazy('horarios_listar')

class HorariosDeleteView(DeleteView):
    model = HorariosNivelEducativo
    template_name = 'Horarios/horarios_eliminar.html'
    success_url = reverse_lazy('horarios_listar')

class HorariosDetailView(DetailView):
    model = HorariosNivelEducativo
    template_name = 'Horarios/horarios_detalle.html'
#views niveles

class NivelesListView(ListView):
    model = NivelEducativo
    template_name = 'Niveles/niveles_listar.html'
    context_object_name = 'niveles'

class NivelesCreateView(CreateView):
    model = NivelEducativo
    form_class = NivelesForm
    template_name = 'Niveles/niveles_crear.html'
    success_url = reverse_lazy('niveles_listar')

class NivelesUpdateView(UpdateView):
    model = NivelEducativo
    form_class = NivelesForm
    template_name = 'Niveles/niveles_editar.html'
    success_url = reverse_lazy('niveles_listar')

class NivelesDeleteView(DeleteView):
    model = NivelEducativo
    template_name = 'Niveles/niveles_eliminar.html'
    success_url = reverse_lazy('niveles_listar')

class NivelesDetailView(DetailView):
    model = NivelEducativo
    template_name = 'Niveles/niveles_detalle.html'

#vies parciales

class ParcialesListView(ListView):
    model = ParcialesAcademicos
    template_name = 'Parciales/parciales_listar.html'
    context_object_name = 'parciales'

class ParcialesCreateView(CreateView):
    model = ParcialesAcademicos
    form_class = ParcialesForm
    template_name = 'Parciales/parciales_crear.html'
    success_url = reverse_lazy('parciales_listar')

class ParcialesUpdateView(UpdateView):
    model = ParcialesAcademicos
    form_class = ParcialesForm
    template_name = 'Parciales/parciales_editar.html'
    success_url = reverse_lazy('parciales_listar')

class ParcialesDeleteView(DeleteView):
    model = ParcialesAcademicos
    template_name = 'Parciales/parciales_eliminar.html'
    success_url = reverse_lazy('parciales_listar')

class ParcialesDetailView(DetailView):
    model = ParcialesAcademicos
    template_name = 'Parciales/parciales_detalle.html'

#Views Notas
class NotasListView(ListView):
    model = NotasAlumnos
    template_name = 'Notas/notas_listar.html'
    context_object_name = 'notas'

class NotasCreateView(CreateView):
    model = NotasAlumnos
    form_class = NotasForm
    template_name = 'Notas/notas_crear.html'
    success_url = reverse_lazy('notas_listar')

class NotasUpdateView(UpdateView):
    model = NotasAlumnos
    form_class = NotasForm
    template_name = 'Notas/notas_editar.html'
    success_url = reverse_lazy('notas_listar')

class NotasDeleteView(DeleteView):
    model = NotasAlumnos
    template_name = 'Notas/notas_eliminar.html'
    success_url = reverse_lazy('notas_listar')

class NotasDetailView(DetailView):
    model = NotasAlumnos
    template_name = 'Notas/notas_detalle.html'

#grados

class GradoListView(ListView):
    model = Grado
    template_name = 'Grado/grado_listar.html'
    context_object_name = 'grados'
    login_url = 'base/login'

class GradoCreateView(CreateView):
    model = Grado
    form_class = GradoForm
    template_name = 'Grado/grado_crear.html'
    success_url = reverse_lazy('grado_listar')

class GradoDetailView(DetailView):
    model = Grado
    template_name = 'Grado/grado_detalle.html'

class GradoUpdateView(UpdateView):
    model = Grado
    form_class = TutorForm
    template_name = 'Grado/grado_editar.html'
    success_url = reverse_lazy('grado_listar')

class GradoDeleteView(DeleteView):
    model = Grado
    template_name = 'Grado/grado_eliminar.html'
    success_url = reverse_lazy('grado_listar')

#expedientes escolares

class ExpedienteEscolarListView(ListView):
    model = ExpedienteEscolar
    template_name = 'ExpedienteEscolar/expedienteescolar_listar.html'
    context_object_name = 'expedienteescolares'

class ExpedienteEscolarCreateView(CreateView):
    model = ExpedienteEscolar
    form_class = ExpedienteEscolarForm
    template_name = 'ExpedienteEscolar/expedienteescolar_crear.html'
    success_url = reverse_lazy('expedienteescolar_listar')

class ExpedienteEscolarDetailView(DetailView):
    model = ExpedienteEscolar
    template_name = 'ExpedienteEscolar/expedienteescolar_detalle.html'

class ExpedienteEscolarUpdateView(UpdateView):
    model = ExpedienteEscolar
    form_class = ExpedienteEscolarForm
    template_name = 'ExpedienteEscolar/expedienteescolar_editar.html'
    success_url = reverse_lazy('expedienteescolar_listar')

class ExpedienteEscolarDeleteView(DeleteView):
    model = ExpedienteEscolar
    template_name = 'ExpedienteEscolar/expedienteescolar_eliminar.html'
    success_url = reverse_lazy('expedienteescolar_listar')
