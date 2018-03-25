import os, sys, inspect, thread, time, socket
#import serial
#ser = serial.Serial(, 9600)
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))

arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'


sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class MyListener(Leap.Listener):

    def on_init(self, controller):
        print('itializing start up sequence')
    def on_connect(self, controller):
        print('Connected')

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
    def on_frame(self, controller):
        frame = controller.frame()
        #print "Frame available"
   # def cal_distance(vector1, vector2):
        # dist = 
        s2_out = "x"
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)
                if (circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2):
                    clockwiseness = "clockwise"
                    s2_out = "u"
                else:
                    clockwiseness = "counterclockwise"
                    s2_out = "d"
                #ser.write('Circle '+ clockwiseness)
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = CircleGesture(gesture)
                s2_out = "b"
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = CircleGesture(gesture)
                start = swipe.start_position
                current = swipe.position
                # direction = swipe.direction doesn't really work 
                s2_out = "l"
            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                s2_out = "f"
                    
        #if not (frame.hands.is_empty and frame.gestures().is_empty):
         #   print ""
        def state_string(self, state):
            if state == Leap.Gesture.STATE_START:
                return "STATE_START"
            if state == Leap.Gesture.STATE_UPDATE:
              return "STATE_UPDATE"
            if state == Leap.Gesture.STATE_INVALID:
                return "STATE_INVALID"
        return s2_out   
def main():
    listener = MyListener()
    controller = Leap.Controller()

    controller.add_listener(listener)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_addr = ('10.120.46.32', 1234)
    print >>sys.stderr, 'connection to %s port %s' % server_addr
   # sock.connect(server_addr)
    while True:
    # Create a TCP/IP socket
        sock.connect(server_addr)
        gesture = listener.on_frame(controller)
        sock.sendall(gesture)
        sock.close() 
    # cer.write('Press Enter to quit')
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)
if __name__ == "__main__":
    main()