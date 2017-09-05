#!/usr/bin/env python
#Start of the poly_chatter node

import rospy
from random import randint
from std_msgs.msg import String

def poly_talker():
	pub = rospy.Publisher('polycrier', String, queue_size=10)
	rospy.init_node('Crier', anonymous=True)
	rate = rospy.Rate(21) #21hz
	while not rospy.is_shutdown():
		num = random.randint(1,3)
		name["Dean","Jon","Vamsi"]
		output = name[num]
		rospy.loginfo(output)
		pub.publish(output)
		rate.sleep()

if __name__ == '__main__':
	try:
		poly_talker()
	except rospy.ROSInterruptException:
		pass

