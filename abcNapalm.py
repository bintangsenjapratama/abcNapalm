import bpy
import os

baseFilePath = bpy.path.basename(bpy.context.blend_data.filepath)
sceneName = os.path.splitext(baseFilePath)[0]

fullFilePath = bpy.data.filepath
epsFolder = os.path.split(fullFilePath)[0]
epsFolder = epsFolder.replace('\\','/')
abcFolder = epsFolder + "/abc"
try:
    os.mkdir(abcFolder)
except:
    pass

# Need to make some interface and ability to enable all Collections viewport and render visibility in the scene

# Export Abc for Each Characters
charList = ["hana", "oki", "omar", "ikan_koi_01", "ikan_koi_02", "ikan_koi_03"]
bpy.ops.object.mode_set(mode='OBJECT')

for char in charList:
    if bpy.data.objects.get(char) is not None:

        bpy.ops.object.select_all(action='DESELECT')
        charOb = bpy.data.objects[char]
        charOb.hide_select = False
        charOb.hide_render = False
        charOb.hide_viewport = False
        charOb.select_set(state=True)
        bpy.context.view_layer.objects.active = charOb
        
        
        bpy.ops.wm.alembic_export(filepath="%s/%s_%s.abc" % (abcFolder, sceneName, char), check_existing=True, selected=True, renderable_only=True, visible_layers_only=False, flatten=True, uvs=True, packuv=False, normals=True,export_hair=False, export_particles=False, init_scene_frame_range=True)