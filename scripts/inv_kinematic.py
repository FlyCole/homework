#!/usr/bin/env python

"""
    inv_kinematic.py - move robot arm according to predefined gestures

"""

import rospy
import math
from std_msgs.msg import Float64


class inv_kinematic():
    def __init__(self, x, y):
        rospy.on_shutdown(self.cleanup)
        self.x = x
        self.y = y
        self.l1 = .145
        self.l2 = .15
        self.theta1 = 0.0
        self.theta2 = 0.0
        self.theta3 = 0.0

        self.joint2 = rospy.Publisher('/shoulder_controller/command', Float64, queue_size=15)
        self.joint3 = rospy.Publisher('/elbow_controller/command', Float64, queue_size=15)
        self.joint4 = rospy.Publisher('/wrist_controller/command', Float64, queue_size=15)

        # Initial gesture of robot arm
        self.pos1 = 1.565
        self.pos2 = 2.102
        self.pos3 = -2.439
        self.pos4 = -1.294
        self.pos5 = 0.0
        self.joint2.publish(self.pos2)
        self.joint3.publish(self.pos3)
        self.joint4.publish(self.pos4)

        self.cal_theta2()
        self.cal_theta1()

        while 1:
            self.joint2.publish(self.theta1)
            self.joint3.publish(self.theta2)
            self.joint4.publish(self.theta3)
            print self.theta1
            print self.theta2
            print self.theta3
            rospy.sleep(0.1)


        print self.theta1
        print self.theta2
        print self.theta3



    def cal_theta2(self):
        c2 = (self.x ** 2 + self.y ** 2 - self.l1 ** 2 - self.l2 ** 2) / (2 * self.l1 * self.l2)
        self.theta2 = math.acos(c2)

    def cal_theta1(self):
        k = -self.x / math.sqrt((self.l2 * math.sin(self.theta2)) ** 2 + (self.l1 + self.l2 * math.cos(self.theta2)) ** 2)
        gama = math.atan2(self.l1 + self.l2 * math.cos(self.theta2), self.l2 * math.sin(self.theta2))
        self.theta1 = gama + math.asin(k)
        #self.theta1 = math.atan2(self.y, self.x) - math.acos((self.l1 ** 2 - self.l2 ** 2 + (self.x ** 2 + self.y ** 2)) / (2 * self.l1 * math.sqrt(self.x ** 2 + self.y ** 2)))


    def cleanup(self):
        rospy.loginfo("Shutting down robot arm....")


if __name__ == "__main__":
    rospy.init_node('arm')
    x = .1
    y = .1
    try:
        inv_kinematic(x, y)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
