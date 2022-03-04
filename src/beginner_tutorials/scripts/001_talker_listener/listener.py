#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data) -> None:
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener() -> None:
	rospy.init_node("listener", anonymous=True) # So each node is given a unique node
	rospy.Subscriber("chatter", String, callback)

	rospy.spin()

if __name__ == "__main__":
	listener()
