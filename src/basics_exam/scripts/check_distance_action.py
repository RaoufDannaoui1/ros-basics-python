#! /usr/bin/env python
import rospy
import time
import actionlib
from OdomTopicSubsciber import OdomTopicReader 
from basics_exam.msg import RecordPoseFeedback, RecordPoseAction, RecordPoseResult
from nav_msgs.msg import Odometry

class DronePositionReader:
    def __init__(self, topic='/ground_truth/state'):
        self.position = None
        self.odom_subscriber = rospy.Subscriber(topic, Odometry, self.odom_callback)

    def odom_callback(self, odom_msg):
        # Extract and store the drone's current position
        self.position = odom_msg.pose.pose.position

    def get_current_position(self):
        return self.position


def goal_callback(goal):
    rate = rospy.Rate(1)
    result = RecordPoseResult()
    sucess = True
    recording_time = 20 # recording time

    # record pos 20 times
    for i in range (20):
        rospy.loginfo("Recording odom index " + str(i))
        current_position = drone_position_reader.get_current_position()
        if current_position:
            print(f" x={current_position.x}, y={current_position.y}, z={current_position.z}")
        else:
            rospy.loginfo("Waiting for position data...")
        rospy.sleep(1.0)
        if record_odom_action_server.is_preempt_requested():
            sucess = False
            record_odom_action_server.set_preempted()
        else:
            # odom_reader_object = OdomTopicReader()
            # result.result_odom_array.append(odom_reader_object.get_odomdata())
            result.result_odom_array.append((current_position.x, current_position.y, current_position.z))
        rate.sleep()
    rospy.loginfo("finished recording 20 data sets")
    if sucess:
        
        record_odom_action_server.set_succeeded(result)
        result.result_odom_array
        print("\n\n\n\n\n")
        print(result.result_odom_array)
        rospy.loginfo("result data is sent")
    
    

rospy.init_node("check_distance_action_node")
record_odom_action_server = actionlib.SimpleActionServer('/rec_pose_as',RecordPoseAction,goal_callback,False)
record_odom_action_server.start()
rospy.loginfo("Action server started")
drone_position_reader = DronePositionReader()


