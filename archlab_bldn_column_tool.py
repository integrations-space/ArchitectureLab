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
from bpy.props import EnumProperty, IntProperty, FloatProperty, CollectionProperty
from .archlab_utils import *
from .archlab_utils_mesh_generator import *

# ------------------------------------------------------------------------------
# Create main object for the column.
# ------------------------------------------------------------------------------
def create_column(self, context):
    # deselect all objects
    for o in bpy.data.objects:
        o.select = False

    # we create main object and mesh for column
    columnmesh = bpy.data.meshes.new("Column")
    columnobject = bpy.data.objects.new("Column", columnmesh)
    columnobject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(columnobject)
    columnobject.ArchLabColumnGenerator.add()

    columnobject.ArchLabColumnGenerator[0].column_radius = self.column_radius
    columnobject.ArchLabColumnGenerator[0].column_segments = self.column_segments
    columnobject.ArchLabColumnGenerator[0].column_height = self.column_height

    # we shape the mesh.
    shape_column_mesh(columnobject, columnmesh)

    # we select, and activate, main object for the column.
    columnobject.select = True
    bpy.context.scene.objects.active = columnobject

# ------------------------------------------------------------------------------
# Shapes mesh and creates modifier solidify (the modifier, only the first time).
# ------------------------------------------------------------------------------
def shape_column_mesh(mycolumn, tmp_mesh, update=False):
    cp = mycolumn.ArchLabColumnGenerator[0]  # "cp" means "column properties".
    # Create column mesh data
    update_column_mesh_data(tmp_mesh, cp.column_radius, cp.column_segments, cp.column_height)
    mycolumn.data = tmp_mesh

    remove_doubles(mycolumn)
    set_normals(mycolumn)

    # deactivate others
    for o in bpy.data.objects:
        if o.select is True and o.name != mycolumn.name:
            o.select = False

# ------------------------------------------------------------------------------
# Creates column mesh data.
# ------------------------------------------------------------------------------
def update_column_mesh_data(mymesh, radius, segments, height):
    (myvertices, myedges, myfaces) = generate_mesh_from_library(
        'Column01',
        size=(radius, radius, height),
        segments=segments
    )

    mymesh.from_pydata(myvertices, myedges, myfaces)
    mymesh.update(calc_edges=True)

# ------------------------------------------------------------------------------
# Update column mesh.
# ------------------------------------------------------------------------------
def update_column(self, context):
    # When we update, the active object is the main object of the column.
    o = bpy.context.active_object
    oldmesh = o.data
    oldname = o.data.name
    # Now we deselect that column object to not delete it.
    o.select = False
    # and we create a new mesh for the column:
    tmp_mesh = bpy.data.meshes.new("temp")
    # deselect all objects
    for obj in bpy.data.objects:
        obj.select = False
    # Finally we shape the main mesh again,
    shape_column_mesh(o, tmp_mesh, True)
    o.data = tmp_mesh
    # Remove data (mesh of active object),
    bpy.data.meshes.remove(oldmesh)
    tmp_mesh.name = oldname
    # and select, and activate, the main object of the column.
    o.select = True
    bpy.context.scene.objects.active = o


# -----------------------------------------------------
# Property definition creator
# -----------------------------------------------------
def column_radius_property(callback=None):
    return FloatProperty(
            name='Radius',
            soft_min=0.001,
            default=0.15, precision=3, unit='LENGTH',
            description='Column radius', update=callback,
            )

def column_segments_property(callback=None):
    return IntProperty(
            name='Segments',
            min=3, max=1000,
            default=16,
            description='Column vertices', update=callback,
            )

def column_height_property(callback=None):
    return FloatProperty(
            name='Height',
            soft_min=0.001,
            default=2.5, precision=3, unit='LENGTH',
            description='Column height', update=callback,
            )

# ------------------------------------------------------------------
# Define property group class to create or modify a columns.
# ------------------------------------------------------------------
class ArchLabColumnProperties(PropertyGroup):
    column_radius = column_radius_property(callback=update_column)
    column_segments = column_segments_property(callback=update_column)
    column_height = column_height_property(callback=update_column)

bpy.utils.register_class(ArchLabColumnProperties)
Object.ArchLabColumnGenerator = CollectionProperty(type=ArchLabColumnProperties)

# ------------------------------------------------------------------
# Define panel class to modify columns.
# ------------------------------------------------------------------
class ArchLabColumnGeneratorPanel(Panel):
    bl_idname = "OBJECT_PT_column_generator"
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
        if 'ArchLabColumnGenerator' not in o:
            return False
        if act_op is not None and act_op.bl_idname.endswith('archlab_column'):
            return False
        else:
            return True

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        o = context.object
        # If the selected object didn't be created with the group 'ArchLabColumnGenerator', this panel is not created.
        try:
            if 'ArchLabColumnGenerator' not in o:
                return
        except:
            return

        layout = self.layout
        if bpy.context.mode == 'EDIT_MESH':
            layout.label('Warning: Operator does not work in edit mode.', icon='ERROR')
        else:
            column = o.ArchLabColumnGenerator[0]
            row = layout.row()
            row.prop(column, 'column_segments')
            row = layout.row()
            row.prop(column, 'column_radius')
            row = layout.row()
            row.prop(column, 'column_height')

# ------------------------------------------------------------------
# Define operator class to create columns
# ------------------------------------------------------------------
class ArchLabColumn(Operator):
    bl_idname = "mesh.archlab_column"
    bl_label = "Add Column"
    bl_description = "Generate column primitive mesh"
    bl_category = 'ArchLab'
    bl_options = {'REGISTER', 'UNDO'}

    # preset
    column_radius = column_radius_property()
    column_segments = column_segments_property()
    column_height = column_height_property()

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if not space.local_view:
            row = layout.row()
            row.prop(self, 'column_segments')
            row = layout.row()
            row.prop(self, 'column_radius')
            row = layout.row()
            row.prop(self, 'column_height')
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
                create_column(self, context)
                return {'FINISHED'}
            else:
                self.report({'WARNING'}, "ArchLab: Option only valid in global view mode")
                return {'CANCELLED'}
        else:
            self.report({'WARNING'}, "ArchLab: Option only valid in Object mode")
            return {'CANCELLED'}
