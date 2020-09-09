import selenium
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import cycle

#Recordar que la variable en este caso se llamará "driver", con la que deberán trabajar los códigos.
#Existen ocasiones en las cuales la páginas necesita tiempo para cargar y si se realizan acciones demasiado rápido, se
#descoordina el programa y termina. Es recomendable en este caso usar #time.sleep(1) o los segundos que usted desee que espere.
	#driver.set_window_position(0,0)
	#driver.set_window_size(1920,1040)

def getAcc():
	acc = str(random.randrange(1000000,10000001)) + "xyz@test.com"
	return acc

def getRut():
	rut = random.randrange(10000000,25000001)
	return rut

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

#Creación de cuenta
def reg_dotCL():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	#pagina inicial chilena
	#driver.get("https://www.puntajenacional.cl")
	#pagina inicial española
	driver.get("https://puntajenacional.cl")
	time.sleep(5)
	#registrar
	boton0 = driver.find_element_by_xpath('//*[@id="section1"]/div/div[2]/div[2]/div/div[2]/div[1]/div/a[1]')
	#time.sleep(1)
	boton0.click()
	time.sleep(1)
	rutform = driver.find_element_by_xpath('//*[@id="rut"]')
	rut = getRut()
	digito = digito_verificador(rut)
	rutform.send_keys(str(rut)+str(digito_verificador(rut)))
	print('RUT utilizado: ' + str(rut)+'-'+str(digito_verificador(rut)))
	time.sleep(1)
	nombre = driver.find_element_by_xpath('//*[@id="nombre"]')
	nombre.send_keys('Pp')
	apellido = driver.find_element_by_xpath('//*[@id="apellido_paterno"]')
	apellido.send_keys('Cripto')
	time.sleep(1)
	enviar = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/shared-layout/div[2]/div/div/div[3]/div[2]/shared-layout-contenido/usuario-registro/form/div/button')
	enviar.click()
	time.sleep(3)
	email = driver.find_element_by_xpath('//*[@id="email"]')
	acc = getAcc()
	email.send_keys(acc)
	print('Email utilizado: ' + acc)
	time.sleep(1)
	contraseña = driver.find_element_by_xpath('//*[@id="password"]')
	pw0 = '0Test@Test'
	contraseña.send_keys(pw0)
	print('Contraseña utilizada: ' + pw0)
	confirmar = driver.find_element_by_xpath('//*[@id="password_confirmation"]')
	confirmar.send_keys(pw0)
	time.sleep(1)
	siguiente = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/shared-layout/div[2]/div/div/div[3]/div[2]/shared-layout-contenido/usuario-registro/form/div/button[2]')
	siguiente.click()
	time.sleep(3)
	egresado = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/shared-layout/div[2]/div/div/div[3]/div[2]/shared-layout-contenido/usuario-registro/form/form-input[1]/div[1]/div/div/label/span')
	egresado.click()
	terminos = driver.find_element_by_xpath('//*[@id="terminos_y_condiciones10"]')
	terminos.click()
	time.sleep(3)
	registrarse = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/shared-layout/div[2]/div/div/div[3]/div[2]/shared-layout-contenido/usuario-registro/form/div[2]/button[2]')
	time.sleep(1)
	registrarse.click()
	time.sleep(1)


	return driver

def log_dotCL(num):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://puntajenacional.cl")

	time.sleep(3)
	email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[1]/input')
	email.send_keys('cripto_throwaway@outlook.cl')
	print('Email utilizado: cripto_throwaway@outlook.cl')
	time.sleep(1)
	contraseña = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[2]/input')
	time.sleep(1)
	if num == 1:
		contraseña.send_keys(pw1)
		print('Contraseña utilizada: ' + pw1)
		ingresar = driver.find_element_by_xpath('//*[@id="btn-ingresar"]')
		time.sleep(1)
		ingresar.click()
	if num == 2:
		contraseña.send_keys(pw0)
		print('Contraseña utilizada: ' + pw0)
		ingresar = driver.find_element_by_xpath('//*[@id="btn-ingresar"]')
		time.sleep(1)
		ingresar.click()
	elif num == 3:
		contraseña.send_keys('0pw@incorrecta')
		print('Contraseña utilizada: 0pw@incorrecta')
		enviar = driver.find_element_by_xpath('//*[@id="btn-ingresar"]')
		for i in range(100):
			time.sleep(1)
			enviar.click()
	
	return driver

