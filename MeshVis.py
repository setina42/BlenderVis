import bpy
from bpy import context

def deselect():
    for obj in bpy.data.objects:
        obj.select = False

## Set Basic Scene: Import reference atlas mesh and desired gene expression/connectivity meshed
##, add a basic lamp and camera set to predefined location and rotation

#Import Reference Atlas
bpy.ops.import_scene.obj(filepath="C:/Users/tinas/Desktop/Sync/Rec/abi2dsurqec_40micron_masked_affine.obj")
Atlas = bpy.context.selected_objects[0]

#Import Gene data
bpy.ops.import_scene.obj(filepath="C:/Users/tinas/Desktop/Sync/Rec/warped_withref200.nii.gz_affine.obj")
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
bpy.context.object.rotation_axis_angle[0] = 3.02814
bpy.context.object.rotation_axis_angle[1] = 0.000353694
bpy.context.object.rotation_axis_angle[2] = 0.487187
bpy.context.object.rotation_axis_angle[3] = -0.916546





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

bpy.data.scenes["Scene"].render.filepath = "C:/Users/tinas/Desktop/Sync/Rec/Pic1"
bpy.ops.render.render( write_still=True )

Atlas.select=True
GeneData.select = True
bpy.ops.transform.rotate(value=1.21921, axis=(-0.00457997, 0.716912, -0.697148), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


bpy.data.scenes["Scene"].render.filepath = "C:/Users/tinas/Desktop/Sync/Rec/Pic2"
bpy.ops.render.render( write_still=True )