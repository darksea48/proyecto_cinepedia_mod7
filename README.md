# 🎬 Proyecto Cinepedia

[![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

**Plataforma web para gestión y reseña de películas** - Sistema completo de gestión de contenido cinematográfico con funcionalidades de publicación, comentarios y administración de usuarios.

## 📋 Descripción

Cinepedia es una aplicación web desarrollada en Django que permite a los usuarios gestionar una base de datos de películas, escribir reseñas, comentar y interactuar con el contenido cinematográfico. El sistema incluye autenticación de usuarios, gestión de permisos y un sistema de comentarios con funcionalidades avanzadas.

## ✨ Características Principales

### 🎥 Gestión de Películas
- **CRUD Completo**: Crear, leer, actualizar y eliminar películas
- **Información Detallada**: Nombre, director, fecha de estreno y sinopsis
- **Control de Permisos**: Solo el usuario que publica puede editar/eliminar

### 💬 Sistema de Comentarios
- **Comentarios por Película**: Los usuarios pueden comentar en cada película
- **Ordenamiento Inteligente**: Por fecha de creación y comentarios fijados
- **Gestión de Comentarios Fijados**: Máximo 2 comentarios fijados por película por parte de quien publica la película
- **Eliminación Controlada**: Solo el autor del comentario o del contenido puede eliminar

### 👥 Gestión de Usuarios
- **Registro e Inicio de Sesión**: Sistema de autenticación personalizado
- **Control de Acceso**: Páginas protegidas con `LoginRequiredMixin`
- **Perfiles de Usuario**: Asociación de contenido con usuarios específicos

### 🎨 Interfaz de Usuario
- **Diseño Responsivo**: Interfaz moderna con Bootstrap 5
- **Formularios Estilizados**: Formularios personalizados con validación
- **Mensajes de Feedback**: Sistema de notificaciones para acciones del usuario

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| **Django** | 5.2.7 | Framework web principal |
| **MySQL** | 8.0+ | Base de datos |
| **Bootstrap** | 5.3 | Framework CSS |
| **Python** | 3.11+ | Lenguaje de programación |
| **django-crispy-forms** | Latest | Renderizado de formularios |

## 📁 Estructura del Proyecto

```
proyecto_cinepedia/
├── manage.py                      # Utilidad de administración de Django
├── cinepedia/                     # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py               # Configuración del proyecto
│   ├── urls.py                   # URLs principales
│   ├── wsgi.py                   # Configuración WSGI
│   └── asgi.py                   # Configuración ASGI
├── app_peliculas/                # Aplicación principal de películas
│   ├── models.py                 # Modelos de datos (Pelicula, Comentario)
│   ├── views.py                  # Vistas CBV y FBV
│   ├── urls.py                   # URLs de la aplicación
│   ├── forms.py                  # Formularios personalizados
│   ├── admin.py                  # Configuración del admin
│   ├── templates/                # Plantillas HTML
│   │   ├── index.html           # Página de inicio
│   │   ├── lista.html           # Lista de películas
│   │   ├── detalle.html         # Detalle de película y comentarios
│   │   ├── form.html            # Formulario de película
│   │   └── confirm_delete.html  # Confirmación de eliminación
│   └── migrations/              # Migraciones de base de datos
├── app_usuarios/                 # Aplicación de gestión de usuarios
│   ├── models.py                # Modelos de usuario (usa User de Django)
│   ├── views.py                 # Vistas de registro y autenticación
│   ├── forms.py                 # Formularios de usuario personalizados
│   ├── urls.py                  # URLs de autenticación
│   └── templates/               # Plantillas de autenticación
└── templates/                   # Plantillas globales
    └── base.html               # Plantilla base
```

## 🗃️ Modelos de Datos

### Modelo Pelicula
```python
class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)           # Título de la película
    director = models.CharField(max_length=255)         # Director
    fecha_estreno = models.DateField()                  # Fecha de estreno
    sinopsis = models.TextField()                       # Descripción/sinopsis
    publicado_por = models.ForeignKey(User)             # Usuario que publicó
```

### Modelo Comentario
```python
class Comentario(models.Model):
    contenido = models.TextField()                      # Contenido del comentario
    fecha = models.DateTimeField(auto_now_add=True)     # Fecha de creación
    pelicula = models.ForeignKey(Pelicula)              # Película asociada
    autor = models.ForeignKey(User)                     # Autor del comentario
    fijado = models.BooleanField(default=False)         # Estado de fijado
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.11 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el Repositorio
```bash
git clone <repository-url>
cd proyecto_cinepedia
```

### 2. Crear Entorno Virtual
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Linux/macOS
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install django==5.2.7
pip install mysqlclient
pip install django-crispy-forms
pip install crispy-bootstrap5
```

### 4. Configurar Base de Datos
1. Crear base de datos MySQL:
```sql
CREATE DATABASE cinepedia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Configurar credenciales en `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cinepedia',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Ejecutar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear Superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar Servidor de Desarrollo
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## 🌐 URLs y Endpoints

### Aplicación Principal
| URL | Vista | Nombre | Descripción |
|-----|-------|--------|-------------|
| `/` | `index` | `index` | Página de inicio |
| `/cine/` | `PeliculaListView` | `pelicula_list` | Lista de películas |
| `/cine/nueva/` | `PeliculaCreateView` | `pelicula_create` | Crear película |
| `/cine/<int:pk>/` | `PeliculaDetailView` | `pelicula_detail` | Detalle de película |
| `/cine/editar/<int:pk>/` | `PeliculaUpdateView` | `pelicula_update` | Editar película |
| `/cine/eliminar/<int:pk>/` | `PeliculaDeleteView` | `pelicula_delete` | Eliminar película |

### Gestión de Comentarios
| URL | Vista | Nombre | Descripción |
|-----|-------|--------|-------------|
| `/comentario/fijar/<int:comentario_id>/` | `fijar_comentario` | `fijar_comentario` | Fijar comentario |
| `/comentario/desfijar/<int:comentario_id>/` | `desfijar_comentario` | `desfijar_comentario` | Desfijar comentario |
| `/comentario/eliminar/<int:comentario_id>/` | `comentario_delete` | `comentario_delete` | Eliminar comentario |

### Autenticación
| URL | Vista | Nombre | Descripción |
|-----|-------|--------|-------------|
| `/accounts/register/` | `registro` | `register` | Registro de usuario |
| `/accounts/login/` | `LoginView` | `login` | Inicio de sesión |
| `/accounts/logout/` | `LogoutView` | `logout` | Cerrar sesión |

## 🎯 Funcionalidades Principales

### 1. Gestión de Películas
- **Crear**: Formulario para agregar nuevas películas
- **Listar**: Vista de todas las películas disponibles
- **Detalle**: Vista completa con comentarios
- **Editar**: Solo disponible para el usuario que publicó
- **Eliminar**: Confirmación requerida, solo para el autor

### 2. Sistema de Comentarios
- **Agregar Comentarios**: En la vista de detalle de cada película
- **Ordenamiento**: Comentarios fijados primero, luego por fecha
- **Fijar/Desfijar**: Máximo 2 comentarios fijados por película
- **Eliminar**: Solo el autor del comentario o de la película

### 3. Control de Permisos
- **Autenticación Requerida**: Todas las páginas excepto inicio
- **Autorización Granular**: Edición/eliminación solo para autores
- **Mensajes de Error**: Feedback claro para acciones no permitidas

## 🔒 Seguridad

### Medidas Implementadas
- **Autenticación Django**: Sistema robusto de usuarios
- **CSRF Protection**: Protección contra ataques CSRF
- **Validación de Permisos**: `UserPassesTestMixin` para control granular
- **Sanitización de Datos**: Validación de formularios
- **Configuración Segura**: Debug deshabilitado en producción

### Configuración de Seguridad
```python
# En settings.py
DEBUG = False  # En producción
ALLOWED_HOSTS = ['tu-dominio.com']
SECRET_KEY = 'clave-secreta-compleja'
```

## 🧪 Testing

### Ejecutar Tests
```bash
python manage.py test
```

### Estructura de Tests
```
app_peliculas/tests.py    # Tests de funcionalidad de películas
app_usuarios/tests.py     # Tests de autenticación
```

## 📱 Características de UI/UX

### Diseño Responsivo
- **Bootstrap 5**: Framework CSS moderno
- **Componentes Estilizados**: Cards, formularios, botones
- **Navegación Intuitiva**: Menú de navegación claro
- **Mensajes de Feedback**: Notificaciones de éxito/error

### Experiencia de Usuario
- **Formularios Validados**: Feedback inmediato
- **Confirmaciones**: Para acciones destructivas
- **Carga Rápida**: Optimización de consultas
- **Accesibilidad**: Etiquetas semánticas

## 🚀 Despliegue

### Preparación para Producción
1. **Configurar Variables de Entorno**:
```bash
export SECRET_KEY='tu-clave-secreta'
export DEBUG=False
export DATABASE_URL='mysql://usuario:password@host:puerto/basedatos'
```

2. **Recopilar Archivos Estáticos**:
```bash
python manage.py collectstatic
```

3. **Configurar Servidor Web** (Nginx + Gunicorn recomendado)

### Docker (Opcional)
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "cinepedia.wsgi:application"]
```

## 🤝 Contribución

### Guías de Contribución
1. Fork del repositorio
2. Crear rama para feature: `git checkout -b feature/nueva-caracteristica`
3. Commit de cambios: `git commit -m 'Agregar nueva característica'`
4. Push a la rama: `git push origin feature/nueva-caracteristica`
5. Crear Pull Request

### Estándares de Código
- **PEP 8**: Seguir estándares de Python
- **Documentación**: Comentar código complejo
- **Tests**: Incluir tests para nuevas funcionalidades
- **Commits**: Mensajes descriptivos y claros

## 🐛 Problemas Conocidos

- [ ] Implementar paginación para lista de películas
- [ ] Agregar sistema de calificaciones
- [ ] Implementar búsqueda avanzada
- [ ] Optimizar carga de imágenes

## 📝 Changelog

### v1.0.0 (Actual)
- ✅ Sistema completo de gestión de películas
- ✅ Sistema de comentarios con fijado
- ✅ Autenticación y autorización
- ✅ Interfaz responsiva con Bootstrap

### Próximas Versiones
- 🔄 Sistema de calificaciones por estrellas
- 🔄 Búsqueda y filtros avanzados
- 🔄 Subida de pósters de películas
- 🔄 API REST para integración

## 📞 Soporte

### Creado por
- **Desarrollador**: [Douglas Suárez Zamorano]
- **Email**: [d.suarez.zamorano@gmail.com]
- **GitHub**: [@darksea48]

### Documentación Adicional
- [Documentación de Django](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

---

**© 2024 Proyecto Cinepedia** - Desarrollado con ❤️ y con Django

*Proyecto desarrollado como parte del Bootcamp Full Stack Python/Django - Sistema de gestión cinematográfica*