# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Mek Tools",
    "author" : "Meku Maki, ThetaFive, Skulblaka", 
    "description" : "Helps with importing and exporting FBX models and animating in blender!",
    "blender" : (4, 0, 0),
    "version" : (0, 3, 6),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "3D View" 
}


import bpy
import bpy.utils.previews
import os
import json
from os import path
from math import radians
from mathutils import *
from bpy_extras.io_utils import ExportHelper


addon_keymaps = {}
_icons = None
class SNA_PT_IMPORT_AND_EXPORT_D25AF(bpy.types.Panel):
    bl_label = 'Import and Export'
    bl_idname = 'SNA_PT_IMPORT_AND_EXPORT_D25AF'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Mektools 0.36'
    bl_order = 1
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_1056A = layout.box()
        box_1056A.alert = False
        box_1056A.enabled = True
        box_1056A.active = True
        box_1056A.use_property_split = False
        box_1056A.use_property_decorate = False
        box_1056A.alignment = 'Expand'.upper()
        box_1056A.scale_x = 1.0
        box_1056A.scale_y = 1.0
        if not True: box_1056A.operator_context = "EXEC_DEFAULT"
        split_57605 = box_1056A.split(factor=0.5, align=False)
        split_57605.alert = False
        split_57605.enabled = True
        split_57605.active = True
        split_57605.use_property_split = False
        split_57605.use_property_decorate = False
        split_57605.scale_x = 1.0
        split_57605.scale_y = 1.0
        split_57605.alignment = 'Expand'.upper()
        if not True: split_57605.operator_context = "EXEC_DEFAULT"
        op = split_57605.operator('import_scene.fbx', text='Import FBX', icon_value=706, emboss=True, depress=False)
        op.force_connect_children = True
        op.automatic_bone_orientation = True
        op = split_57605.operator('export_scene.fbx', text='Export FBX', icon_value=707, emboss=True, depress=False)
        box_FEE47 = layout.box()
        box_FEE47.alert = False
        box_FEE47.enabled = True
        box_FEE47.active = True
        box_FEE47.use_property_split = False
        box_FEE47.use_property_decorate = False
        box_FEE47.alignment = 'Expand'.upper()
        box_FEE47.scale_x = 1.0
        box_FEE47.scale_y = 1.0
        if not True: box_FEE47.operator_context = "EXEC_DEFAULT"
        split_7EDD2 = box_FEE47.split(factor=0.5, align=False)
        split_7EDD2.alert = False
        split_7EDD2.enabled = True
        split_7EDD2.active = True
        split_7EDD2.use_property_split = False
        split_7EDD2.use_property_decorate = False
        split_7EDD2.scale_x = 1.0
        split_7EDD2.scale_y = 1.0
        split_7EDD2.alignment = 'Expand'.upper()
        if not True: split_7EDD2.operator_context = "EXEC_DEFAULT"
        op = split_7EDD2.operator('object.parent_clear', text='Clear Parents', icon_value=0, emboss=True, depress=False)
        op.type = 'CLEAR_KEEP_TRANSFORM'
        op = split_7EDD2.operator('sna.alphafix_4f08e', text='Fix Alpha', icon_value=0, emboss=True, depress=False)
        split_55F05 = box_FEE47.split(factor=0.5, align=False)
        split_55F05.alert = False
        split_55F05.enabled = True
        split_55F05.active = True
        split_55F05.use_property_split = False
        split_55F05.use_property_decorate = False
        split_55F05.scale_x = 1.0
        split_55F05.scale_y = 1.0
        split_55F05.alignment = 'Expand'.upper()
        if not True: split_55F05.operator_context = "EXEC_DEFAULT"
        op = split_55F05.operator('myops.fixmetallic', text='Fix Metallic', icon_value=0, emboss=True, depress=False)
        op = split_55F05.operator('myops.clear_split_normals', text='Fix Split Normal Data', icon_value=0, emboss=True, depress=False)
        box_00E0C = layout.box()
        box_00E0C.alert = False
        box_00E0C.enabled = True
        box_00E0C.active = True
        box_00E0C.use_property_split = False
        box_00E0C.use_property_decorate = False
        box_00E0C.alignment = 'Expand'.upper()
        box_00E0C.scale_x = 1.0
        box_00E0C.scale_y = 1.0
        if not True: box_00E0C.operator_context = "EXEC_DEFAULT"
        op = box_00E0C.operator('myops.matfix', text='Apply Custom Skin Shader', icon_value=0, emboss=True, depress=False)
        op = box_00E0C.operator('myops.eyefix', text='Fix Eyes', icon_value=0, emboss=True, depress=False)


