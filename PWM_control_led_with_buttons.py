import RPi.GPIO as GPIO

def button_callback(channel):
    global led_state
    
    if led_state == False:
        print("LED ON")
        led_state = True
        pwm_led.ChangeDutyCycle(100)
    else:
        print("LED OFF")
        led_state = False
        pwm_led.ChangeDutyCycle(0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_pin = 20
led_state = False

GPIO.setup(led_pin, GPIO.OUT)
pwm_led = GPIO.PWM(led_pin, 50)
pwm_led.start(0)

GPIO.add_event_detect(21, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    while True:
        pass

except KeyboardInterrupt:
    # 프로그램 종료 시 GPIO 리소스 정리
    pwm_led.stop()
    GPIO.cleanup()
