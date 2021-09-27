import time, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

def selector(indice, elemento):
    elm = driver.find_element_by_id(f"asignarCitaForm:{elemento}")
    elm = Select(elm)
    elm.select_by_index(indice)

#export PATH=$PATH:/opt/WebDriver/bin >> ~/.profile
driver = webdriver.Firefox()

driver.get("https://enlinea.famisanar.com.co/Portal/home.jspx")

with open("secure.json") as json_file:
    data = json.load(json_file)
    cc = data['p'][0]['user']
    cl = data['p'][0]['pass']

    ususario = driver.find_element_by_name("loginForm:id")
    clave = driver.find_element_by_name("loginForm:clave")
    ususario.send_keys(cc)
    clave.send_keys(cl)
    time.sleep(2)

loginBtn = driver.find_element_by_name("loginForm:loginButton")
loginBtn.click()
time.sleep(2)

driver.get("https://enlinea.famisanar.com.co/Portal/pages/menu/welcome.jspx")
time.sleep(2)

afiliadoBtn = driver.find_element_by_class_name("itemMenu")
afiliadoBtn.click()

driver.get("https://enlinea.famisanar.com.co/Portal/pages/afiliado/consultarCitasMedicas.jspx")
time.sleep(1)

paciente = driver.find_element_by_id("ifAuto")
innerPage = paciente.get_attribute('src')
driver.get(innerPage)

time.sleep(1)
# Probablemente el elemento se hacia unclickeable desde la página por lo cual con el ActionChains, me permite
# hacer click sobre él directamente 
paciente2 = driver.find_element_by_id("generarReporteAutorizacionesXAfiliadoForm:resumenDataTable:1") # 0, para citas de mamá
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(paciente2).click(paciente2).perform()

solicitarBtn = driver.find_element_by_name("generarReporteAutorizacionesXAfiliadoForm:cmdsolicitar")
solicitarBtn.click()

# Formulario
selector(3, "especialidad")
selector(3, "consultaPor")
time.sleep(2)

selector(17, "centrosMed")
selector(2, "jornada")

btnConsultar = driver.find_element_by_id("asignarCitaForm:cmdAceptar")
btnConsultar.click()
time.sleep(2)

fechaPrimeraCita = driver.find_element_by_id("asignarCitaForm:citasDisponibles:0:_id58").text


contador = 0
while(fechaPrimeraCita != "28-09-2021"):
    btnConsultarNew = driver.find_element_by_id("asignarCitaForm:cmdAceptar")
    btnConsultarNew.click()
    try:
        fechaPrimeraCita = driver.find_element_by_id("asignarCitaForm:citasDisponibles:0:_id58").text
    except:
        fechaPrimeraCita = ""
    print(f"Consulta {contador}, {fechaPrimeraCita}")
    contador += 1
    time.sleep(3)
        
        
seleccionarCita = driver.find_element_by_id("asignarCitaForm:citasDisponibles:0")
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(seleccionarCita).click(seleccionarCita).perform()

asignarBtn = driver.find_element_by_id("asignarCitaForm:cmdaceptar")
asignarBtn.click()
print("Cita Asignada")

driver.close()