class SNA_PT_FOR_RENDERING_12387(bpy.types.Panel):
    bl_label = 'For Rendering'
    bl_idname = 'SNA_PT_FOR_RENDERING_12387'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Mektools 0.36'
    bl_order = 2
    bl_options = {'HEADER_LAYOUT_EXPAND', 'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout.label(text="Don't use below if making a mod!", icon_value=2)
        layout.label(text='Use if you want to Animate!', icon_value=168)
        box_3B691 = layout.box()
        box_3B691.alert = False
        box_3B691.enabled = True
        box_3B691.active = True
        box_3B691.use_property_split = False
        box_3B691.use_property_decorate = False
        box_3B691.alignment = 'Expand'.upper()
        box_3B691.scale_x = 3.0
        box_3B691.scale_y = 3.0
        if not True: box_3B691.operator_context = "EXEC_DEFAULT"
        op = box_3B691.operator('myops.remove_un_needed_bones', text='Remove Bones', icon_value=200, emboss=True, depress=False)
        split_45C4A = box_3B691.split(factor=0.5, align=False)
        split_45C4A.alert = False
        split_45C4A.enabled = True
        split_45C4A.active = True
        split_45C4A.use_property_split = False
        split_45C4A.use_property_decorate = False
        split_45C4A.scale_x = 1.0
        split_45C4A.scale_y = 1.0
        split_45C4A.alignment = 'Expand'.upper()
        if not True: split_45C4A.operator_context = "EXEC_DEFAULT"
        split_45C4A.popover('SNA_PT_MALE_RIGS_0127C', text='Male Rigs', icon_value=0)
        split_45C4A.popover('SNA_PT_FEMALE_RIGS_43F95', text='Female Rigs', icon_value=0)


class SNA_OT_Import_Am_C728C(bpy.types.Operator):
    bl_idname = "sna.import_am_c728c"
    bl_label = "Import_AM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Aura Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_FC980 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Af_B4751(bpy.types.Operator):
    bl_idname = "sna.import_af_b4751"
    bl_label = "Import_AF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Aura Female', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_F4C30 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Ef_8E849(bpy.types.Operator):
    bl_idname = "sna.import_ef_8e849"
    bl_label = "Import_EF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Elezen Female', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_3B2C6 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Em_B2121(bpy.types.Operator):
    bl_idname = "sna.import_em_b2121"
    bl_label = "Import_EM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Elezen Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_6AEEF = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Hf_E2D09(bpy.types.Operator):
    bl_idname = "sna.import_hf_e2d09"
    bl_label = "Import_HF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Highlander Female', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_1EBCC = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Hrm_C1590(bpy.types.Operator):
    bl_idname = "sna.import_hrm_c1590"
    bl_label = "Import_HrM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Hrothgar Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_A726E = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Lala_Adb84(bpy.types.Operator):
    bl_idname = "sna.import_lala_adb84"
    bl_label = "Import_Lala"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Lalafell Rig', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_A652A = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Mf_36952(bpy.types.Operator):
    bl_idname = "sna.import_mf_36952"
    bl_label = "Import_MF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Midlander Female', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_6B38E = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Mm_02Dc3(bpy.types.Operator):
    bl_idname = "sna.import_mm_02dc3"
    bl_label = "Import_MM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Midlander Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_4E078 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Miqf_E13B1(bpy.types.Operator):
    bl_idname = "sna.import_miqf_e13b1"
    bl_label = "Import_MiqF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Miqote Female', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_26D72 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Miqm_0929D(bpy.types.Operator):
    bl_idname = "sna.import_miqm_0929d"
    bl_label = "Import_MiqM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Miqote Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_28999 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Rf_C1Dc0(bpy.types.Operator):
    bl_idname = "sna.import_rf_c1dc0"
    bl_label = "Import_RF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Roe Female', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_2392A = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Rm_39A5F(bpy.types.Operator):
    bl_idname = "sna.import_rm_39a5f"
    bl_label = "Import_RM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Roe Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_815B4 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Vm_4Aaf7(bpy.types.Operator):
    bl_idname = "sna.import_vm_4aaf7"
    bl_label = "Import_VM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Viera Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_08521 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Vf_6301C(bpy.types.Operator):
    bl_idname = "sna.import_vf_6301c"
    bl_label = "Import_VF"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Viera Female', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_6A4B6 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_FEMALE_RIGS_43F95(bpy.types.Panel):
    bl_label = 'Female Rigs'
    bl_idname = 'SNA_PT_FEMALE_RIGS_43F95'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = ''
    bl_order = 0
    bl_options = {'HIDE_HEADER', 'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_4B3A4 = layout.box()
        box_4B3A4.alert = False
        box_4B3A4.enabled = True
        box_4B3A4.active = True
        box_4B3A4.use_property_split = False
        box_4B3A4.use_property_decorate = False
        box_4B3A4.alignment = 'Expand'.upper()
        box_4B3A4.scale_x = 1.0
        box_4B3A4.scale_y = 1.0
        if not True: box_4B3A4.operator_context = "EXEC_DEFAULT"
        op = box_4B3A4.operator('sna.import_mf_36952', text='Hyur Midlander', icon_value=241, emboss=True, depress=False)
        op = box_4B3A4.operator('sna.import_hf_e2d09', text='Hyur Highlander', icon_value=241, emboss=True, depress=False)
        op = box_4B3A4.operator('sna.import_ef_8e849', text='Elezen', icon_value=241, emboss=True, depress=False)
        op = box_4B3A4.operator('sna.import_miqf_e13b1', text='Miqote', icon_value=241, emboss=True, depress=False)
        op = box_4B3A4.operator('sna.import_rf_c1dc0', text='Roegadyn', icon_value=241, emboss=True, depress=False)
        op = box_4B3A4.operator('sna.import_lala_adb84', text='Lalafell', icon_value=241, emboss=True, depress=False)
        op = box_4B3A4.operator('sna.import_af_b4751', text='Aura', icon_value=241, emboss=True, depress=False)
        op = box_4B3A4.operator('sna.import_vf_6301c', text='Viera', icon_value=241, emboss=True, depress=False)


class SNA_PT_MALE_RIGS_0127C(bpy.types.Panel):
    bl_label = 'Male Rigs'
    bl_idname = 'SNA_PT_MALE_RIGS_0127C'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = ''
    bl_order = 0
    bl_options = {'HIDE_HEADER', 'DEFAULT_CLOSED'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_B4788 = layout.box()
        box_B4788.alert = False
        box_B4788.enabled = True
        box_B4788.active = True
        box_B4788.use_property_split = False
        box_B4788.use_property_decorate = False
        box_B4788.alignment = 'Expand'.upper()
        box_B4788.scale_x = 1.0
        box_B4788.scale_y = 1.0
        if not True: box_B4788.operator_context = "EXEC_DEFAULT"
        op = box_B4788.operator('sna.import_mm_02dc3', text='Hyur Midlander', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_hm_52444', text='Hyur Highlander', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_em_b2121', text='Elezen', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_miqm_0929d', text='Miqote', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_rm_39a5f', text='Roegadyn', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_lala_adb84', text='Lalafell', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_am_c728c', text='Aura', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_hrm_c1590', text='Hrothgar', icon_value=172, emboss=True, depress=False)
        op = box_B4788.operator('sna.import_vm_4aaf7', text='Viera', icon_value=172, emboss=True, depress=False)


class SNA_OT_Alphafix_4F08E(bpy.types.Operator):
    bl_idname = "sna.alphafix_4f08e"
    bl_label = "AlphaFix"
    bl_description = "Changes the viewport settings for its alpha blend mode"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        for item in bpy.data.materials:
            item.blend_method = 'HASHED' # Such a smol function, much wow
        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Import_Hm_52444(bpy.types.Operator):
    bl_idname = "sna.import_hm_52444"
    bl_label = "Import_HM"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and False:
            cls.poll_message_set()
        return not False

    def execute(self, context):
        before_data = list(bpy.data.collections)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__file__), 'assets', 'Rig Collections 4.0.blend') + r'\Collection', filename='Highlander Male', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.collections)))
        appended_69A63 = None if not new_data else new_data[0]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class SNA_PT_MEKTOOLS_036_003A7(bpy.types.Panel):
    bl_label = 'Mektools 0.36'
    bl_idname = 'SNA_PT_MEKTOOLS_036_003A7'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Mektools 0.36'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        exec('op =' + 'layout.' + 'operator(' + "'wm.url_open'," + "text='Support me on Patreon!'," + 'icon_value=227,' + 'emboss=True,' + 'depress=False,)' + ".url = '" + 'https://www.patreon.com/MekuuMaki' + "'")
        exec('op =' + 'layout.' + 'operator(' + "'wm.url_open'," + "text='Join the Discord! (18+ only)'," + 'icon_value=227,' + 'emboss=True,' + 'depress=False,)' + ".url = '" + 'https://www.discord.gg/98DqcKE' + "'")

