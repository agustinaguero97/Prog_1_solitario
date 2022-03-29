from main import create_app
import os							#metodo que me permite cargar las variables de entorno en .env
app = create_app()
app.app_context().push()				#permitir que se puedan acceder a las propiedades de la app en cualquier parte

if __name__ == '__main__':
	app.run(port=os.getenv("PORT"),debug = True)   #debug permite mostrar cambios de manera activa


