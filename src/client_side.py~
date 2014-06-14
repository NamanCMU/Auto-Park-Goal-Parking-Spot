#!/usr/bin/env python
import rospy
import roslib
import tf
from std_msgs.msg import Float32
import subprocess
import os

def callback(data):
    rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)
    if data.data == 1:
        os.system("roslaunch FinalPark.launch &")
    elif data.data == 0:
        rospy.sleep(5.0);
        os.system("rosrun dynamic_reconfigure dynparam set car1/move_base_node base_local_planner base_local_planner/TrajectoryPlannerROS")
        os.system("roslaunch FinalUnpark.launch &")
        
        
def client_side():
    
    pub = rospy.Subscriber('car1/Park', Float32,callback)
    rospy.init_node('client_side_car1')
    rospy.spin()
    
if __name__ == '__main__':
    try:
        client_side()
    except rospy.ROSInterruptException:
        pass


