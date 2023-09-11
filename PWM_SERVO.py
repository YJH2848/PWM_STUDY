import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50) # 50hz
pwm.start(3.0) # 기본 초기값 0도

for cnt in range(0, 3):
    pwm.ChangeDutyCycle(3.0) # Servo 0도
    time.sleep(1.0)
    pwm.ChangeDutyCycle(7.5) # Servo 90도
    time.sleep(1.0)
    pwm.ChangeDutyCycle(12.5) # Servo 180도
    time.sleep(1.0)

pwm.ChangeDutyCycle(0.0) # Servo 정지

pwm.stop()
GPIO.cleanup()