import speech_recognition as sr
# referenze libreria: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#speech-recognition-library-reference

recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

text = ""


def avanti():
    print("robot avanti")


def indietro():
    print("robot indietro")



while(text != "esci"):
    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        print("Sono in ascolto... parla pure!")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        print("Google ha capito: \n", text)
        if (text == "esci"):
             break
        if (text =="avanti"):
            avanti()
        if (text =="indietro"):
            indietro()
    except Exception as e:
         print(e)




