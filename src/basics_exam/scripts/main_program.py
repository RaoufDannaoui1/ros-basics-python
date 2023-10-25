#! /usr/bin/env python

import rospy
from basics_exam.srv import DistanceMotionMessage, DistanceMotionMessageResponse, DistanceMotionMessageRequest # you import the service message python classes generated from Empty.srv.
from basics_exam.msg import RecordPoseFeedback, RecordPoseAction, RecordPoseResult, RecordPoseGoal
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty as Empty_msg
from std_srvs.srv import Empty, EmptyRequest
import actionlib
from geometry_msgs.msg import Twist

goal = RecordPoseGoal
finished = False

rospy.init_node("main_node")
rate = rospy.Rate(10)
rospy.sleep(0.5)
record_odom_client = actionlib.SimpleActionClient('/rec_pose_as',RecordPoseAction)
rospy.loginfo("waiting for ACTION server")
record_odom_client.wait_for_server()
rospy.loginfo("ACTION server found")

rospy.loginfo("waiting for SERVICE server")
rospy.wait_for_service('/my_service')
rospy.loginfo("SERVICE server found")
service_object = rospy.ServiceProxy('/my_service', DistanceMotionMessage)
rospy.loginfo("Connection established")



def rec_odom_feedback_callback(feedback):
    rospy.loginfo("Feedback ==> " + str(feedback))


record_odom_client.send_goal(RecordPoseGoal,feedback_cb=rec_odom_feedback_callback)
rospy.loginfo("Goal message sent")
request = DistanceMotionMessageRequest()
result = service_object(request)
rospy.loginfo("Service is sent")

while not finished:
    if (record_odom_client.get_state() >= 2):
        result = record_odom_client.get_result()
        finished = True
     #wait for client to finish

rospy.sleep(0.5)
result_array = result.result_odom_array
#get the finall array
last_index_val = result_array[1]
#exlcude covaraince
last_index_split = str(last_index_val.pose).split('covariance')
new_str = str(last_index_split[0])

#delete final space
print(len(new_str))
final_str = new_str[0:(len(new_str)-1)]
print("Last Pose:\n" + final_str)