class RemoveBones(bpy.types.Operator):
    bl_idname = "myops.remove_un_needed_bones"
    bl_label = "Clear them basic bones"
    bl_description = "Removes bones that are already included in Meku Rig V7. DO NOT REMOVE BONES IF YOU INTEND TO USE THIS FOR MODDING"
    
    def execute(self, context):
        
        # This is a list of bone names that get removed when remove bones button is clicked #
        bones_to_remove = ["j_kao", "n_throw", "n_hijisoubi_l", "n_hijisoubi_r", "n_buki_tate_r", "n_buki_tate_l", "n_buki_l", "n_buki_r", "n_kataarmor_l", "n_kataarmor_r", "j_buki_sebo_l", "j_buki_sebo_r", "j_buki_kosi_l", "j_buki_kosi_r", "j_buki2_kosi_l", "j_buki2_kosi_r", "n_hizasoubi_l", "n_hizasoubi_r", "j_kubi", "j_kosi", "n_root", "j_asi_a_l", "j_asi_a_r", "j_asi_b_l", "j_asi_b_r", "j_asi_c_l", "j_asi_c_r", "j_asi_d_l", "j_asi_d_r", "j_asi_e_l", "j_asi_e_r", "n_hara", "j_sebo_a", "j_sebo_b", "j_sebo_c", "j_sako_l", "j_sako_r", "j_ude_a_l", "j_ude_a_r", "n_hkata_l", "n_hkata_r", "j_ude_b_l", "j_ude_b_r", "n_hhiji_l", "n_hhiji_r", "n_hte_l", "n_hte_r", "j_te_l", "j_te_r", "j_oya_a_l", "j_oya_a_r", "j_oya_b_l", "j_oya_b_r", "j_hito_a_l", "j_hito_a_r", "j_hito_b_l", "j_hito_b_r", "j_naka_a_l", "j_naka_a_r", "j_naka_b_l", "j_naka_b_r", "j_kusu_a_l", "j_kusu_a_r", "j_kusu_b_l", "j_kusu_b_r", "j_ko_a_l", "j_ko_a_r", "j_ko_b_l", "j_ko_b_r", "j_mune_l", "j_mune_r", "j_f_ulip_b", "j_f_dlip_b", "j_f_ulip_a", "j_f_dlip_a", "j_ago", "j_f_eye_l", "j_f_eye_r", "j_f_dmab_l", "j_f_dmab_r", "j_f_umab_l", "j_f_umab_r", "j_f_miken_l", "j_f_miken_r", "j_f_mayu_l", "j_f_mayu_r", "j_f_memoto", "j_f_hana", "j_f_hoho_l", "j_f_hoho_r", "j_f_lip_l", "j_f_lip_r", "j_sk_f_a_l", "j_sk_f_b_l", "j_sk_f_c_l", "j_sk_f_a_r", "j_sk_f_b_r", "j_sk_f_c_r", "j_sk_s_a_l", "j_sk_s_b_l", "j_sk_s_c_l", "j_sk_s_a_r", "j_sk_s_b_r", "j_sk_s_c_r", "j_sk_b_a_l", "j_sk_b_b_l", "j_sk_b_c_l", "j_sk_b_a_r", "j_sk_b_b_r", "j_sk_b_c_r", "n_sippo_a", "n_sippo_b", "n_sippo_c", "n_sippo_d", "n_sippo_e", "n_ear_a_r", "n_ear_b_r", "n_ear_a_l", "n_ear_b_l"]

        selected_objects = bpy.context.selected_objects
        
        for object in selected_objects:
            if object.type == 'ARMATURE':
                
                object.select_set(True)  # Select the armature object
                
                bpy.context.view_layer.objects.active = object  # Set the armature object to active
                
                bpy.ops.object.mode_set(mode='EDIT') # Set mode to Edit because it's impossible to access bones otherwise
                for bone in object.data.edit_bones:
                    
                    if bone.name in bones_to_remove:
                        
                        object.data.edit_bones.remove(bone)
                
                bpy.ops.object.mode_set(mode='OBJECT')
                
                object.select_set(False)
                        
        return {'FINISHED'}

