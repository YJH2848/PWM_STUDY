import RPi.GPIO as GPIO

# GPIO 핀 번호 설정
button_pin = 21

def button_callback(channel):
    print("안녕")

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀을 입력으로 설정하고 Pull-up 저항 활성화
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 버튼 이벤트에 대한 콜백 함수 등록
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

try:
    while True:
        pass

except KeyboardInterrupt:
    # 프로그램 종료 시 GPIO 리소스 정리
    GPIO.cleanup()
