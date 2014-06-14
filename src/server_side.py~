#!/usr/bin/env python
import rospy
import roslib
import tf
import sys
from std_msgs.msg import Float32



def server_side():
    #carname = sys.argv[1]
    
    
    publisher_topic = 'car1/Park'
    publisher_topic2 = 'car2/Park'
    publisher_topic3 = 'car3/Park'
    pub = rospy.Publisher(publisher_topic, Float32)
    pub2 = rospy.Publisher(publisher_topic2, Float32)
    pub3 = rospy.Publisher(publisher_topic3, Float32)
    rospy.init_node('server_side')
    

    current_time = rospy.get_rostime();
    
    while not rospy.is_shutdown():
	car = input('Enter the car name: ')
        command = input('To Park press 1, to Unpark press 0: ')
        rospy.loginfo(command)
	if car == 'car1':
            pub.publish(command) 
        if car == 'car2':
	    pub2.publish(command)   
        if car == 'car3':
	    pub3.publish(command)      
       # rospy.sleep(5.0);

if __name__ == '__main__':
    try:
        server_side()
    except rospy.ROSInterruptException:
        pass

