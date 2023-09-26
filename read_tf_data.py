#! /usr/bin/env python

import rospy
import pickle
import tf2_ros # knjiznica za tf
from geometry_msgs.msg import TransformStamped # vrsta sporocila

if __name__ == '__main__':

    # Init the node
    rospy.init_node('tf_loader')

    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = raw_input('Vpisi ime datoteke: ')

    infile = open(file_name + '.txt','rb')
    stored_poses = pickle.load(infile)
    infile.close()


    #########################
    ##### STUDENT WRITES ####
    #########################

    frame = 'frame_2'

    tf_broad = tf2_ros.StaticTransformBroadcaster() # naredimo Broadcaster objekt

    transformation = stored_poses.values()
    print(stored_poses.values())

    rospy.loginfo("Publishing transform from {0} to {1}".format(transformation[0].header.frame_id, transformation[0].child_frame_id))
    tf_broad.sendTransform(transformation) # sendTransform sprejme array koordinatnih sistemov

    #########################
    rospy.spin()
