#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('speech', String, queue_size=10)
    rospy.init_node('publishtext', anonymous=True)
    while not rospy.is_shutdown():
        hello_str = raw_input('input text:')
        rospy.loginfo(hello_str)
        pub.publish(hello_str)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
