# Instrucciones para ejecutar este proyecto
# MODIFICAR ANTES DE ENTREGAR!!!!
- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/FRABT/Proyecto.git

cd Proyecto

git checkout master

```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
- Instalar Django
```bash
pip install Django
```

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations app_blog

python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```

- Ejecutar proyecto
```bash
python manage.py runserver
```

- Navegar en la web
```bash
Ingresar a:
    http://127.0.0.1:8000/app_blog

    Los formularios para insertar datos en:
        
        Clase User: Entrar a User >>> Create User
        Clase Blog: Entrar a Blog >>> Create Blog
        Clase Comment: Entrar a Comment >>> Create Comment

    El formulario para buscar elgo en la BD(En este caso en la Clase User):

        Entrar a User >>> Search User
```