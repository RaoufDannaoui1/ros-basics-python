#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty, EmptyResponse
from std_msgs.msg import Empty as EEE

def motion_service_callback(req):
    rospy.loginfo("Motion service called. Initiating the movement...")

    rospy.logwarn("Taking Off...")
    # Publish the Empty message to initiate takeoff
    takeOff_pub.publish(EEE())
    time.sleep(3)


    for _ in range(10):
        rospy.loginfo("Going back...")
        time.sleep(1)  # Sleep for 1 second

    # ############################################################################
    for _ in range(4):
        rospy.logwarn("Moving forward...")
        move_msg.linear.x = 0.8
        move_msg.angular.z = 0
        move_pub.publish(move_msg)
        time.sleep(2.5)

        rospy.logwarn("Rotating...")
        move_msg.linear.x = 0
        move_msg.angular.z = 0.4
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
    land_pub.publish(EEE())

    # Return an EmptyResponse to indicate a successful execution of the service
    return EmptyResponse()

rospy.init_node('motion_service_node')
service = rospy.Service('/motion_service', Empty, motion_service_callback)
move_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # Create a Publisher to move the drone
takeOff_pub = rospy.Publisher('/takeoff', EEE, queue_size=1)
land_pub = rospy.Publisher('/land', EEE, queue_size=1) 
move_msg = Twist()  # Create the message to move the drone
takeoff_msg = EEE() # Create the message to takeoff the drone
land_msg = EEE() # Create the message to land the drone

time.sleep(3)
rospy.loginfo("Motion service is ready.")
rospy.spin()
