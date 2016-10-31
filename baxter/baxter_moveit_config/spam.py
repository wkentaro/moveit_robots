#!/usr/bin/env python

import rospy
import moveit_commander

from geometry_msgs.msg import PoseStamped


rospy.init_node('spam')

scene = moveit_commander.PlanningSceneInterface()
robot = moveit_commander.RobotCommander()

rospy.sleep(2)
scene.remove_world_object()

# shelf
p = PoseStamped()
p.header.frame_id = robot.get_planning_frame()
p.pose.position.x = 1.6
p.pose.position.y = 0
p.pose.position.z = 0
scene.add_box('shelf', p, (1.0, 1.0, 2.0))

rospy.sleep(1)

# tote
p = PoseStamped()
p.header.frame_id = robot.get_planning_frame()
p.pose.position.x = 0.8
p.pose.position.y = 0
p.pose.position.z = -0.4
scene.add_box('tote', p, (0.4, 0.8, 0.3))
