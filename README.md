# taller_admin_django
# Escenarios de Administración de Base de Datos y Django Admin

## Escenario 1: SQLiteBrowser + Django Admin

En este escenario se utiliza SQLite como motor de base de datos predeterminado de Django. La administración de los datos se realiza mediante SQLiteBrowser, mientras que la gestión de usuarios, modelos y registros se realiza desde el panel de administración de Django.

### Evidencia

En la siguiente imagen se muestra SQLiteBrowser junto con el panel de administración de Django funcionando sobre la misma base de datos.

![SQLiteBrowser y Django Admin](![alt text](<Captura de pantalla 2026-06-16 150110.png>)![alt text](<Captura de pantalla 2026-06-16 150517.png>)![alt text](<Captura de pantalla 2026-06-16 150549.png>)
![alt text](<Captura de pantalla 2026-06-16 150608.png>)
)

---

## Escenario 2: PostgreSQL (Docker) + PgAdmin + Django Admin

En este escenario se utiliza PostgreSQL como sistema gestor de base de datos, ejecutado mediante Docker. Para la administración de la base de datos se emplea PgAdmin y para la gestión de la aplicación se utiliza el panel de administración de Django.

### Configuración de PostgreSQL en Django

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'museo_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}
```

### Configuración Docker

```yaml
services:
  postgres:
    image: postgres:15
    container_name: museo_db
    environment:
      POSTGRES_DB: museo_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    ports:
      - "5433:5432"

  pgadmin:
    image: dpage/pgadmin4:latest
    container_name: museo_pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
```

### Evidencia

En la siguiente imagen se muestra PgAdmin conectado a PostgreSQL mediante Docker y el panel de administración de Django utilizando la misma base de datos.

![PgAdmin y Django Admin](![alt text](<Captura de pantalla 2026-06-16 162349.png>)![alt text](<Captura de pantalla 2026-06-16 162533.png>)![alt text](<Captura de pantalla 2026-06-16 162813.png>)
