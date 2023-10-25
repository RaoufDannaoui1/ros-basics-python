#! /usr/bin/env python

import rospy
# from std_msgs.msg import Int32 
from std_msgs.msg import Odometry 

def callback(msg): 
    print(msg) #This will print the whole Odometry message
    # print(msg.header) #This will print the header section of the Odometry message
    # print(msg.pose) # #This will print the pose section of the Odometry message
    # rospy.init_node('topic_subscriber')
    
rospy.init_node('topic_subscriber')
# sub = rospy.Subscriber('/odom', Int32, callback)
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()