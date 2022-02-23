from time import sleep
import power_terminal as terminal


terminal.clear()

terminal.countdown("Starting in...", 1000)

terminal.introduction("Power Terminal", "0.0.7")

sleep(0.3)


terminal.debug("It's ALIVE!!!!!!!!!")

sleep(0.3)

terminal.ask("Or is it?")

sleep(0.3)


terminal.statement("It IS alive!")

sleep(0.3)

terminal.error("It's dead :(")

sleep(1)


for i in range(0, 100):
    terminal.clear()
    terminal.progress(
        i + 1, 100, string="No, it just needs a second.", fill="█", empty=" ")
    sleep(0.01)

alive = terminal.confirm("Is it alive?", "You must answer y or n")

if alive:
    terminal.statement("IT'S ALIIIIIVEEEEEE!!!!!!!!!!!!!!")
else:
    terminal.error("It's dead =|")
