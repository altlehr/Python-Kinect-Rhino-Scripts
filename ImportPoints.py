# Import points from a text file
import rhinoscriptsyntax as rs
from openni import *
import numpy as np
import cv2
 
# Initialise OpenNI
context = Context()
context.init()
 
# Create a depth generator to access the depth stream
depth = DepthGenerator()
depth.create(context)
depth.set_resolution_preset(RES_VGA)
depth.fps = 30
 
# Start Kinect
context.start_generating_all()
context.wait_any_update_all()
 
# Create array from the raw depth map string
frame = np.fromstring(depth.get_raw_depth_map_8(), "uint8").reshape(480, 640)

#rs.AddPoints("image", frame)

def ImportPoints():
    

    # local helper function    
    def __point_from_string(frame):
        items = frame.strip("()\n").split(",")
        x = float(items[0])
        y = float(items[1])
        z = float(items[2])
        return x, y, z

    contents = [__point_from_string(line) for line in contents]
    rs.AddPoints(contents)



##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    ImportPoints()