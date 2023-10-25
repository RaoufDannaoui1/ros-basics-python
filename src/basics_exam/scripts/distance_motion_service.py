#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from basics_exam.srv import DistanceMotionMessage, DistanceMotionMessageResponse
# from std_srvs.srv import Empty as EEE
from std_msgs.msg import Empty

def motion_service_callback(req):
    rospy.loginfo("Motion service called. Initiating the movement...")

    rospy.loginfo("Taking Off...")
    # Publish the Empty message to initiate takeoff
    takeOff_pub.publish(takeoff_msg)
    rospy.sleep(3)

    distance_moved = 0.0  # Initialize the distance moved variable

    for _ in range(10):
        rospy.loginfo("Going back...")
        rospy.sleep(1)  # Sleep for 1 second

    # ############################################################################
    for _ in range(4):
        rospy.loginfo("Moving forward...")
        move_msg.linear.x = 0.8
        move_msg.angular.z = 0
        move_pub.publish(move_msg)
        rospy.sleep(2.5)

        # Calculate and accumulate the distance moved in the x-axis
        distance_moved += 0.8 * 2.5  # Velocity * time

        rospy.loginfo("Rotating...")
        move_msg.linear.x = 0
        move_msg.angular.z = 0.4
        move_pub.publish(move_msg)
        rospy.sleep(3.927)
    # ############################################################################

    # ############################################################################
    rospy.loginfo("Stopping...")
    move_msg.linear.x = 0
    move_msg.angular.z = 0
    move_pub.publish(move_msg)
    rospy.sleep(3)

    rospy.loginfo("Landing...")
    # Publish the Empty message to the /land topic
    land_pub.publish(land_msg)

    # Return a response with the distance moved in the x-axis and success flag
    response = DistanceMotionMessageResponse()
    response.success = True
    response.message = f"The drone has moved {distance_moved} meters."

    return response

rospy.init_node('dist_motion_service_node')
service = rospy.Service('/dist_motion_service', DistanceMotionMessage, motion_service_callback)
move_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # Create a Publisher to move the drone
takeOff_pub = rospy.Publisher('/takeoff', Empty, queue_size=1)
land_pub = rospy.Publisher('/land', Empty, queue_size=1) 
move_msg = Twist()  # Create the message to move the drone
takeoff_msg = Empty() # Create the message to takeoff the drone
land_msg = Empty() # Create the message to land the drone

rospy.sleep(3)
rospy.loginfo("Distance Motion service is ready.")
rospy.spin()