def pass_dotCL():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://puntajenacional.cl")

	time.sleep(3)
	recordar = driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/div[1]/div/p/a')
	time.sleep(1)
	recordar.click()
	time.sleep(3)
	email = driver.find_element_by_xpath('//*[@id="email"]')
	email.send_keys('cripto_throwaway@outlook.cl')
	time.sleep(1)
	continuar = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/simple-shared-layout/div/div[2]/simple-shared-layout-contenido/user-forgot-password/form/div[2]/button')
	continuar.click()
	time.sleep(2)
	boton = driver.find_element_by_xpath('/html/body/modal-container/div/div/div/div[2]/modal-contenido/div/input')
	time.sleep(1)
	boton.click()
	time.sleep(1)
	enviar = driver.find_element_by_xpath('/html/body/modal-container/div/div/div/div[3]/modal-botones/button')
	enviar.click()
	time.sleep(2)
	salir = driver.find_element_by_xpath('/html/body/modal-container/div/div/div/div[1]/button/span')
	salir.click()

	return driver

def mod_dotCL(camb):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://puntajenacional.cl")

	time.sleep(3)
	email = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[1]/input')
	email.send_keys('cripto_throwaway@outlook.cl')
	print('Email utilizado: cripto_throwaway@outlook.cl')
	time.sleep(1)
	contraseña = driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[2]/input')
	time.sleep(1)
	if int(camb) == 1:
		contraseña.send_keys(pw0)
		print('Contraseña utilizada: ' + pw0)
		
	elif int(camb) == 2:
		contraseña.send_keys(pw1)
		print('Contraseña utilizada: ' + pw1)
	ingresar = driver.find_element_by_xpath('//*[@id="btn-ingresar"]')
	time.sleep(1)
	ingresar.click()
	time.sleep(5)
	perfil = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/logged-layout/div/navbar/nav/div/div[2]/ul/li[4]/a/div/div[1]/fa/i')
	perfil.click()
	time.sleep(2)
	editar = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/logged-layout/div/navbar/nav/div/div[2]/ul/li[4]/ul/li[1]/a')
	editar.click()
	time.sleep(3)
	cambiar = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/logged-layout/div/div[1]/div/div/div[4]/logged-layout-contenido/usuarios-puntaje-edit/loading-layout/div/div/div/div[2]/button')
	cambiar.click()
	time.sleep(1)
	actual = driver.find_element_by_xpath('//*[@id="current_password"]')
	time.sleep(1)
	nueva = driver.find_element_by_xpath('//*[@id="password"]')
	time.sleep(1)
	confirm = driver.find_element_by_xpath('//*[@id="password_confirmation"]')
	time.sleep(1)
	if int(camb) == 1:
		actual.send_keys(pw0)
		print('Contraseña actual: ' + pw0)
		nueva.send_keys(pw1)
		print('Contraseña nueva: ' + pw1)
		confirm.send_keys(pw1)
	elif int(camb) == 2:
		actual.send_keys(pw1)
		print('Contraseña actual: ' + pw1)
		nueva.send_keys(pw0)
		print('Contraseña nueva: ' + pw0)
		confirm.send_keys(pw0)
	time.sleep(1)
	confirmar = driver.find_element_by_xpath('/html/body/puntaje/main-layout/div/ng-component/logged-layout/div/div[1]/div/div/div[4]/logged-layout-contenido/usuarios-puntaje-edit/loading-layout/div/div/div/div[2]/div/div/usuario-edit-password/button')
	time.sleep(1)
	confirmar.click()
	time.sleep(1)

	return driver

#reg_dotCL()
acc_ta = "cripto_throwaway@outlook.cl"

#pw0 original
pw0 = "0Test@Test"
pw1 = "1Test@Test"
pass_bool = 0
#print(acc)
#print(pw)
print('-- Seleccione la acción --')
print('1: Creación de una cuenta')
print('2: Inicio de sesión')
print('3: Login fuerza bruta (100 intentos)')
print('4: Restablecimiento de contraseña')
print('5: Modificación de contraseña')
num = int(input())
if num == 1:
	reg_dotCL()
elif num == 2:
	print("Si no ha modificado la contraseña, o la ha modificado un número par de veces, seleccione '1'. En otro caso seleccione '2'")
	camb = int(input())
	if camb == 1:
		log_dotCL(num)
	elif camb == 2:
		log_dotCL(1)
elif num == 3:
	log_dotCL(num)
elif num == 4:
	pass_dotCL()
elif num == 5:
	print("Si no ha modificado la contraseña, o la ha modificado un número par de veces, seleccione '1'. En otro caso seleccione '2'")
	camb = int(input())
	if camb == 1:
		mod_dotCL(camb)
	elif camb == 2:
		mod_dotCL(camb)

print('Finalización del programa.')
