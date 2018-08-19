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
from bpy.props import FloatProperty, CollectionProperty
from .archlab_utils import *

# ------------------------------------------------------------------------------
# Create main object for the window.
# ------------------------------------------------------------------------------
def create_window(self, context):
    # deselect all objects
    for o in bpy.data.objects:
        o.select = False

    # we create main object and mesh for window
    windowmesh = bpy.data.meshes.new("Window")
    windowobject = bpy.data.objects.new("Window", windowmesh)
    windowobject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(windowobject)
    windowobject.ArchLabWindowGenerator.add()

    windowobject.ArchLabWindowGenerator[0].window_height = self.window_height
    windowobject.ArchLabWindowGenerator[0].window_width = self.window_width
    windowobject.ArchLabWindowGenerator[0].window_depth = self.window_depth

    # we shape the mesh.
    shape_window_mesh(windowobject, windowmesh)

    # we select, and activate, main object for the window.
    windowobject.select = True
    bpy.context.scene.objects.active = windowobject

# ------------------------------------------------------------------------------
# Shapes mesh and creates modifier solidify (the modifier, only the first time).
# ------------------------------------------------------------------------------
def shape_window_mesh(mywindow, tmp_mesh, update=False):
    wip = mywindow.ArchLabWindowGenerator[0]  # "wip" means "window properties".
    # Create window mesh data
    update_window_mesh_data(tmp_mesh, wip.window_width, wip.window_height, wip.window_depth)
    mywindow.data = tmp_mesh

    remove_doubles(mywindow)
    #set_normals(mywindow)

    # deactivate others
    for o in bpy.data.objects:
        if o.select is True and o.name != mywindow.name:
            o.select = False

# ------------------------------------------------------------------------------
# Creates window mesh data.
# ------------------------------------------------------------------------------
def update_window_mesh_data(mymesh, width, height, depth):
    posx = width /2
    posy = depth /2
    posz = height /2
    frame = 0.055
    framed = 0.015

    myvertices = [
        (-posx, -posy, -posz), (posx, -posy, -posz), (-posx, posy, -posz), (posx, posy, -posz),
        (-posx, -posy, posz), (posx, -posy, posz), (-posx, posy, posz), (posx, posy, posz)
    ]

    posx = posx - frame
    posz = posz - frame
    myvertices.extend([
        (-posx, -posy, -posz), (posx, -posy, -posz), (-posx, posy, -posz), (posx, posy, -posz),
        (-posx, -posy, posz), (posx, -posy, posz), (-posx, posy, posz), (posx, posy, posz)
    ])

    posy = posy - framed
    myvertices.extend([
        (-posx, -posy, -posz), (posx, -posy, -posz), (-posx, posy, -posz), (posx, posy, -posz),
        (-posx, -posy, posz), (posx, -posy, posz), (-posx, posy, posz), (posx, posy, posz)
    ])

    myfaces = [
        (1, 0, 2, 3), (2, 0, 4, 6), (1, 3, 7, 5), (4, 5, 7, 6),                 # # # B T L R

        (0, 1, 9, 8), (5, 4, 12, 13), (4, 0, 8, 12), (1, 5, 13, 9),             # F # B T L R
        (3, 2, 10, 11), (6, 7, 15, 14), (2, 6, 14, 10), (7, 3, 11, 15),         # B # B T R L

        (8, 9, 17, 16), (13, 12, 20, 21), (12, 8, 16, 20), (9, 13, 21, 17),     # F # B T L R
        (11, 10, 18, 19), (14, 15, 23, 22), (10, 14, 22, 18), (15, 11, 19, 23), # B # B T R L

        (16, 17, 21, 20), (19, 18, 22, 23)                                      # F B # #
    ]

    mymesh.from_pydata(myvertices, [], myfaces)
    mymesh.update(calc_edges=True)

