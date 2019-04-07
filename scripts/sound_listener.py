#!/usr/bin/env python
#import roslib; roslib.load_manifest('sound_yak')
import rospy,os,sys
from sound_play.msg import SoundRequest
#from sound_yak.msg import yak_cmd
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data)
    soundhandle = SoundClient()

    rospy.sleep(1)
    #soundhandle.stopAll()

    text = data.data
    voice = 'voice_kal_diphone'
    volume = 1.0
    print 'Saying: %s' % text
    print 'Voice: %s' % voice
    print 'Volume: %s' % volume
    soundhandle.say(text)
    rospy.sleep(1)

def listener():
    rospy.init_node('say', anonymous=True)
    rospy.Subscriber('speech', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

    print "This script will runcontinuously until you hit CTRL+C, testing various sound_node sound types."

    
