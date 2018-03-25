import os, sys, inspect, thread, time, socket, requests, traceback
#import serial
#ser = serial.Serial(, 9600)
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'


sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class MyListener(Leap.Listener):

    def on_init(self, controller):
        print('initializing start up sequence')
    def on_connect(self, controller):
        print('Connected')
        '''
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)'''
    def on_frame(self, controller):
        time.sleep(.2)
        frame = controller.frame()
        hands = frame.hands
        hand = hands[0]
        palm = hand.palm_normal
        y = palm.y
        z = palm.z
        
        s2_out = "x"
        # up and down
        print str(z)+", "+str(y)
        if y < z*1.5:
            s2_out = 'd'
        elif z == 0 and y == 0:
            s2_out = 'x'
        else:
            s2_out = 'u'
        # sphere_diameter = 2 * hand.sphere_radius
        # print sphere_diameter
        '''
        if (sphere_diameter > 90):
            s2_out = 'u'
        elif (sphere_diameter <= 90):
            s2_out = 'd'
        
        if sphere_diameter == 0:
            s2_out = 'x'
        '''
        return s2_out
                    
    #if not (frame.hands.is_empty and frame.gestures().is_empty):
        #   print ""
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
    # Connect the socket to the port where the server is listening
    data = requests.get('https://raw.githubusercontent.com/grandtissue/quadmotion/master/ip')
    ip = str(data.text)
    # print >>sys.stderr, 'connection to %s port %s' % server_addr
    while True:
        time.sleep(.1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = (ip, 1234)
        sock.connect(server_addr)
        try:
    # Create a TCP/IP socket
            gesture = listener.on_frame(controller)
            print gesture   
            sock.sendall(gesture)
            if gesture == 'o':
                sys.exit()
        # sock.close() 
    # cer.write('Press Enter to quit')
        except Exception as e:
            print("EXCEPT: " + traceback.print_tb(*sys.exc_info()))
            continue
if __name__ == "__main__":
    main()
