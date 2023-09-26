#! /usr/bin/env python

import rospy
import pickle
import os
import tf2_ros

if __name__ == '__main__':

    rospy.init_node('tf_saver')
    rospy.loginfo("TF saver started!")

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rospy.sleep(1)
    stored_data = {}

    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = raw_input('Vpisi ime datoteke: ')
    outfile = open(file_name + '.txt','wb')
    saved_data = {}
    #########################
    ##### STUDENT WRITES ####

    #########################

    frame = 'frame_2'

    transformation = tf_buffer.lookup_transform(frame,'world',rospy.Time(0))
    print(transformation)

    saved_data[frame] = transformation
    
    # saved_data['frame_2'] = transformation.transform.translation.x
    # Hint - Use the tf_buffer.lookup_transform() method to retrieve the transform.
    # Example:
    # transformation = tf_buffer.lookup_transform(from_frame, to_frame, rospy.Time(0))
    # Note - from_frame and to_frame need to be defined!


    #########################

    pickle.dump(saved_data, outfile)
    outfile.close()