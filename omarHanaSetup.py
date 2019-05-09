import bpy
import os

# change File Output Node Path
fileName = bpy.path.basename(bpy.context.blend_data.filepath)
sceneName = os.path.splitext(fileName)[0]
absolutePath = "//../../../03_render/frames/02_salawat/"

for scene in bpy.data.scenes:
    for node in scene.node_tree.nodes:
        if node.type == 'OUTPUT_FILE':
            print(node.name)
            node.base_path = absolutePath + sceneName + "/" + node.name + "/"

# change Abc Filepath
sceneName = sceneName.replace('rd', 'an')
abcPath = '//abc\\'

abcList = ["hana.abc", "oki.abc", "omar.abc", "ikan_koi_01.abc", "ikan_koi_02.abc", "ikan_koi_03.abc"]

for abc in abcList:
    if bpy.data.cache_files.get(abc) is not None:
        bpy.data.cache_files[abc].filepath = abcPath + sceneName + '_' + abc