class MaterialFix(bpy.types.Operator): # Adds Custom Shader to active material
    bl_idname = "myops.matfix"
    bl_label = "Apply Custom Material Nodes"
    bl_description = "Applies Custom Material Node to objects for fixing shading issues present in FFXIV Furniture and Landscape objects"

    def execute(self, context):
        check_for_nodes()
        selected_material = bpy.context.active_object.active_material
        selected_objects = bpy.context.active_object
        change_material(selected_material)
        return {"FINISHED"}    

# --- functions for doing the things

# For nudging nodes easily

def move_node(node, x_amount, y_amount):
    node.location.x += x_amount
    node.location.y += y_amount

# For placing nodes in absolute space
def place_node(node, x_pos, y_pos):
    node.location.x = x_pos
    node.location.y = y_pos

def check_for_nodes(): #TODO: Check for all nodes? Right now this just checks for the diff-spec converter
    nodesappended = False
    for n in bpy.data.node_groups:
        if n.name == 'Diff-Spec-Converter':
            nodesappended = True
            print("Nodes Found, not appending")
    if nodesappended == False:
        append_nodegroups()
        print("Nodes not found, appending")


#BELOW REFERENCES THE RIG COLLECTION BLEND FILE. UPDATE IT IF THE NAME WAS CHANGED.

def append_nodegroups():
    path = os.path.dirname(__file__) + '/assets/Rig Collections 4.0.blend\\NodeTree\\'
    import_node = 'Diff-Spec-Converter'
    bpy.ops.wm.append( filename = import_node, directory = path)
    import_node2 = 'Texture-4X'
    bpy.ops.wm.append( filename = import_node2, directory = path)
    import_node3 = 'FFXIV Face Decal'
    bpy.ops.wm.append( filename = import_node3, directory = path)
    import_node4 = 'FFXIV Eye Shader'
    bpy.ops.wm.append( filename = import_node4, directory = path)
    import_node5 = 'FFXIV Skin Shader'
    bpy.ops.wm.append( filename = import_node5, directory = path)

def change_material(mat):

    print("Changing Material")
    to_remove = []
    for node in mat.node_tree.nodes:
        if node.bl_idname == 'ShaderNodeBsdfPrincipled':
            if len(node.inputs[0].links) > 0: #checking if input 0 has a connection (diffuse tex)
                checknode = node.inputs[0].links[0].from_node #assigning checknode var to that linked node
                if checknode.bl_idname != 'ShaderNodeTexImage': #if that's not an image texture, run away
                    return
                else:
                    connect_alpha(node, mat)
                    add_slap(node, mat.node_tree)
                    to_remove.append(node)
                    
    for node in to_remove:
        mat.node_tree.nodes.remove(node)
    
def connect_alpha(node, mat):
    if len(node.inputs[0].links) > 0:
        if len(node.inputs[4].links) > 0:  #Looking for the alpha on the principled bsdf sockets
            alphaNode = node.inputs[4].links[0].from_node
            if alphaNode.bl_idname == 'ShaderNodeTexImage':
                mat.node_tree.nodes.remove(alphaNode)
        mat.node_tree.links.new(node.inputs[0].links[0].from_node.outputs[1], node.inputs[24]) #Looking for the emission socket

