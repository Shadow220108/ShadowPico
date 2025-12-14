from machine import Pin, PWM
import utime

btn_up = Pin(4, Pin.IN, Pin.PULL_UP)
btn_down = Pin(5, Pin.IN, Pin.PULL_UP)
btn_left = Pin(3, Pin.IN, Pin.PULL_UP)
btn_right = Pin(2, Pin.IN, Pin.PULL_UP)

btn_a = Pin(7, Pin.IN, Pin.PULL_UP)
btn_b = Pin(6, Pin.IN, Pin.PULL_UP)
btn_x = Pin(9, Pin.IN, Pin.PULL_UP)
btn_y = Pin(8, Pin.IN, Pin.PULL_UP)

led_user = Pin(22, Pin.OUT)
buzzer = Pin(15, Pin.OUT)


def beep(duration_ms):
    buzzer.value(1)
    led_user.value(1)
    utime.sleep_ms(duration_ms)
    buzzer.value(0)
    led_user.value(0)


print("--- CYBERDECK SYSTEM START ---")
print("Press any button to test...")

beep(50)
utime.sleep_ms(100)
beep(50)

while True:
    if btn_up.value() == 0:
        print("UP Pressed")
        beep(20)
        while btn_up.value() == 0: pass

    if btn_down.value() == 0:
        print("DOWN Pressed")
        beep(20)
        while btn_down.value() == 0: pass

    if btn_left.value() == 0:
        print("LEFT Pressed")
        beep(20)
        while btn_left.value() == 0: pass

    if btn_right.value() == 0:
        print("RIGHT Pressed")
        beep(20)
        while btn_right.value() == 0: pass

    if btn_a.value() == 0:
        print("A Button Pressed")
        beep(50)
        while btn_a.value() == 0: pass

    if btn_b.value() == 0:
        print("B Button Pressed")
        beep(50)
        while btn_b.value() == 0: pass

    if btn_x.value() == 0:
        print("X Button Pressed")
        beep(50)
        while btn_x.value() == 0: pass

    if btn_y.value() == 0:
        print("Y Button Pressed")
        beep(50)
        while btn_y.value() == 0: pass

    utime.sleep_ms(10)