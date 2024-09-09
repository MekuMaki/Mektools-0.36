import bpy # type: ignore

class MEK_LinksPanel(bpy.types.Panel):
    bl_label = 'Mektools 0.36'
    bl_idname = 'MEK_LinksPanel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mektools 0.36'

    def draw(self, context):
        layout = self.layout
        exec('op =' + 'layout.' + 'operator(' + "'wm.url_open'," + "text='Support me on Patreon!'," + 'icon_value=227,' + 'emboss=True,' + 'depress=False,)' + ".url = '" + 'https://www.patreon.com/MekuuMaki' + "'")
        exec('op =' + 'layout.' + 'operator(' + "'wm.url_open'," + "text='Join the Discord! (18+ only)'," + 'icon_value=227,' + 'emboss=True,' + 'depress=False,)' + ".url = '" + 'https://www.discord.gg/98DqcKE' + "'")