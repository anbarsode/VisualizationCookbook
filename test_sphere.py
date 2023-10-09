import bpy
import numpy as np
import os, sys
cwd = os.getcwd()
sys.path.append(cwd)
from materials import *
from UI import *

##### Load images and their z locations
px = 64
py = px
pz = 8
r_locs = np.linspace(0, 1, pz)
image_filenames = ['../cube_data/t_10_px_%d_py_%d_pz_64/cube_z_%d.png' % (px, py, i) for i in range(pz)]
images = [bpy.data.images.load(cwd + '/' + image_filename) for image_filename in image_filenames]
loc_tol = np.min(np.diff(r_locs)) * 1e-3

# Create layers
for i in range(len(images)-1):
    create_scalar_Ellipsoid_layer(i, r_locs[i], r_locs[i+1], images[i], images[i+1], cmap_name = 'my_cold', \
                                  obj_scale = [1,1,1], obj_radius = 1, \
                                  obj_loc = [0,0,0], randomize_loc = True, loc_tol = loc_tol)

# Put the layers in a collection
bpy.ops.object.select_all(action = 'DESELECT')
bpy.ops.object.select_pattern(pattern = 'Layer *')
bpy.ops.object.move_to_collection(collection_index = 0, is_new = True, new_collection_name = 'Sphere 1' )
bpy.ops.object.select_all(action = 'DESELECT')

# Set viewport and rendering settings
reset_render_settings(**RENDER_SETTINGS)
reset_viewport_settings(**VIEW_SETTINGS)

def register():
    for cls in blender_classes: bpy.utils.register_class(cls)
    
    bpy.types.Scene.user_inputs = bpy.props.PointerProperty(type = MyProperties)

def unregister():
    del bpy.types.Scene.user_inputs
    
    for cls in blender_classes: bpy.utils.unregister_class(cls)

if __name__ == '__main__':
    register()
