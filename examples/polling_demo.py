from pyPS4Controller.controller import Controller
import time

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       print("Hello world")

    def on_x_release(self):
       print("Goodbye world")

    def on_timer(self):
        print("timer func2")

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.wait_for_interface()
controller.open()

while(1):
    # Process events that are 0.001 seconds apart all together
    while(event := controller.poll_events(0.001)):
        controller.process_event(event)

    print('doing something')
    time.sleep(0.1)

