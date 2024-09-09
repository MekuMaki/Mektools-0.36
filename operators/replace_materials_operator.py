import bpy # type: ignore


# Dictionary of keywords and corresponding material names
material_replacement_map = {
    "fac": "Face Dawntrail",
    "iri": "Eyes Dawntrail",
    "etc_a": "etc_a Dawntrail",
    "etc_b": "etc_b Dawntrail",
    "etc_c": "etc_c Dawntrail",
    "hir": "Hair Dawntrail"
}

def replace_material_with_external(context):
    # Get the path of the current addon
    addon_directory = os.path.dirname(os.path.abspath(__file__))

    # Path to the shaders.blend file inside the 'assets' folder of the addon
    blend_filepath = os.path.join(addon_directory, "assets", "shaders.blend")
    
    # Loop through selected objects
    for obj in bpy.context.selected_objects:
        # Check if the object has material slots
        if obj.type == 'MESH' and obj.material_slots:
            for mat_slot in obj.material_slots:
                # Get the current material name
                current_material = mat_slot.material
                if current_material:
                    # Loop through the keywords in the dictionary
                    for keyword, replacement_material_name in material_replacement_map.items():
                        # Check if the material name contains the keyword
                        if keyword in current_material.name:
                            # Link material from the external file
                            with bpy.data.libraries.load(blend_filepath, link=False) as (data_from, data_to):
                                if replacement_material_name in data_from.materials:
                                    data_to.materials = [replacement_material_name]
                            
                            # Assign the appended material
                            new_material = data_to.materials[0]
                            mat_slot.material = new_material
                            break  # Once matched, no need to check other keywords

class ReplaceMaterialsOperator(bpy.types.Operator):
    """Replace materials by name part"""
    bl_idname = "object.replace_materials"
    bl_label = "Replace Materials"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        replace_material_with_external(context)
        return {'FINISHED'}