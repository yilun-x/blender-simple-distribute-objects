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
    "name" : "Simple Distribute Objects",
    "author" : "Allen Chia",
    "description" : "A tool to distribute multi objects.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 2),
    "location": "View3D > Sidebar > Item Tab",
    "warning" : "",
    "category" : "Object"
}

import bpy

from . distribute_pnl import DB_PT_Panel
from . distribute_op import DB_X_Op, DB_Y_Op, DB_Z_Op

classes = (DB_PT_Panel, DB_X_Op, DB_Y_Op, DB_Z_Op)
def register():
    for c in classes:
       bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()