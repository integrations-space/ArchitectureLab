# ##### BEGIN MIT LICENSE BLOCK #####
# MIT License
# 
# Copyright (c) 2018 Insma Software
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ##### END MIT LICENSE BLOCK #####

# ----------------------------------------------------------
# Author: Maciej Klemarczyk (mklemarczyk)
# ----------------------------------------------------------
import bpy
from bpy.types import Operator, PropertyGroup, Object, Panel
from bpy.props import BoolProperty, FloatProperty, CollectionProperty
from .archlab_utils import *

# ------------------------------------------------------------------------------
# Create main object for the door.
# ------------------------------------------------------------------------------
def create_door(self, context):
    # deselect all objects
    for o in bpy.data.objects:
        o.select = False

    # we create door object and mesh
    doormesh = bpy.data.meshes.new("Door")
    doorobject = bpy.data.objects.new("Door", doormesh)
    doorobject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(doorobject)
    doorobject.ArchLabDoorGenerator.add()

    doorobject.ArchLabDoorGenerator[0].door_height = self.door_height
    doorobject.ArchLabDoorGenerator[0].door_width = self.door_width
    doorobject.ArchLabDoorGenerator[0].door_depth = self.door_depth
    doorobject.ArchLabDoorGenerator[0].door_thickness = self.door_thickness
    doorobject.ArchLabDoorGenerator[0].door_armature = self.door_armature
    
    # we shape the mesh.
    shape_door_mesh(doorobject, doormesh)

    if self.door_armature:
        # we create main object and mesh for door
        doorarmature = bpy.data.armatures.new("Door Armature")
        doorarmatureobject = bpy.data.objects.new("Door Armature", doorarmature)
        doorarmatureobject.location = bpy.context.scene.cursor_location
        doorarmatureobject.parent = doorobject
        bpy.context.scene.objects.link(doorarmatureobject)

        # we shape the armature.
        shape_door_armature(doorobject, doorarmatureobject, doorarmature)

    # we select, and activate, main object for the door.
    doorobject.select = True
    bpy.context.scene.objects.active = doorobject

# ------------------------------------------------------------------------------
# Shapes mesh and creates modifier solidify (the modifier, only the first time).
# ------------------------------------------------------------------------------
def shape_door_mesh(mydoor, tmp_mesh, update=False):
    sp = mydoor.ArchLabDoorGenerator[0]  # "sp" means "door properties".
    # Create door mesh data
    update_door_mesh_data(tmp_mesh, sp.door_width, sp.door_height, sp.door_depth, sp.door_thickness)
    mydoor.data = tmp_mesh

    remove_doubles(mydoor)
    set_normals(mydoor)

    # Create Door vertex group
    if not is_vertex_group(mydoor, 'Door Door'):
        doorvg = mydoor.vertex_groups.new()
        doorvg.name = 'Door Door'
        doorvg.add(index=[8, 9, 11, 10], weight=1, type='ADD')

    if sp.door_thickness > 0.0:
        if update is False or is_solidify(mydoor) is False:
            set_modifier_solidify(mydoor, sp.door_thickness)
        else:
            for mod in mydoor.modifiers:
                if mod.type == 'SOLIDIFY':
                    mod.thickness = sp.door_thickness
        # Move to Top SOLIDIFY
        movetotopsolidify(mydoor)

    else:  # clear not used SOLIDIFY
        for mod in mydoor.modifiers:
            if mod.type == 'SOLIDIFY':
                mydoor.modifiers.remove(mod)

    # deactivate others
    for o in bpy.data.objects:
        if o.select is True and o.name != mydoor.name:
            o.select = False

# ------------------------------------------------------------------------------
# Shapes armature and creates modifier armature (the modifier, only the first time).
# ------------------------------------------------------------------------------
def shape_door_armature(mydoor, myarmatureobj, myarmature, update=False):
    sp = mydoor.ArchLabDoorGenerator[0]  # "sp" means "door properties".
    # Create door armature data
    update_door_armature_data(myarmatureobj, myarmature, sp.door_width, sp.door_height, sp.door_depth, sp.door_thickness)

    if sp.door_armature:
        if update is False or is_armature(mydoor) is False:
            set_modifier_armature(mydoor, myarmatureobj)
        else:
            for mod in mydoor.modifiers:
                if mod.type == 'ARMATURE':
                    mod.thickness = sp.door_thickness
        # Move to Top ARMATURE
        movetotoparmature(mydoor)

    else:  # clear not used ARMATURE
        for mod in mydoor.modifiers:
            if mod.type == 'ARMATURE':
                mydoor.modifiers.remove(mod)

