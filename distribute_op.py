import bpy
from bpy.types import Operator

class DB_X_Op(Operator):
    bl_idname = "object.db_ot_distribute_x"
    bl_label = "X"
    bl_description = "Distribute objects that you have selected from X axis"


    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True

        return False

    def execute(self, context):
        selected_objects = context.selected_objects
        xdict = {}
        for so in selected_objects:
            #so.location = (10.0, 10.0, 10.0)
            xdict[so] = so.location[0]
        sorteddict = sorted(xdict.items(), key=lambda obj: obj[1])
        distanceX = abs(sorteddict[0][1] - sorteddict[-1][1])
        stepX = distanceX / (len(sorteddict) - 1)
        for la in range(len(sorteddict)):
            if (la != 0 and la != len(sorteddict)-1):
                sorteddict[la][0].location = ((sorteddict[0][1]) + stepX * la, sorteddict[la][0].location[1], sorteddict[la][0].location[2])
        return {'FINISHED'}

class DB_Y_Op(Operator):
    bl_idname = "object.db_ot_distribute_y"
    bl_label = "Y"
    bl_description = "Distribute objects that you have selected from Y axis"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None:
            if obj.mode == "OBJECT":
                return True

        return False

    def execute(self, context):
        selected_objects = context.selected_objects
        ydict = {}
        for so in selected_objects:
            ydict[so] = so.location[1]
        sorteddict = sorted(ydict.items(), key=lambda obj: obj[1])
        distanceY = abs(sorteddict[0][1] - sorteddict[-1][1])
        stepY = distanceY / (len(sorteddict) - 1)
        for la in range(len(sorteddict)):
            if (la != 0 and la != len(sorteddict)-1):
                sorteddict[la][0].location = (sorteddict[la][0].location[0], (sorteddict[0][1]) + stepY * la, sorteddict[la][0].location[2])
        return {'FINISHED'}


class DB_Z_Op(Operator):
    bl_idname = "object.db_ot_distribute_z"
    bl_label = "Z"
    bl_description = "Distribute objects that you have selected from Z axis"
    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True

        return False
    def execute(self, context):
        selected_objects = context.selected_objects
        zdict = {}
        for so in selected_objects:
            zdict[so] = so.location[2]
        sorteddict = sorted(zdict.items(), key=lambda obj: obj[1])
        distanceZ = abs(sorteddict[0][1] - sorteddict[-1][1])
        stepZ = distanceZ / (len(sorteddict) - 1)
        for la in range(len(sorteddict)):
            if (la != 0 and la != len(sorteddict)-1):
                sorteddict[la][0].location = (sorteddict[la][0].location[0], sorteddict[la][0].location[1], (sorteddict[0][1]) + stepZ * la)
        return {'FINISHED'}