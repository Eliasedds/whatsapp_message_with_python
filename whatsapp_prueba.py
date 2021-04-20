from datetime import date, datetime
import pywhatkit as kit
    
def buscar_contacto(contactos:dict):
    for contacto in contactos.keys():
        print(contacto.capitalize())
    
    contacto_seleccionado = input("¿Cual de sus contactos desea enviarle un mensaje: ")
    assert contacto_seleccionado in contactos.keys(), 'El contacto no esta en la agenda'
    contacto_seleccionado = contacto_seleccionado.lower().strip()
    
    return contacto_seleccionado    
    
def redaccion_mensaje():
    mensaje = input("Inserte el mensaje que quiere enviar:\n")
    return mensaje

def hora_mensaje():
    ahora = datetime.now()
    hora, minuto = ahora.hour, ahora.minute
    print("Actualmente son las " + str(hora) + ":" + str(minuto))
    hora_usuario = int(input("Dentro de cuantas horas lo quiere enviar:\n"))
    assert hora_usuario >= 0, 'La hora ingresa no puede ser negativa'
    minuto_usuario = int(input("Dentro de cuantos minutos quiere enviar el mensaje:\n"))
    assert minuto_usuario >= 0, 'Los minutos ingresados no pueden ser negativos' 
    hora_mensaje = hora + hora_usuario
    minuto_mensaje = minuto + minuto_usuario
    return [hora_mensaje, minuto_mensaje]

def mensaje_a_enviar(contactos:dict, contacto:str, mensaje:str, hora:int, minuto:int):
    try:
        print(f'El mensaje será enviado a las {hora}:{minuto}')
        kit.sendwhatmsg(contactos[contacto], mensaje, hora, minuto)
        print("Mensaje enviado con exito")
    except:
        print("Error al enviar el mensaje")


def run():
    print("-"*30)

    contactos = {'contacto_1':"+########",'contacto_2':"+############", 'contacto_3':"+###########"}

    x = 1
    while x < 2:
        print("Hola, soy Juancho tu ayudante para enviar mensajes")
    
        contacto = buscar_contacto(contactos)
        mensaje = redaccion_mensaje()
        hora, minuto = hora_mensaje()
        mensaje_a_enviar(contactos, contacto, mensaje, hora, minuto)

        x = int(input("Desea continuar\n1. SI \n2. NO\n(Seleccione el número de la acción deseada)\n"))

    print("Chao! Ha sido un placer ayudarte")
    print("-"*30)

if __name__ == '__main__':
    run()