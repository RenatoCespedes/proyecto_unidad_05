
# API DE PAGOS V2


# **Integrantes**
+ Renato Gonzalo Cespedes Fuentes
+ Abel Esteban Orosco Segovia

## Documentacion
La Documentacion de la Api se encuentra en la ruta del host  /swagger/user (usuarios) y en la ruta /swagger/pagos (pagos v2), para más detalle observar el archivo [urls.py](/API_Payments/urls.py)



## Instalacion
Para instalar las dependencias necesarias se debe ejecutar el siguiente comando con python


```bash
  pip install -r requirements.txt
```
    
### Variables de la base de datos

Para correr este proyecto necesitas ir al archivo settings y cambiar las siguientes Variables por las Variables que usas en la base de datos.

`NAME` Nombre de la base de datos

`USER` Nombre de usuario de la base de datos

`PASSWORD` Contraseña de la base de datos, en caso no tenga dejarlo vacio

`HOST` Nombre del host a usar, exemplo: localhost

`PORT` puerto de la base de datos


### Hacer Migraciones
Para hacerlo ejecutamos los comandos

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py makemigrations users
  python manage.py migrate users
  python manage.py makemigrations payments
  python manage.py migrate payments
```
En caso de error borrar la carpeta **migration** que se encuentra en la carpeta **users** y **payments**. 
Y eliminar la base de datos que se usara

### Probar la aplicacion
Para hacerlo ejecutamos el comando:
```bash
  python manage.py runserver
```
Y al hacerlo usar la url  para probarla
