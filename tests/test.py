from time import sleep
import power_terminal as terminal


terminal.clear()

terminal.introduction("Power Terminal", "0.0.5")

terminal.debug("It's ALIVE!!!!!!!!!")

terminal.ask("Or is it?")

terminal.statement("It IS alive!")

terminal.error("It's dead :(")

sleep(3)


for i in range(0, 100):
    terminal.clear()
    terminal.progress(i + 1, 100, string="Progress: ", fill="█", empty=" ")
    sleep(0.01)
