import selenium
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Recordar que la variable en este caso se llamará "driver", con la que deberán trabajar los códigos.
#Existen ocasiones en las cuales la páginas necesita tiempo para cargar y si se realizan acciones demasiado rápido, se
#descoordina el programa y termina. Es recomendable en este caso usar #time.sleep(1) o los segundos que usted desee que espere.
	#driver.set_window_position(0,0)
	#driver.set_window_size(1920,1040)

def getAcc():
	acc = str(random.randrange(1000000,10000001)) + "xyz@test.com"
	return acc

#Creación de cuenta
def reg_dotES():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	#pagina inicial chilena
	#driver.get("https://www.puntajenacional.cl")
	#pagina inicial española
	driver.get("https://estrellagalicia.es")
	time.sleep(3)
	#+18
	boton0 = driver.find_element_by_id('wpsp-continue')
	#time.sleep(1)
	boton0.click()
	time.sleep(3)
	#scroll
	driver.execute_script("window.scrollTo(0, 500)") 
	#time.sleep(1)
	#tienda
	boton1 = driver.find_element_by_xpath('//*[@id="menu-item-4096"]/a')
	#time.sleep(1)
	boton1.click()
	time.sleep(3)
	#+18
	boton2 = driver.find_element_by_class_name('swal2-confirm.swal2-styled')
	#time.sleep(1)
	boton2.click()
	time.sleep(3)
	#notif
	boton3 = driver.find_element_by_class_name('align-right.secondary.slidedown-button')
	#time.sleep(1)
	boton3.click()
	time.sleep(3)
	#perfil
	cuenta = driver.find_element_by_xpath('//*[@id="masthead"]/nav/div[1]/a')
	#time.sleep(1)
	cuenta.click()
	time.sleep(3)
	#crear
	boton4 = driver.find_element_by_link_text('¿Aún no tiene una cuenta?')
	time.sleep(1)
	boton4.click()
	time.sleep(3)
	#correo
	box0 = driver.find_element_by_xpath('//*[@id="register-site-login"]/div[1]/div[1]/div/input')
	time.sleep(1)
	acc = getAcc()
	box0.send_keys(acc)
	print('Email utilizado: ' + acc)
	#time.sleep(3)
	#nombre
	box1 = driver.find_element_by_xpath('//*[@id="gigya-textbox-104976479773255180"]')
	time.sleep(1)
	box1.send_keys('Pp')
	#apellido1
	box2 = driver.find_element_by_xpath('//*[@id="register-site-login"]/div[2]/div[1]/div/input')
	time.sleep(1)
	box2.send_keys('Cripto')
	#apellido2
	box3 = driver.find_element_by_xpath('//*[@id="register-site-login"]/div[2]/div[2]/div/input')
	time.sleep(1)
	box3.send_keys('Redes')
	#PW
	box4 = driver.find_element_by_xpath('//*[@id="password-row"]/div[1]/div/input')
	time.sleep(1)
	box4.send_keys(pw0)
	print('Contraseña utilizada: ' + pw0)
	#PWconfirm
	box5 = driver.find_element_by_xpath('//*[@id="password-row"]/div[2]/div/input')
	time.sleep(1)
	box5.send_keys(pw0)
	#Enviar
	boton5 = driver.find_element_by_xpath('//*[@id="register-site-login"]/div[4]/input')
	time.sleep(1)
	boton5.click()

	return driver

#Inicio de sesión
def log_dotES(num):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://estrellagalicia.es/tienda/mi-cuenta/")
	
	time.sleep(3)
	#+18
	boton0 = driver.find_element_by_class_name('swal2-confirm.swal2-styled')
	#time.sleep(1)
	boton0.click()
	time.sleep(3)
	#notif
	boton1 = driver.find_element_by_class_name('align-right.secondary.slidedown-button')
	#time.sleep(1)
	boton1.click()
	logacc = driver.find_element_by_xpath('//*[@id="gigya-loginID-28293776870068580"]')
	time.sleep(1)
	logacc.send_keys('cripto_throwaway@outlook.cl')
	print('Correo utilizado: cripto_throwaway@outlook.cl')
	logpw = driver.find_element_by_xpath('//*[@id="gigya-password-35214771101447810"]')
	time.sleep(1)
	if num == 1:
		logpw.send_keys(pw1)
		print('Contraseña utilizada: ' + pw1)
		enviar = driver.find_element_by_xpath('//*[@id="gigya-login-form"]/div[2]/div[3]/div[4]/input')
		time.sleep(1)
		enviar.click()
	if num == 2:
		logpw.send_keys(pw0)
		print('Contraseña utilizada: ' + pw0)
		enviar = driver.find_element_by_xpath('//*[@id="gigya-login-form"]/div[2]/div[3]/div[4]/input')
		time.sleep(1)
		enviar.click()
	elif num == 3:
		logpw.send_keys('0pw@incorrecta')
		print('Contraseña utilizada: 0pw@incorrecta')
		enviar = driver.find_element_by_xpath('//*[@id="gigya-login-form"]/div[2]/div[3]/div[4]/input')
		for i in range(100):
			time.sleep(1)
			enviar.click()

	return driver