# ------------------------------------------------------------------------------
# Creates door mesh data.
# ------------------------------------------------------------------------------
def update_door_mesh_data(mymesh, width, height, depth, thickness):
    basethick = thickness /2
    posx = width /2
    posy = depth /2
    posz = height +basethick

    myvertices = [
        (-posx, -posy, basethick), (posx, -posy, basethick),
        (-posx, posy, basethick), (posx, posy, basethick),
        (-posx, -posy, posz), (posx, -posy, posz),
        (-posx, posy, posz), (posx, posy, posz)]

    thickdiff = thickness /2 + 0.001
    myvertices.extend([
        (-posx + thickdiff, -posy + thickdiff, basethick + thickdiff),
        (posx - thickdiff, -posy + thickdiff, basethick + thickdiff),
        (-posx + thickdiff, -posy + thickdiff, posz - thickdiff),
        (posx - thickdiff, -posy + thickdiff, posz - thickdiff)
    ])

    myfaces = [
        (0, 1, 3, 2),
        (0, 4, 6, 2),
        (1, 5, 7, 3),
        (4, 5, 7, 6),

        (8, 9, 11, 10)
    ]

    mymesh.from_pydata(myvertices, [], myfaces)
    mymesh.update(calc_edges=True)

# ------------------------------------------------------------------------------
# Creates door armature data.
# ------------------------------------------------------------------------------
def update_door_armature_data(myarmatureobj, myarmature, width, height, depth, thickness):
    basethick = thickness /2
    posx = width /2
    posy = depth /2
    posz = height /2 +basethick
    thickdiff = thickness /2 + 0.001

    prev_o = bpy.context.scene.objects.active
    bpy.context.scene.objects.active = myarmatureobj
    myarmatureobj.select = True
    bpy.ops.object.editmode_toggle()

    doorbone = myarmature.edit_bones.new('Door Door')
    doorbone.head = (posx - thickdiff, -posy + thickdiff, posz )
    doorbone.tail = (-posx + thickdiff, -posy + thickdiff, posz)

    bpy.ops.object.editmode_toggle()
    bpy.context.scene.objects.active = prev_o

    doorbone = myarmatureobj.pose.bones[0]
    doorbone.rotation_mode = 'XYZ'
    doorbone.lock_location[0] = True
    doorbone.lock_location[1] = True
    doorbone.lock_location[2] = True
    doorbone.lock_rotation[0] = True
    doorbone.lock_rotation[1] = True
    doorbone.lock_scale[0] = True
    doorbone.lock_scale[1] = True
    doorbone.lock_scale[2] = True

# ------------------------------------------------------------------------------
# Update door mesh.
# ------------------------------------------------------------------------------
def update_door(self, context):
    # When we update, the active object is the main object of the door.
    o = bpy.context.active_object
    oldmesh = o.data
    oldname = o.data.name
    # Now we deselect that door object to not delete it.
    o.select = False
    # and we create a new mesh for the door:
    tmp_mesh = bpy.data.meshes.new("temp")
    # deselect all objects
    for obj in bpy.data.objects:
        obj.select = False
    # Finally we shape the main mesh again,
    shape_door_mesh(o, tmp_mesh, True)
    o.data = tmp_mesh
    # Remove data (mesh of active object),
    bpy.data.meshes.remove(oldmesh)
    tmp_mesh.name = oldname
    # and select, and activate, the main object of the door.
    o.select = True
    bpy.context.scene.objects.active = o

# -----------------------------------------------------
# Verify if vertex group exist
# -----------------------------------------------------
def is_vertex_group(myobject, vgname):
    flag = False
    try:
        if myobject.vertex_groups is None:
            return False

        for vg in myobject.vertex_groups:
            if vg.name == vgname:
                flag = True
                break
        return flag
    except AttributeError:
        return False

# -----------------------------------------------------
# Verify if armature exist
# -----------------------------------------------------
def is_armature(myobject):
    flag = False
    try:
        if myobject.modifiers is None:
            return False

        for mod in myobject.modifiers:
            if mod.type == 'ARMATURE':
                flag = True
                break
        return flag
    except AttributeError:
        return False

# -----------------------------------------------------
# Move Armature to Top
# -----------------------------------------------------
def movetotoparmature(myobject):
    mymod = None
    try:
        if myobject.modifiers is not None:
            for mod in myobject.modifiers:
                if mod.type == 'ARMATURE':
                    mymod = mod

            if mymod is not None:
                while myobject.modifiers[0] != mymod:
                    bpy.ops.object.modifier_move_up(modifier=mymod.name)
    except AttributeError:
        return

# -----------------------------------------------------
# Verify if solidify exist
# -----------------------------------------------------
def is_solidify(myobject):
    flag = False
    try:
        if myobject.modifiers is None:
            return False

        for mod in myobject.modifiers:
            if mod.type == 'SOLIDIFY':
                flag = True
                break
        return flag
    except AttributeError:
        return False

