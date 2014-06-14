#!/usr/bin/env python
import rospy
import roslib
import tf
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
from std_msgs.msg import Float32
import os

goal_x = -1000.0
goal_y = -1000.0
goal_angular_z = -1000.0
goal_angular_w = -10000.0
check = 0
final_goal_spot = PoseStamped();

def callback1(data):
    tolerance = 1.5
    linear_x = data.pose.pose.position.x
    linear_y = data.pose.pose.position.y
    angular_z = data.pose.pose.orientation.z
    angular_w = data.pose.pose.orientation.w
    #rospy.loginfo(rospy.get_name() + ": Linear X %s" % linear_x)
    #rospy.loginfo(rospy.get_name() + ": Linear Y %s" % linear_y)
    #rospy.loginfo(rospy.get_name() + ": Angular Z %s" % angular_z)
    #rospy.loginfo(rospy.get_name() + ": Angular W %s" % angular_w)
    global check
    global final_goal_spot
    print "Linear X: ", linear_x, " Linear Y: ", linear_y, " Goal X: ", goal_x, " Goal Y: ", goal_y
    if check == 0 and abs(linear_x - goal_x) <= tolerance and abs(linear_y - goal_y) <= tolerance and abs(angular_z - goal_angular_z) <= tolerance and abs(angular_w - goal_angular_w) <= tolerance:
        check  = 1;
	print "check check check"
        os.system("rosrun dynamic_reconfigure dynparam set car1/move_base_node base_local_planner pose_follower/PoseFollower")
        #pub3 = rospy.Publisher('move_base_simple/goal', PoseStamped)
        #print final_goal_spot
        #while not rospy.is_shutdown():
        #    pub3.publish(final_goal_spot)
        #    rospy.sleep(10000.0);
        # Change the planner


def callback2(data):
    global goal_x
    global goal_y
    global goal_angular_z
    global goal_angular_w
    global final_goal_spot
    final_goal_spot = data
    
    goal_x = data.pose.position.x
    goal_y = data.pose.position.y
    goal_angular_z = data.pose.orientation.z
    goal_angular_w = data.pose.orientation.w
    
    rospy.loginfo(rospy.get_name() + " Goal X:: %s" % goal_x)
    rospy.loginfo(rospy.get_name() + " Goal Y:: %s" % goal_y)
    rospy.loginfo(rospy.get_name() + " Goal Angular Z:: %s" % goal_angular_z)
    rospy.loginfo(rospy.get_name() + " Goal Angular W:: %s" % goal_angular_w)


def path_changer2():
    pub1 = rospy.Subscriber('car1/amcl_pose', PoseWithCovarianceStamped,callback1)
    pub2 = rospy.Subscriber('car1/move_base_simple/goal', PoseStamped,callback2)
    
    rospy.init_node('path_changer2')
    
    rospy.spin()   
    
if __name__ == '__main__':
    try:
        path_changer2()
    except rospy.ROSInterruptException:
        pass

