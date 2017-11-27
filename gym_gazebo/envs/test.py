#!/usr/bin/env python
import roslib; roslib.load_manifest('gazebo_ros')
import sys
from gazebo_msgs.msg import ModelState
import rospy

def setmodelstate(modelname,x,y,yaw):
	pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=10)
	# rospy.init_node('ali')	
	state=ModelState()
	state.model_name = modelname
	state.pose.position.x=x
	state.pose.position.y=y
	state.pose.orientation.z=yaw
	pub.publish(state)
	