import bpy # type: ignore

class MEK_NormalsFix(bpy.types.Operator):
    bl_label = "Normals Fix"
    bl_idname = "MEK_NormalsFix"
    bl_description = "Clear Custom Split Normals if the model looks kinda jank for some reasons."
    
    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        joined_objects = bpy.context.selected_objects
    
        for object in selected_objects:
            if object.type == 'MESH':
                bpy.ops.mesh.customdata_custom_splitnormals_clear()

        return {'FINISHED'}