def add_slap(node, node_tree): # Relink existing materials to custom nodegroup

    #Create groupnode
    groupnode = node_tree.nodes.new('ShaderNodeGroup')
    groupnode.node_tree = bpy.data.node_groups['FFXIV Skin Shader']


    materialOut = node.outputs[0].links[0].to_node
    normalNode = node.inputs[5].links[0].from_node #Normal node socket ?
    normalImage = normalNode.inputs[1].links[0].from_node    
    diffImage = node.inputs[0].links[0].from_node
    #Connect diff node to slap node
    node_tree.links.new(groupnode.inputs[2], diffImage.outputs[0])
    node_tree.links.new(groupnode.inputs[5], diffImage.outputs[1])
    node_tree.links.new(groupnode.inputs[4], normalImage.outputs[0])

    SpecExists = False
    if len(node.inputs[10].links) > 0: #Sometimes there's no spec-- also looking for spec socket
        SpecExists = True
        specimage = node.inputs[10].links[0].from_node
        #Connect spec node to slap node
        node_tree.links.new(groupnode.inputs[3], specimage.outputs[0])
    
    #Connect slap node outputs to main node inputs.
    node_tree.links.new(groupnode.outputs[0], materialOut.inputs[0])

    move_node(groupnode, -200, 250)
    move_node(diffImage, -300, 335)
    move_node(normalImage, 0, 1000)
    if SpecExists == True:
        move_node(specimage, 0, 80)

    node_tree.nodes.remove(normalNode)

def add_eyes(eyes):
    
    node_tree = eyes.node_tree
    
    for n in node_tree.nodes:
        if n.bl_idname != 'ShaderNodeOutputMaterial':
            node_tree.nodes.remove(n)
        else:
             materialOutput = n
             
    check_for_nodes()
    groupnode = node_tree.nodes.new('ShaderNodeGroup')
    groupnode.node_tree = bpy.data.node_groups['FFXIV Eye Shader']
                
    node_tree.links.new(groupnode.outputs[0], materialOutput.inputs[0])
    move_node(groupnode, 0, 357)

class EyeFix(bpy.types.Operator): # Adds Custom Shader to active material
    bl_idname = "myops.eyefix"
    bl_label = "Fix my goddamend eyes"
    bl_description = "Use this only on the iris material-- you have been warned."

    def execute(self, context):
        selected_material = bpy.context.active_object.active_material
        add_eyes(selected_material)

        return {"FINISHED"}

class ClearCustomSplitNormals(bpy.types.Operator):
    bl_idname = "myops.clear_split_normals"
    bl_label = "Clear custom split normals"
    bl_description = "Clear Custom Split Normals if the model looks kinda jank for some reasons. Also sets autosmooth on and to 180 degrees"
    
    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        joined_objects = bpy.context.selected_objects
    
        for object in selected_objects:
            if object.type == 'MESH':
                bpy.ops.mesh.customdata_custom_splitnormals_clear() #clear custom split normals
                bpy.context.object.data.use_auto_smooth = True  # Set autosmooth to enabled
                bpy.context.object.data.auto_smooth_angle = radians(180) # Set autosmooth to 180 degrees

        return {'FINISHED'}

class FixMetallic(bpy.types.Operator):
    bl_idname = "myops.fixmetallic"
    bl_label = "The Metalness tho"
    bl_description = "Fixes Metallic issue"
        
    def execute(self, context):
        for mat in bpy.data.materials:
            if not mat.use_nodes:
                mat.metallic = 0
                continue
            for n in mat.node_tree.nodes:
                if n.type == 'BSDF_PRINCIPLED':
                     n.inputs["Metallic"].default_value = 0  
        return {'FINISHED'}

