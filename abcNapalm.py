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
# This script still need to select at least one object in the scene to run, didn't work when using bpy.ops.object.select_all(action='SELECT') before exporting Abc lines.

# Export Abc for Hana
bpy.ops.object.select_all(action='DESELECT')
if bpy.data.objects.get("hana") is not None:

    hanaOb = bpy.data.objects["hana"]
    hanaOb.hide_select = False
    hanaOb.hide_render = False
    hanaOb.hide_viewport = False
    hanaOb.select_set(state=True)
    bpy.context.view_layer.objects.active = hanaOb

    bpy.ops.wm.alembic_export(filepath="%s/%s_hana.abc" % (abcFolder, sceneName), check_existing=True, selected=True, renderable_only=False, visible_layers_only=False, flatten=True, uvs=True, packuv=False, normals=True,export_hair=False, export_particles=False, init_scene_frame_range=True)


# Export Abc for Oki
bpy.ops.object.select_all(action='DESELECT')
if bpy.data.objects.get("oki") is not None:

    okiOb = bpy.data.objects["oki"]
    okiOb.hide_select = False
    okiOb.hide_render = False
    okiOb.hide_viewport = False
    okiOb.select_set(state=True)
    bpy.context.view_layer.objects.active = okiOb

    bpy.ops.wm.alembic_export(filepath="%s/%s_oki.abc" % (abcFolder, sceneName), check_existing=True, selected=True, renderable_only=False, visible_layers_only=False, flatten=True, uvs=True, packuv=False, normals=True,export_hair=False, export_particles=False, init_scene_frame_range=True)


# Export Abc for Omar
bpy.ops.object.select_all(action='DESELECT')
if bpy.data.objects.get("omar") is not None:

    omarOb = bpy.data.objects["omar"]
    omarOb.hide_select = False
    omarOb.hide_render = False
    omarOb.hide_viewport = False
    omarOb.select_set(state=True)
    bpy.context.view_layer.objects.active = omarOb

    bpy.ops.wm.alembic_export(filepath="%s/%s_omar.abc" % (abcFolder, sceneName), check_existing=True, selected=True, renderable_only=False, visible_layers_only=False, flatten=True, uvs=True, packuv=False, normals=True,export_hair=False, export_particles=False, init_scene_frame_range=True)
