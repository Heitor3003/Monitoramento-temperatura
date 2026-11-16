import serial

arduino = serial.Serial("COM5", 9600)

def ler_dados():
    try:
        arduino.reset_input_buffer()

        linha = arduino.readline().decode('utf8').strip()

        if "," in linha:
            temp, umid = linha.split(",")
        return float(temp), float(umid)

    except Exception as e:
        print("Erro na leitura serial:", e)
        
    return None, None

