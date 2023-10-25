cmake_minimum_required(VERSION 3.0.2)
project(basics_exam)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  actionlib_msgs
  nav_msgs
)

add_service_files(
  FILES
  DistanceMotionMessage.srv
)

add_action_files(
   FILES
   RecordPose.action
)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
  nav_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy message_runtime nav_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)