# ------------------------------------------------------------------------------
# Update window mesh.
# ------------------------------------------------------------------------------
def update_window(self, context):
    # When we update, the active object is the main object of the window.
    o = bpy.context.active_object
    oldmesh = o.data
    oldname = o.data.name
    # Now we deselect that window object to not delete it.
    o.select = False
    # and we create a new mesh for the window:
    tmp_mesh = bpy.data.meshes.new("temp")
    # deselect all objects
    for obj in bpy.data.objects:
        obj.select = False
    # Finally we shape the main mesh again,
    shape_window_mesh(o, tmp_mesh, True)
    o.data = tmp_mesh
    # Remove data (mesh of active object),
    bpy.data.meshes.remove(oldmesh)
    tmp_mesh.name = oldname
    # and select, and activate, the main object of the window.
    o.select = True
    bpy.context.scene.objects.active = o

# -----------------------------------------------------
# Property definition creator
# -----------------------------------------------------
def window_height_property(callback=None):
    return FloatProperty(
            name='Height',
            soft_min=0.375,
            default=1.25, precision=3, unit = 'LENGTH',
            description='Window height', update=callback,
            )

def window_width_property(callback=None):
    return FloatProperty(
            name='Width',
            soft_min=0.375,
            default=1.5, precision=3, unit = 'LENGTH',
            description='Window width', update=callback,
            )

def window_depth_property(callback=None):
    return FloatProperty(
            name='Thickness',
            soft_min=0.001,
            default=0.075, precision=4, unit = 'LENGTH',
            description='Thickness of the window', update=callback,
            )

# ------------------------------------------------------------------
# Define property group class to create or modify a windows.
# ------------------------------------------------------------------
class ArchLabWindowProperties(PropertyGroup):
    window_height = window_height_property(callback=update_window)
    window_width = window_width_property(callback=update_window)
    window_depth = window_depth_property(callback=update_window)

bpy.utils.register_class(ArchLabWindowProperties)
Object.ArchLabWindowGenerator = CollectionProperty(type=ArchLabWindowProperties)

# ------------------------------------------------------------------
# Define panel class to modify windows.
# ------------------------------------------------------------------
class ArchLabWindowGeneratorPanel(Panel):
    bl_idname = "OBJECT_PT_window_generator"
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
        if 'ArchLabWindowGenerator' not in o:
            return False
        if act_op is not None and act_op.bl_idname.endswith('archlab_window'):
            return False
        else:
            return True

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        o = context.object
        # If the selected object didn't be created with the group 'ArchLabWindowGenerator', this panel is not created.
        try:
            if 'ArchLabWindowGenerator' not in o:
                return
        except:
            return

        layout = self.layout
        if bpy.context.mode == 'EDIT_MESH':
            layout.label('Warning: Operator does not work in edit mode.', icon='ERROR')
        else:
            window = o.ArchLabWindowGenerator[0]
            row = layout.row()
            row.prop(window, 'window_width')
            row = layout.row()
            row.prop(window, 'window_height')
            row = layout.row()
            row.prop(window, 'window_depth')

# ------------------------------------------------------------------
# Define operator class to create windows
# ------------------------------------------------------------------
class ArchLabWindow(Operator):
    bl_idname = "mesh.archlab_window"
    bl_label = "Add Window"
    bl_description = "Generate window mesh"
    bl_category = 'ArchLab'
    bl_options = {'REGISTER', 'UNDO'}

    # preset
    window_height = window_height_property()
    window_width = window_width_property()
    window_depth = window_depth_property()

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if not space.local_view:
            row = layout.row()
            row.prop(self, 'window_width')
            row = layout.row()
            row.prop(self, 'window_height')
            row = layout.row()
            row.prop(self, 'window_depth')
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
                create_window(self, context)
                return {'FINISHED'}
            else:
                self.report({'WARNING'}, "ArchLab: Option only valid in global view mode")
                return {'CANCELLED'}
        else:
            self.report({'WARNING'}, "ArchLab: Option only valid in Object mode")
            return {'CANCELLED'}
