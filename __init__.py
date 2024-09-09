bl_info = {
    "name" : "Mek Tools",
    "author" : "Meku Maki, ThetaFive, Skulblaka", 
    "description" : "Helps with importing and exporting FBX models and animating in blender!",
    "blender" : (4, 0, 0),
    "version" : (0, 3, 6),
    "category" : "3D View" 
}


import bpy # type: ignore
import os


#from .utils import wol_material_replacement


from .operators.alpha_fix_operator import OT_AlphaFix
from .operators.normals_fix_operator import OT_NormalsFix
from .operators.replace_materials_operator import ReplaceMaterialsOperator


from .panels.importexport_mek import VIEW3D_IMPORT_AND_EXPORT_MEK
from .panels.links_panel import MEK_LinksPanel

classes = [MEK_LinksPanel,
           VIEW3D_IMPORT_AND_EXPORT_MEK,
           OT_AlphaFix,
           OT_NormalsFix,
           ReplaceMaterialsOperator,
           
           ]





def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()