#! /usr/bin/env python

import rospy
import tf2_ros # knjiznica za tf
from geometry_msgs.msg import TransformStamped # vrsta sporocila

if __name__ == '__main__':

    rospy.init_node('tf_static_broadcaster') # topic, na katerega bomo poslali

    tf_broad = tf2_ros.StaticTransformBroadcaster() # naredimo Broadcaster objekt

    frame_1 = TransformStamped()
    frame_1.child_frame_id = 'frame_1' # do cesa
    frame_1.header.frame_id = 'world' # iz cesa

    frame_1.transform.rotation.w = 1.0

    frame_1.transform.translation.z = 1.0
    frame_1.transform.translation.y = 0.0
    frame_1.transform.translation.x = 0.0

    rospy.loginfo("Publishing transform from {0} to {1}".format(frame_1.header.frame_id, frame_1.child_frame_id))
    tf_broad.sendTransform([frame_1]) # sendTransform sprejme array koordinatnih sistemov

    rospy.spin()