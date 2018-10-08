import bpy
from bpy import context
import os
import sys

##Function to deselect all objects
def deselect():
    for obj in bpy.data.objects:
        obj.select = False

##File path
#path = os.path.abspath('.')
path = "C:/Users/tinas/Desktop/Sync/Rec"



## Set Basic Scene: Import reference atlas mesh and desired gene expression/connectivity meshed
##, add a basic lamp and camera set to predefined location and rotation

#Delete all present objects if any
for obj in bpy.data.objects:
    obj.select = True
    bpy.ops.object.delete()

#Import Reference Atlas
bpy.ops.import_scene.obj(filepath= path +"/abi2dsurqec_40micron_masked_affine.obj")
Atlas = bpy.context.selected_objects[0]

#Import Gene data
bpy.ops.import_scene.obj(filepath=path + "/warped_withref200.nii.gz_affine.obj")
GeneData = bpy.context.selected_objects[0]

#Add a lamp, set location and rotation
bpy.ops.object.lamp_add(type='SUN', radius=1, view_align=False, location=(0, -10, 10), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
Sun = bpy.context.selected_objects[0]

deselect()
Sun.select = True
bpy.context.object.rotation_mode = 'AXIS_ANGLE'
bpy.context.object.rotation_axis_angle[0] = 3.02814
bpy.context.object.rotation_axis_angle[1] = 0.0004
bpy.context.object.rotation_axis_angle[2] = 0.387187
bpy.context.object.rotation_axis_angle[3] = -0.916546


#Try with a hemi lamp
deselect()
bpy.context.object.rotation_axis_angle[2] = 0.387187
bpy.ops.object.lamp_add(type='HEMI', radius=1, view_align=False, location=(-0.00643184, -10.4931, 10.284), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
Hemi = bpy.context.selected_objects[0]

#Add a camera, set location and rotation
bpy.ops.object.camera_add(view_align=True, enter_editmode=False, location=(0, 0, 0), rotation=(1.10871, 0.0132652, 1.14827), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
Camera = bpy.context.selected_objects[0]
Camera.location = (0,-20,20)

deselect()
Camera.select = True

bpy.context.object.rotation_mode = 'AXIS_ANGLE'
bpy.context.object.rotation_axis_angle[0] = 3.12814
bpy.context.object.rotation_axis_angle[1] = 0.000353694
bpy.context.object.rotation_axis_angle[2] = 0.487187
bpy.context.object.rotation_axis_angle[3] = -1.11655



## Add colour and material to the meshes for visualization

deselect()

MatAtlas = bpy.data.materials.new(name="atlas_material")

#bpy.context.space_data.context = 'MATERIAL'
#bpy.ops.material.new()
MatAtlas.diffuse_color = (0.178419, 0.178419, 0.178419)
MatAtlas.use_transparency = True
MatAtlas.alpha = 0.7


MatGenes = bpy.data.materials.new(name="gene_material")

MatGenes.diffuse_color = (0.8, 0.0102894, 0)
MatGenesdiffuse_color = (0.611409, 0.00855554, 0)
MatGenes.diffuse_color = (0.611409, 0.00855554, 0)


#Apply colours
Atlas.data.materials.append(MatAtlas)
GeneData.data.materials.append(MatGenes)




step_count = 32

#Try to rotate camera around the brain and render different angles.

#for step in range(0, step_count):
#    origin.rotation_euler[2] = radians(step * (360.0 / step_count))
#
deselect() 

bpy.data.scenes["Scene"].camera = Camera

bpy.data.scenes["Scene"].render.filepath = path + "/Pic1"
bpy.ops.render.render( write_still=True )

Atlas.select=True
GeneData.select = True
#bpy.ops.transform.rotate(value=1.21921, axis=(-0.00457997, 0.716912, -0.697148), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


## Try moving the camera instead of the brain
def look_at(obj_camera, point):
    loc_camera = Camera.location

    direction = point - loc_camera
    # point the cameras '-Z' and use its 'Y' as up
    rot_quat = direction.to_track_quat('-Z', 'Y')

    # assume we're using euler rotation
    obj_camera.rotation_euler = rot_quat.to_euler()




#Set camera to a specific location, render and save image
def TakePic(FileName,loc):
    Camera.location = loc
    deselect()
    Camera.select= True
    bpy.context.object.rotation_mode = 'XYZ'
    look_at(Camera,Atlas.location)
    bpy.data.scenes["Scene"].render.filepath = path + "/" + FileName
    bpy.ops.render.render( write_still=True )
    
TakePic("Default", Camera.location)  
TakePic("TopView", (0,-30,0))
TakePic("Side", (10,-18,18))
    

