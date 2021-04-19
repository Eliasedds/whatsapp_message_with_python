from datetime import date, datetime
import pywhatkit as kit

print("-"*30)

x = 1
while x < 2:
    print("Hola, soy Juancho tu ayudante para enviar mensajes")

    contacts = {'papa':"+584145177288",'mama':"+584140727383", 'paul':"+5491135137095",
                'emi':"+5491131414249", 'samy':'+5491132891480', 'cande':'+5491173673595'}
    try:
        for contact in contacts.keys():
            print(contact)
    except KeyError:
        print('Contacto no encontrado')

    selected_contact = input("¿Cual de sus contactos desea enviarle un mensaje: ")
    message = input("Inserte el mensaje que quiere enviar:\n")

    now = datetime.now()
    hour, minute = now.hour, now.minute
    print("Actualmente son las " + str(hour) + ":" + str(minute))
    user_hour = int(input("Dentro de cuantas horas lo quiere enviar:\n"))
    user_minute = int(input("Dentro de cuantos minutos quiere enviar el mensaje:\n"))
    hour_message = hour + user_hour
    minute_message = minute + user_minute

    try:
        kit.sendwhatmsg(contact[selected_contact], message, hour_message, minute_message)
        print("Mensaje enviado con exito")
    except:
        print("Error al enviar el mensaje")

    x = int(input("Desea continuar\n1. SI \n2. NO\n(Seleccione el número de la acción deseada)\n\t"))

print("Chao! Ha sido un placer ayudarte")
print("-"*30)
