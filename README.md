# Tercera_preentrega_DeLaVarga
Tercera pre-entrega De La Varga Ramiro 43865

Para usar la aplicación sigue estos pasos:

Configuración del entorno:

Tener Python instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python (https://www.python.org/downloads/).
Instala Django en tu entorno virtual. Puedes hacerlo mediante el comando pip install django.
Descarga y prepara el proyecto:

Descarga los archivos del proyecto a tu máquina local y descomprímelos si es necesario.
Abre una terminal o línea de comandos y navega al directorio raíz del proyecto.
Configura la base de datos:

Abre el archivo settings.py dentro del directorio miapp3.
Asegúrate de configurar la base de datos según tus preferencias (por defecto, está configurado para utilizar SQLite, que es una base de datos ligera incluida con Django).
Aplica las migraciones:

En la terminal, ejecuta el siguiente comando para aplicar las migraciones y crear las tablas necesarias en la base de datos: python manage.py migrate.
Crea un superusuario (opcional):

Si deseas acceder al panel de administración de Django, puedes crear un superusuario utilizando el siguiente comando: python manage.py createsuperuser.
Sigue las instrucciones para ingresar un nombre de usuario, dirección de correo electrónico y contraseña.
Ejecuta el servidor de desarrollo:

Inicia el servidor de desarrollo de Django con el siguiente comando: python manage.py runserver.
El servidor estará disponible en http://localhost:8000/.
Accede a la aplicación:

Abre tu navegador web y navega a http://localhost:8000/.
Verás la página de inicio de la aplicación, con enlaces para registrar clientes, productos, realizar pedidos y buscar.
Registra un cliente:

Haz clic en el enlace "Clientes".
Serás dirigido a la página de registro de clientes.
Completa el formulario con la información del cliente y haz clic en "Guardar".
Registra un producto:

Haz clic en el enlace "Producto".
Serás dirigido a la página de registro de productos.
Completa el formulario con la información del producto y haz clic en "Guardar".
Realiza un pedido:

Haz clic en el enlace "Pedido".
Serás dirigido a la página de registro de pedidos.
Selecciona un cliente y un producto, ingresa la cantidad y haz clic en "Guardar".
Realiza una búsqueda:

Haz clic en el enlace "Buscar".
Serás dirigido a la página de búsqueda.
Ingresa un término de búsqueda y haz clic en "Buscar".
Verás los resultados de la búsqueda para clientes y productos.

Ahora puedes utilizar la aplicación para registrar clientes, productos, realizar pedidos y buscar información. Puedes acceder al panel de administración de Django en http://localhost:8000/admin/ utilizando las credenciales del superusuario si necesitas administrar los registros de la base de datos directamente.





