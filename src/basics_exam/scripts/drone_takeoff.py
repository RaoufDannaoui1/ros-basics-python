#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty

rospy.init_node('drone_takeoff_node', anonymous=True)
pub = rospy.Publisher('/takeoff', Empty, queue_size=1)
rospy.loginfo("Publishing Ready...")
rospy.sleep(5)

rospy.loginfo("Taking Off...")
pub_msg = Empty()
pub.publish(pub_msg)

rospy.spin()

    