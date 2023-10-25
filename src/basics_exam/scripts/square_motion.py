#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


rospy.init_node('squre_motion_node')

move_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # Create a Publisher to move the drone
takeOff_pub = rospy.Publisher('/takeoff', Empty, queue_size=1)
land_pub = rospy.Publisher('/land', Empty, queue_size=1) 
time.sleep(3)

move_msg = Twist()  # Create the message to move the drone
takeoff_msg = Empty() #Create the message to takeoff the drone
land_msg = Empty() #Create the message to land the drone

rospy.logwarn("Taking Off...")
# Publish the Empty message to initiate takeoff
takeOff_pub.publish(Empty())
time.sleep(3)


for _ in range(10):
    rospy.loginfo("Going back...")
    time.sleep(1)  # Sleep for 1 second

# ############################################################################
for _ in range(4):
    rospy.logwarn("Moving forward...")
    move_msg.linear.x = 0.8 # forward speed = 0.8 m/s for 2.5s it will go 0.8*2.5 = 2 meters
    move_msg.angular.z = 0
    move_pub.publish(move_msg)
    time.sleep(2.5)

    rospy.logwarn("Rotating...")
    move_msg.linear.x = 0
    move_msg.angular.z = 0.4 # angular speed = 0.4 rad/s for 3.927 it will go 0.4*3.927 = 1.5708 rad ~ 90 degrees
    move_pub.publish(move_msg)
    time.sleep(3.927)
# ############################################################################

# ############################################################################
rospy.logfatal("Stopping...")
move_msg.linear.x = 0
move_msg.angular.z = 0
move_pub.publish(move_msg)
time.sleep(3)

rospy.logfatal("Landing...")
# Publish the Empty message to the /land topic
land_pub.publish(Empty())