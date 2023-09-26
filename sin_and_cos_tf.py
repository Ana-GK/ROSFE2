#! /usr/bin/env python

import rospy
import tf2_ros # knjiznica za tf
from geometry_msgs.msg import TransformStamped # vrsta sporocila
# import numpy as np
import math

if __name__ == '__main__':


    rospy.init_node('tf_static_broadcaster') # topic, na katerega bomo poslali

    t = rospy.get_time()

    tf_broad = tf2_ros.TransformBroadcaster() # ni vec staticTransformbroadcaster!

    frame_1 = TransformStamped()
    frame_1.child_frame_id = 'frame_1' # do cesa
    frame_1.header.frame_id = 'world' # iz cesa

    frame_1.transform.rotation.w = 1.0

    frame_1.transform.translation.z = 1.0
    frame_1.transform.translation.y = 0.0
    frame_1.transform.translation.x = 0.0


    frame_2 = TransformStamped()
    frame_2.child_frame_id = 'frame_2'
    frame_2.header.frame_id = 'frame_1'

    frame_2.transform.rotation.w = 1.0


    frame_2.transform.translation.y = 0.0
    frame_2.transform.translation.z = math.cos(t)
    frame_2.transform.translation.x = math.sin(t)

    world = TransformStamped()

    rospy.loginfo("Publishing transform from {0} to {1}".format(frame_1.header.frame_id, frame_1.child_frame_id))
    while not rospy.is_shutdown(): # dokler je node aktiven - dokler ne kliknemo ^C
        t = rospy.get_time()
        frame_2.transform.translation.z = math.cos(t)
        frame_2.transform.translation.x = math.sin(t)
        tf_broad.sendTransform([frame_1,frame_2]) # sendTransform sprejme array koordinatnih sistemov
        rospy.sleep(0.1)
    

    rospy.spin()