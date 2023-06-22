import time
from datetime import timedelta

from reciprocal import Action
from reciprocal import Menu
from reciprocal import WaitingAction


# Waiting actions

options: list[Action] = [
    WaitingAction("I feel like waiting a year", "Waiting{animation}", timeout=timedelta(days=365)),
    WaitingAction("I feel like waiting a couple of years", "Waiting{animation}", timeout=timedelta(days=365 * 2)),
    WaitingAction("I feel like waiting for eternity", "Waiting{animation}", timeout=0),
]

menu = Menu("Root menu", options)

waiting_action = menu.execute()

time.sleep(4)
waiting_action.send("Haha, just kidding! Just a few more seconds")
time.sleep(3)
waiting_action.send("Done!")
waiting_action.done()
