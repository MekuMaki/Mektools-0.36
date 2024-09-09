import bpy # type: ignore

class MEK_AlphaFix(bpy.types.Operator):
    bl_label = 'Alpha Fix'
    bl_idname = 'mek_alpha_fix'

    def execute(self, context):
        for item in bpy.data.materials:
            item.blend_method = 'HASHED' # Such a smol function, much wow
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)