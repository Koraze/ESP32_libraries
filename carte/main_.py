import machine

exec(open("./exemple/reset_neopixel.py").read())
if cause == machine.PWRON_RESET or cause == machine.HARD_RESET or cause == machine.DEEPSLEEP_RESET :
    print("launching main")
    exec(open("./exemple/mqtt_ha.py").read())
