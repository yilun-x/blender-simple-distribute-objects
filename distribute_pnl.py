import bpy

from bpy.types import Panel

class DB_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Distribute Objects"
    bl_category = "Item"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):

        layout = self.layout

        # 3 Columns with buttons
        row = layout.row()
        col = row.column()
        col.operator("object.db_ot_distribute_x", text = "X")

        col = row.column()
        col.operator("object.db_ot_distribute_y", text = "Y")

        col = row.column()
        col.operator("object.db_ot_distribute_z", text = "Z")
