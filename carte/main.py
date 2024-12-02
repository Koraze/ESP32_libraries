import machine

cause = machine.reset_cause()
if cause == machine.PWRON_RESET or cause == machine.HARD_RESET or cause == machine.DEEPSLEEP_RESET :
    print("launching main")
    exec(open("main_.py").read())