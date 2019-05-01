import bpy
import os

filePath = bpy.path.basename(bpy.context.blend_data.filepath)
sceneName = os.path.splitext(filePath)[0]


# Export Abc for Hana
bpy.ops.object.select_all(action='DESELECT')
if bpy.data.objects.get("hana") is not None:

    hanaOb = bpy.data.objects["hana"]
    hanaOb.hide_select = False
    hanaOb.hide_render = False
    hanaOb.hide_viewport = False
    hanaOb.select_set(state=True)
    bpy.context.view_layer.objects.active = hanaOb

    bpy.ops.wm.alembic_export(filepath="F:/Projects/Pawitra/Dropbox/OH_2019/batch01/01_pro/03_eps/02_salawat/abc/%s_hana.abc" % sceneName, check_existing=True, selected=True, renderable_only=False, visible_layers_only=False, flatten=True, uvs=True, packuv=False, normals=True,export_hair=False, export_particles=False, init_scene_frame_range=True)


# Export Abc for Oki
bpy.ops.object.select_all(action='DESELECT')
if bpy.data.objects.get("oki") is not None:

    okiOb = bpy.data.objects["oki"]
    okiOb.hide_select = False
    okiOb.hide_render = False
    okiOb.hide_viewport = False
    okiOb.select_set(state=True)
    bpy.context.view_layer.objects.active = okiOb

    bpy.ops.wm.alembic_export(filepath="F:/Projects/Pawitra/Dropbox/OH_2019/batch01/01_pro/03_eps/02_salawat/abc/%s_oki.abc" % sceneName, check_existing=True, selected=True, renderable_only=False, visible_layers_only=False, flatten=True, uvs=True, packuv=False, normals=True,export_hair=False, export_particles=False, init_scene_frame_range=True)


# Export Abc for Omar
bpy.ops.object.select_all(action='DESELECT')
if bpy.data.objects.get("omar") is not None:

    omarOb = bpy.data.objects["omar"]
    omarOb.hide_select = False
    omarOb.hide_render = False
    omarOb.hide_viewport = False
    omarOb.select_set(state=True)
    bpy.context.view_layer.objects.active = omarOb

    bpy.ops.wm.alembic_export(filepath="F:/Projects/Pawitra/Dropbox/OH_2019/batch01/01_pro/03_eps/02_salawat/abc/%s_omar.abc" % sceneName, check_existing=True, selected=True, renderable_only=False, visible_layers_only=False, flatten=True, uvs=True, packuv=False, normals=True,export_hair=False, export_particles=False, init_scene_frame_range=True)