class FK2IKOP(bpy.types.Operator): # Snaps the FK bone to the IK bone
    bl_idname = "myops.fk2iksnap"
    bl_label = "snaps the FK bones to the IK controller positions and rotations"
    bl_description= "snaps the ik controllers to the FK bones positions and rotations"
    
    def execute(self, context):
        bpy.context.object.pose.bones['__FK_ude_a_r'].matrix = bpy.context.object.pose.bones['__IK_ude_a_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_ude_a_l'].matrix = bpy.context.object.pose.bones['__IK_ude_a_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
        
        bpy.context.object.pose.bones['__FK_ude_b_r'].matrix = bpy.context.object.pose.bones['__FK_ude_b_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_ude_b_l'].matrix = bpy.context.object.pose.bones['__FK_ude_b_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
        
        bpy.context.object.pose.bones['__FK_te_r'].matrix = bpy.context.object.pose.bones['hand.IK.R'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_te_l'].matrix = bpy.context.object.pose.bones['hand.IK.L'].matrix.copy()
        bpy.context.view_layer.update()        

#Below is for the legs, above is for the arms

        bpy.context.object.pose.bones['__FK_asi_a_r'].matrix = bpy.context.object.pose.bones['__IK_asi_a_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_asi_a_l'].matrix = bpy.context.object.pose.bones['__IK_asi_a_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
        
        bpy.context.object.pose.bones['__FK_asi_c_r'].matrix = bpy.context.object.pose.bones['__IK_asi_c_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_asi_c_l'].matrix = bpy.context.object.pose.bones['__IK_asi_c_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
 #and the knee bones....
        bpy.context.object.pose.bones['__FK_asi_b_r'].matrix = bpy.context.object.pose.bones['__IK_asi_b_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_asi_b_l'].matrix = bpy.context.object.pose.bones['__IK_asi_b_l'].matrix.copy()
        bpy.context.view_layer.update()  
#... and the foot bone...
        bpy.context.object.pose.bones['__FK_asi_d_r'].matrix = bpy.context.object.pose.bones['__IK_asi_d_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_asi_d_l'].matrix = bpy.context.object.pose.bones['__IK_asi_d_l'].matrix.copy()
        bpy.context.view_layer.update() 
        
#........ and the toes..... dont need it cuz they were only ever FK

        bpy.context.object.pose.bones['__FK_te_r'].matrix = bpy.context.object.pose.bones['Leg.IK.R'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__FK_te_l'].matrix = bpy.context.object.pose.bones['Leg.IK.L'].matrix.copy()
        bpy.context.view_layer.update()             
        #needs to update after every matrix change
        return {'FINISHED'}

class IK2FKOP(bpy.types.Operator): # Snaps the IK bone to the FK bone
    bl_idname = "myops.ik2fksnap"
    bl_label = "snaps the IK controller to the FK controller positions and rotations"
    bl_description= "snaps the IK controller to the FK controller positions and rotations"
    
    def execute(self, context):
        bpy.context.object.pose.bones['__IK_ude_a_r'].matrix = bpy.context.object.pose.bones['__FK_ude_a_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__IK_ude_a_l'].matrix = bpy.context.object.pose.bones['__FK_ude_a_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
        
        bpy.context.object.pose.bones['__IK_ude_b_r'].matrix = bpy.context.object.pose.bones['__FK_ude_b_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__IK_ude_b_l'].matrix = bpy.context.object.pose.bones['__FK_ude_b_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
        
        bpy.context.object.pose.bones['hand.IK.R'].matrix = bpy.context.object.pose.bones['__FK_te_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['hand.IK.L'].matrix = bpy.context.object.pose.bones['__FK_te_l'].matrix.copy()
        bpy.context.view_layer.update()        

#Below is for the legs, above is for the arms

        bpy.context.object.pose.bones['__IK_asi_a_r'].matrix = bpy.context.object.pose.bones['__FK_asi_a_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__IK_asi_a_l'].matrix = bpy.context.object.pose.bones['__FK_asi_a_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
        
        bpy.context.object.pose.bones['__IK_asi_c_r'].matrix = bpy.context.object.pose.bones['__FK_asi_c_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__IK_asi_c_l'].matrix = bpy.context.object.pose.bones['__FK_asi_c_l'].matrix.copy()
        bpy.context.view_layer.update()        
        
 #and the knee bones....
        bpy.context.object.pose.bones['__IK_asi_b_r'].matrix = bpy.context.object.pose.bones['__FK_asi_b_r'].matrix.copy()
        bpy.context.view_layer.update()
        bpy.context.object.pose.bones['__IK_asi_b_l'].matrix = bpy.context.object.pose.bones['__FK_asi_b_l'].matrix.copy()
        bpy.context.view_layer.update()  
        
#........ and the toes..... dont need it cuz they were only ever FK. The Feet bones move when you switch between IK and FK on the property controls....
          
        #needs to update after every matrix change
        return {'FINISHED'}











#Mek Bar
def sna_add_to_view3d_ht_tool_header_40F4B(self, context):
    if not (False):
        layout = self.layout
        layout.popover('SNA_PT_DROP_DOWN_B9210', text='Mek Bar', icon_value=0)

#This is the mek bar UI stuff ^

class SNA_PT_RIG_LAYERS_14BB3(bpy.types.Panel):
    bl_label = 'Rig Layers'
    bl_idname = 'SNA_PT_RIG_LAYERS_14BB3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Mektools 0.36'
    bl_order = 3
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        if bpy.context.view_layer.objects.active.type == 'ARMATURE':
            layout.label(text='Snap the IK bones to the Loc/Rot of the FK Bones', icon_value=177)
        else:
            op = layout.operator('sn.dummy_button_operator', text='Select a MekRig', icon_value=229, emboss=False, depress=False)
        if bpy.context.view_layer.objects.active.type == 'ARMATURE':
            box_5F4E8 = layout.box()
            box_5F4E8.alert = False
            box_5F4E8.enabled = True
            box_5F4E8.active = True
            box_5F4E8.use_property_split = False
            box_5F4E8.use_property_decorate = False
            box_5F4E8.alignment = 'Expand'.upper()
            box_5F4E8.scale_x = 1.0
            box_5F4E8.scale_y = 1.0
            if not True: box_5F4E8.operator_context = "EXEC_DEFAULT"
            split_2A65F = box_5F4E8.split(factor=0.5, align=False)
            split_2A65F.alert = False
            split_2A65F.enabled = True
            split_2A65F.active = True
            split_2A65F.use_property_split = False
            split_2A65F.use_property_decorate = False
            split_2A65F.scale_x = 1.0
            split_2A65F.scale_y = 1.0
            split_2A65F.alignment = 'Expand'.upper()
            if not True: split_2A65F.operator_context = "EXEC_DEFAULT"
            op = split_2A65F.operator('myops.ik2fksnap', text='IK to FK', icon_value=0, emboss=True, depress=False)
            op = split_2A65F.operator('myops.fk2iksnap', text='FK to IK', icon_value=0, emboss=True, depress=False)
        if bpy.context.view_layer.objects.active.type == 'ARMATURE':
            box_27296 = layout.box()
            box_27296.alert = False
            box_27296.enabled = True
            box_27296.active = True
            box_27296.use_property_split = False
            box_27296.use_property_decorate = False
            box_27296.alignment = 'Expand'.upper()
            box_27296.scale_x = 1.0
            box_27296.scale_y = 1.0
            if not True: box_27296.operator_context = "EXEC_DEFAULT"
            box_27296.prop(bpy.context.active_object.data.collections['Spine'], 'is_visible', text='Torso', icon_value=0, emboss=True, toggle=bpy.context.active_object.data.collections['Spine'].is_visible)
            split_AFACC = box_27296.split(factor=0.5, align=False)
            split_AFACC.alert = False
            split_AFACC.enabled = True
            split_AFACC.active = True
            split_AFACC.use_property_split = False
            split_AFACC.use_property_decorate = False
            split_AFACC.scale_x = 1.0
            split_AFACC.scale_y = 1.0
            split_AFACC.alignment = 'Expand'.upper()
            if not True: split_AFACC.operator_context = "EXEC_DEFAULT"
            split_AFACC.prop(bpy.context.active_object.data.collections['Face'], 'is_visible', text='Face', icon_value=0, emboss=True, toggle=True)
            split_AFACC.prop(bpy.context.active_object.data.collections['Hands'], 'is_visible', text='Hands', icon_value=0, emboss=True, toggle=True)
        if bpy.context.view_layer.objects.active.type == 'ARMATURE':
            box_9F82A = layout.box()
            box_9F82A.alert = False
            box_9F82A.enabled = True
            box_9F82A.active = True
            box_9F82A.use_property_split = False
            box_9F82A.use_property_decorate = False
            box_9F82A.alignment = 'Expand'.upper()
            box_9F82A.scale_x = 1.0
            box_9F82A.scale_y = 1.0
            if not True: box_9F82A.operator_context = "EXEC_DEFAULT"
            split_59644 = box_9F82A.split(factor=0.5, align=False)
            split_59644.alert = False
            split_59644.enabled = True
            split_59644.active = True
            split_59644.use_property_split = False
            split_59644.use_property_decorate = False
            split_59644.scale_x = 1.0
            split_59644.scale_y = 1.0
            split_59644.alignment = 'Expand'.upper()
            if not True: split_59644.operator_context = "EXEC_DEFAULT"
            split_59644.prop(bpy.context.active_object.data.collections['IK Bones'], 'is_visible', text='IK', icon_value=0, emboss=True, toggle=True)
            split_59644.prop(bpy.context.active_object.data.collections['FK Bones'], 'is_visible', text='FK', icon_value=0, emboss=True, toggle=True)
            split_675E9 = box_9F82A.split(factor=0.5, align=False)
            split_675E9.alert = False
            split_675E9.enabled = True
            split_675E9.active = True
            split_675E9.use_property_split = False
            split_675E9.use_property_decorate = False
            split_675E9.scale_x = 1.0
            split_675E9.scale_y = 1.0
            split_675E9.alignment = 'Expand'.upper()
            if not True: split_675E9.operator_context = "EXEC_DEFAULT"
            split_675E9.prop(bpy.context.active_object.data.collections['Physics'], 'is_visible', text='Physics', icon_value=0, emboss=True, toggle=True)
            split_675E9.prop(bpy.context.active_object.data.collections['Extra Bones'], 'is_visible', text='Extra', icon_value=0, emboss=True, toggle=True)
        if bpy.context.view_layer.objects.active.type == 'ARMATURE':
            box_DD11B = layout.box()
            box_DD11B.alert = False
            box_DD11B.enabled = True
            box_DD11B.active = True
            box_DD11B.use_property_split = False
            box_DD11B.use_property_decorate = False
            box_DD11B.alignment = 'Expand'.upper()
            box_DD11B.scale_x = 1.0
            box_DD11B.scale_y = 1.0
            if not True: box_DD11B.operator_context = "EXEC_DEFAULT"
            box_DD11B.prop(bpy.context.active_object.data.collections['Base Bones'], 'is_visible', text='Base Bones', icon_value=0, emboss=True, toggle=True)


class SNA_OT_Addcamop_81Af4(bpy.types.Operator):
    bl_idname = "sna.addcamop_81af4"
    bl_label = "AddCamOp"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.object.camera_add('INVOKE_DEFAULT', )
        bpy.ops.view3d.object_as_camera('INVOKE_DEFAULT', )
        bpy.ops.view3d.camera_to_view('INVOKE_DEFAULT', )
        prev_context = bpy.context.area.type
        bpy.context.area.type = 'DOPESHEET_EDITOR'
        bpy.ops.marker.add('INVOKE_DEFAULT', )
        bpy.context.area.type = prev_context
        prev_context = bpy.context.area.type
        bpy.context.area.type = 'DOPESHEET_EDITOR'
        bpy.ops.marker.camera_bind('INVOKE_DEFAULT', )
        bpy.context.area.type = prev_context
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_PT_DROP_DOWN_B9210(bpy.types.Panel):
    bl_label = 'Drop Down'
    bl_idname = 'SNA_PT_DROP_DOWN_B9210'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_context = ''
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        op = layout.operator('sna.addcamop_81af4', text='Add Camera', icon_value=0, emboss=True, depress=False)
        if bpy.context.view_layer.objects.active.type == 'CAMERA':
            layout.prop(bpy.context.view_layer.objects.active.data, 'passepartout_alpha', text='Passepartout', icon_value=0, emboss=True, slider=bool(bpy.context.view_layer.objects.active.data.passepartout_alpha))
        if bpy.context.view_layer.objects.active.type == 'CAMERA':
            layout.prop(bpy.context.scene.camera.data.dof, 'use_dof', text='DOF', icon_value=0, emboss=True)
        layout.prop(bpy.context.scene.camera.data.dof, 'focus_object', text='DOF to', icon_value=0, emboss=True)
        layout.prop(bpy.context.scene.camera.data.dof, 'aperture_fstop', text='F-Stop', icon_value=0, emboss=True, slider=bool(bpy.context.scene.camera.data.dof.aperture_fstop))
        layout.prop(bpy.context.scene.camera.data, 'lens', text='Focal Length', icon_value=0, emboss=True, slider=bool(bpy.context.scene.camera.data.lens))
#Mek Bar end

def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.utils.register_class(SNA_PT_IMPORT_AND_EXPORT_D25AF)
    bpy.utils.register_class(SNA_PT_FOR_RENDERING_12387)
    bpy.utils.register_class(SNA_OT_Import_Am_C728C)
    bpy.utils.register_class(SNA_OT_Import_Af_B4751)
    bpy.utils.register_class(SNA_OT_Import_Ef_8E849)
    bpy.utils.register_class(SNA_OT_Import_Em_B2121)
    bpy.utils.register_class(SNA_OT_Import_Hf_E2D09)
    bpy.utils.register_class(SNA_OT_Import_Hrm_C1590)
    bpy.utils.register_class(SNA_OT_Import_Lala_Adb84)
    bpy.utils.register_class(SNA_OT_Import_Mf_36952)
    bpy.utils.register_class(SNA_OT_Import_Mm_02Dc3)
    bpy.utils.register_class(SNA_OT_Import_Miqf_E13B1)
    bpy.utils.register_class(SNA_OT_Import_Miqm_0929D)
    bpy.utils.register_class(SNA_OT_Import_Rf_C1Dc0)
    bpy.utils.register_class(SNA_OT_Import_Rm_39A5F)
    bpy.utils.register_class(SNA_OT_Import_Vm_4Aaf7)
    bpy.utils.register_class(SNA_OT_Import_Vf_6301C)
    bpy.utils.register_class(SNA_PT_FEMALE_RIGS_43F95)
    bpy.utils.register_class(SNA_PT_MALE_RIGS_0127C)
    bpy.utils.register_class(SNA_OT_Alphafix_4F08E)
    bpy.utils.register_class(SNA_OT_Import_Hm_52444)
    bpy.utils.register_class(SNA_PT_MEKTOOLS_036_003A7)
    bpy.types.VIEW3D_HT_tool_header.append(sna_add_to_view3d_ht_tool_header_40F4B)
    bpy.utils.register_class(SNA_PT_RIG_LAYERS_14BB3)
    bpy.utils.register_class(SNA_OT_Addcamop_81Af4)
    bpy.utils.register_class(SNA_PT_DROP_DOWN_B9210)
    bpy.utils.register_class(RemoveBones)
    bpy.utils.register_class(EyeFix)
    bpy.utils.register_class(MaterialFix)
    bpy.utils.register_class(ClearCustomSplitNormals)
    bpy.utils.register_class(FixMetallic)
    bpy.utils.register_class(FK2IKOP) 
    bpy.utils.register_class(IK2FKOP)
    


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_PT_IMPORT_AND_EXPORT_D25AF)
    bpy.utils.unregister_class(SNA_PT_FOR_RENDERING_12387)
    bpy.utils.unregister_class(SNA_OT_Import_Am_C728C)
    bpy.utils.unregister_class(SNA_OT_Import_Af_B4751)
    bpy.utils.unregister_class(SNA_OT_Import_Ef_8E849)
    bpy.utils.unregister_class(SNA_OT_Import_Em_B2121)
    bpy.utils.unregister_class(SNA_OT_Import_Hf_E2D09)
    bpy.utils.unregister_class(SNA_OT_Import_Hrm_C1590)
    bpy.utils.unregister_class(SNA_OT_Import_Lala_Adb84)
    bpy.utils.unregister_class(SNA_OT_Import_Mf_36952)
    bpy.utils.unregister_class(SNA_OT_Import_Mm_02Dc3)
    bpy.utils.unregister_class(SNA_OT_Import_Miqf_E13B1)
    bpy.utils.unregister_class(SNA_OT_Import_Miqm_0929D)
    bpy.utils.unregister_class(SNA_OT_Import_Rf_C1Dc0)
    bpy.utils.unregister_class(SNA_OT_Import_Rm_39A5F)
    bpy.utils.unregister_class(SNA_OT_Import_Vm_4Aaf7)
    bpy.utils.unregister_class(SNA_OT_Import_Vf_6301C)
    bpy.utils.unregister_class(SNA_PT_FEMALE_RIGS_43F95)
    bpy.utils.unregister_class(SNA_PT_MALE_RIGS_0127C)
    bpy.utils.unregister_class(SNA_OT_Alphafix_4F08E)
    bpy.utils.unregister_class(SNA_OT_Import_Hm_52444)
    bpy.utils.unregister_class(SNA_PT_MEKTOOLS_036_003A7)
    bpy.types.VIEW3D_HT_tool_header.remove(sna_add_to_view3d_ht_tool_header_40F4B)
    bpy.utils.unregister_class(SNA_PT_RIG_LAYERS_14BB3)
    bpy.utils.unregister_class(SNA_OT_Addcamop_81Af4)
    bpy.utils.unregister_class(SNA_PT_DROP_DOWN_B9210)
    bpy.utils.unregister_class(RemoveBones)
    bpy.utils.unregister_class(EyeFix)
    bpy.utils.unregister_class(MaterialFix)
    bpy.utils.unregister_class(ClearCustomSplitNormals)
    bpy.utils.unregister_class(FixMetallic)
    bpy.utils.unregister_class(FK2IKOP) 
    bpy.utils.unregister_class(IK2FKOP)