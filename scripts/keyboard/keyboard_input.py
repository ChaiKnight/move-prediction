#!/usr/bin/env python

import keyboard
import rospy
import getch
import random
import string
from geometry_msgs.msg import Vector3

INTERP_FACTOR = 1. / 15.  # publish at 30, so going from 1 to 0 takes .5 sec

interp_vec = Vector3()


def clamp(val, _min, _max):
    return max(min(val, _max), _min)


def publisher(interpolate):
    global interp_vec
    global INTERP_FACTOR
    
    pub = rospy.Publisher('keyboard/input', Vector3, queue_size=1)
    rate = rospy.Rate(30)
    
    out = Vector3()

    letters = string.ascii_lowercase + string.digits
    s = ''.join(random.choice(letters) for i in range(6))

    rospy.loginfo(s)
    with open('logs/' + s + '.txt', 'w') as _file:
        while not rospy.is_shutdown():
            if keyboard.is_pressed('esc'):
                rospy.signal_shutdown("Hooked keyboard is no longer needed")
            
            """ old code that allows multiple directions
            if keyboard.is_pressed(72):
                out.x = 1
            elif keyboard.is_pressed(76):
                out.x = -1
            else:
                out.x = 0
                
            if keyboard.is_pressed(75):
                out.y = 1
            elif keyboard.is_pressed(77):
                out.y = -1
            else:
                out.y = 0
            
            if keyboard.is_pressed(73):
                out.z = 1
            elif keyboard.is_pressed(71):
                out.z = -1
            else:
                out.z = 0
            """

            to_print = '0'
            
            out.x = 0.
            out.y = 0.
            out.z = 0.

            if keyboard.is_pressed(28):
                to_print='\n'
            elif keyboard.is_pressed(1):
                _file.close()
                rospy.signal_shutdown("finish logging")
            elif keyboard.is_pressed(72):
                to_print='8'
                out.x = 1
            elif keyboard.is_pressed(76):
                to_print='5'
                out.x = -1
            elif keyboard.is_pressed(75):
                to_print='4'
                out.y = 1
            elif keyboard.is_pressed(77):
                to_print='6'
                out.y = -1
            elif keyboard.is_pressed(73):
                to_print='9'
                out.z = 1
            elif keyboard.is_pressed(71):
                to_print='7'
                out.z = -1
                
            if interpolate:
                out.x = clamp(out.x, interp_vec.x - INTERP_FACTOR, interp_vec.x + INTERP_FACTOR)
                out.y = clamp(out.y, interp_vec.y - INTERP_FACTOR, interp_vec.y + INTERP_FACTOR)
                out.z = clamp(out.z, interp_vec.z - INTERP_FACTOR, interp_vec.z + INTERP_FACTOR)
                interp_vec.x = out.x
                interp_vec.y = out.y
                interp_vec.z = out.z
            
            _file.write(to_print)
            pub.publish(out)
            rate.sleep()
            
if __name__ == '__main__':
    try:
        rospy.init_node('keyboard_input', anonymous=False)
        publisher(True)
    except rospy.ROSInterruptException:
        pass
    