# -----------------------------------------------------
# Move Solidify to Top
# -----------------------------------------------------
def movetotopsolidify(myobject):
    mymod = None
    try:
        if myobject.modifiers is not None:
            for mod in myobject.modifiers:
                if mod.type == 'SOLIDIFY':
                    mymod = mod

            if mymod is not None:
                while myobject.modifiers[0] != mymod:
                    bpy.ops.object.modifier_move_up(modifier=mymod.name)
    except AttributeError:
        return

# -----------------------------------------------------
# Property definition creator
# -----------------------------------------------------
def door_height_property(callback=None):
    return FloatProperty(
            name='Height',
            soft_min=1.875,
            default=2.0, precision=3, unit = 'LENGTH',
            description='Door height', update=callback,
            )

def door_width_property(callback=None):
    return FloatProperty(
            name='Width',
            soft_min=0.625,
            default=0.875, precision=3, unit = 'LENGTH',
            description='Door width', update=callback,
            )

def door_depth_property(callback=None):
    return FloatProperty(
            name='Depth',
            soft_min=0.001,
            default=0.20, precision=3, unit = 'LENGTH',
            description='Door depth', update=callback,
            )

def door_thickness_property(callback=None):
    return FloatProperty(
            name='Thickness',
            soft_min=0.001,
            default=0.015, precision=4, unit = 'LENGTH',
            description='Thickness of the door', update=callback,
            )

def door_armature_property(callback=None):
    return BoolProperty(
            name='Armature',
            default=False,
            description='Create armature for the door door', update=callback,
            )

# ------------------------------------------------------------------
# Define property group class to create or modify a doors.
# ------------------------------------------------------------------
class ArchLabDoorProperties(PropertyGroup):
    door_height = door_height_property(callback=update_door)
    door_width = door_width_property(callback=update_door)
    door_depth = door_depth_property(callback=update_door)
    door_thickness = door_thickness_property(callback=update_door)
    door_armature = door_armature_property(callback=update_door)

bpy.utils.register_class(ArchLabDoorProperties)
Object.ArchLabDoorGenerator = CollectionProperty(type=ArchLabDoorProperties)

# ------------------------------------------------------------------
# Define panel class to modify doors.
# ------------------------------------------------------------------
class ArchLabDoorGeneratorPanel(Panel):
    bl_idname = "OBJECT_PT_door_generator"
    bl_label = "Architecture Lab"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'

    # -----------------------------------------------------
    # Verify if visible
    # -----------------------------------------------------
    @classmethod
    def poll(cls, context):
        o = context.object
        act_op = context.active_operator
        if o is None:
            return False
        if 'ArchLabDoorGenerator' not in o:
            return False
        if act_op is not None and act_op.bl_idname.endswith('archlab_door'):
            return False
        if o.ArchLabDoorGenerator[0].door_armature:
            return False
        else:
            return True

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        o = context.object
        # If the selected object didn't be created with the group 'ArchLabDoorGenerator', this panel is not created.
        try:
            if 'ArchLabDoorGenerator' not in o:
                return
        except:
            return

        layout = self.layout
        if bpy.context.mode == 'EDIT_MESH':
            layout.label('Warning: Operator does not work in edit mode.', icon='ERROR')
        else:
            door = o.ArchLabDoorGenerator[0]
            row = layout.row()
            row.prop(door, 'door_width')
            row = layout.row()
            row.prop(door, 'door_height')
            row = layout.row()
            row.prop(door, 'door_depth')
            row = layout.row()
            row.prop(door, 'door_thickness')

# ------------------------------------------------------------------
# Define operator class to create doors
# ------------------------------------------------------------------
class ArchLabDoor(Operator):
    bl_idname = "mesh.archlab_door"
    bl_label = "Add Door"
    bl_description = "Generate door mesh"
    bl_category = 'ArchLab'
    bl_options = {'REGISTER', 'UNDO'}

    # preset
    door_height = door_height_property()
    door_width = door_width_property()
    door_depth = door_depth_property()
    door_thickness = door_thickness_property()
    door_armature = door_armature_property()

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if not space.local_view:
            row = layout.row()
            row.prop(self, 'door_width')
            row = layout.row()
            row.prop(self, 'door_height')
            row = layout.row()
            row.prop(self, 'door_depth')
            row = layout.row()
            row.prop(self, 'door_thickness')
            row = layout.row()
            row.prop(self, 'door_armature')
        else:
            row = layout.row()
            row.label("Warning: Operator does not work in local view mode", icon='ERROR')

    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------
    def execute(self, context):
        if bpy.context.mode == "OBJECT":
            space = bpy.context.space_data
            if not space.local_view:
                create_door(self, context)
                return {'FINISHED'}
            else:
                self.report({'WARNING'}, "ArchLab: Option only valid in global view mode")
                return {'CANCELLED'}
        else:
            self.report({'WARNING'}, "ArchLab: Option only valid in Object mode")
            return {'CANCELLED'}
