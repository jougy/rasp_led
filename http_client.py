from flask import Flask
import rasp_led as led

app = Flask(__name__)

@app.route('/')
def hello_world():
    humidity, temperature = led.get_hum_temp()
    return "umidade: {}\ntemperatura: {}C".format(humidity,temperature)

@app.route('/ligar')
def ligar():
    led.high()
    return 'led ligado'

@app.route('/desligar')
def desligar():
    led.low()
    return 'led desligado'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)