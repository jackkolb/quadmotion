import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))

arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'


sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class MyListener(Leap.Listener):
    def on_init(self, controller):
        print "itializing start up sequence"
    def on_connect(self, controller):
        print "Connected"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
    def on_frame(self, controller):
        frame = controller.frame()
        print "Frame available"

        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)
                print "Circle"
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = CircleGesture(gesture)
                print "Key Tap"
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = CircleGesture(gesture)
                print "Swipe"
            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                swipe = CircleGesture(gesture)
                print "Screen Tap"
    # need to add clock/counterwise implementation
        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""
    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"
        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"
        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"


def main():
    listener = MyListener()
    controller = Leap.Controller()

    controller.add_listener(listener)

    print "Press Enter to quit"
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)
if __name__ == "__main__":
    main()