#Restablecimiento de contraseña
def pass_dotES():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://estrellagalicia.es/tienda/mi-cuenta/")
	#
	time.sleep(3)
	#+18
	boton0 = driver.find_element_by_class_name('swal2-confirm.swal2-styled')
	#time.sleep(1)
	boton0.click()
	time.sleep(3)
	#notif
	boton1 = driver.find_element_by_class_name('align-right.secondary.slidedown-button')
	#time.sleep(1)
	boton1.click()
	time.sleep(1)
	boton2 = driver.find_element_by_link_text('este enlace')
	time.sleep(1)
	boton2.click()
	time.sleep(3)
	email = driver.find_element_by_xpath('//*[@id="gigya-textbox-loginID"]')
	time.sleep(1)
	email.send_keys('cripto_throwaway@outlook.cl')
	print('Correo utilizado: cripto_throwaway@outlook.cl')

	boton3 = driver.find_element_by_xpath('//*[@id="gigya-reset-password-form"]/div[2]/div[1]/input')
	time.sleep(1)
	boton3.click()

	return driver

#Modificación de contraseña
def mod_dotES(camb):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://estrellagalicia.es/tienda/mi-cuenta/")
	#
	time.sleep(3)
	#+18
	boton0 = driver.find_element_by_class_name('swal2-confirm.swal2-styled')
	#time.sleep(1)
	boton0.click()
	time.sleep(3)
	#notif
	boton1 = driver.find_element_by_class_name('align-right.secondary.slidedown-button')
	#time.sleep(1)
	boton1.click()
	logacc = driver.find_element_by_xpath('//*[@id="gigya-loginID-28293776870068580"]')
	time.sleep(1)
	logacc.send_keys('cripto_throwaway@outlook.cl')
	print('Correo utilizado: cripto_throwaway@outlook.cl')
	logpw = driver.find_element_by_xpath('//*[@id="gigya-password-35214771101447810"]')
	time.sleep(1)
	if int(camb) == 1:
		logpw.send_keys(pw0)
		print('Contraseña utilizada: ' + pw0)
	elif int(camb) == 2:
		logpw.send_keys(pw1)
		print('Contraseña utilizada: ' + pw1)
	enviar = driver.find_element_by_xpath('//*[@id="gigya-login-form"]/div[2]/div[3]/div[4]/input')
	time.sleep(1)
	enviar.click()
	#espera larga debido a que no encuentro el elemento con tiempos "normales" (respecto a los usados)
	time.sleep(10)
	detalles = driver.find_element_by_xpath('//*[@id="post-291"]/div/div[1]/div/div[2]/nav/ul/li[4]/a')
	time.sleep(1)
	detalles.click()
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, 300)") 
	time.sleep(1)
	cambiar = driver.find_element_by_xpath('//*[@id="gigya-profile-form"]/div[4]/a')
	time.sleep(1)
	cambiar.click()
	time.sleep(3)
	actual = driver.find_element_by_xpath('//*[@id="gigya-password-password"]')
	time.sleep(1)
	nueva = driver.find_element_by_xpath('//*[@id="gigya-password-newPassword"]')
	time.sleep(1)
	confirm = driver.find_element_by_xpath('//*[@id="gigya-passsord-passwordRetype"]')
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
	enviar = driver.find_element_by_xpath('//*[@id="gigya-profile-form"]/div[5]/div/input')
	time.sleep(1)
	enviar.click()


	return driver

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
	reg_dotES()
elif num == 2:
	print("Si no ha modificado la contraseña, o la ha modificado un número par de veces, seleccione '1'. En otro caso seleccione '2'")
	camb = int(input())
	if camb == 1:
		log_dotES(num)
	elif camb == 2:
		log_dotES(1)
elif num == 3:
	log_dotES(num)
elif num == 4:
	pass_dotES()
elif num == 5:
	print("Si no ha modificado la contraseña, o la ha modificado un número par de veces, seleccione '1'. En otro caso seleccione '2'")
	camb = int(input())
	if camb == 1:
		mod_dotES(camb)
	elif camb == 2:
		mod_dotES(camb)

print('Finalización del programa.')
