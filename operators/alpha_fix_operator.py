import bpy # type: ignore

class OT_AlphaFix(bpy.types.Operator):
    bl_label = 'alpha_fix'
    bl_idname = 'OT_AlphaFix'

    def execute(self, context):
        for item in bpy.data.materials:
            item.blend_method = 'HASHED' # Such a smol function, much wow
        return {'FINISHED'}