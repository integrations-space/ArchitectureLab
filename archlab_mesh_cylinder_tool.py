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
# Create main object for the cylinder.
# ------------------------------------------------------------------------------
def create_cylinder(self, context):
    # deselect all objects
    for o in bpy.data.objects:
        o.select = False

    # we create main object and mesh for cylinder
    cylindermesh = bpy.data.meshes.new("Cylinder")
    cylinderobject = bpy.data.objects.new("Cylinder", cylindermesh)
    cylinderobject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(cylinderobject)
    cylinderobject.ArchLabCylinderGenerator.add()

    cylinderobject.ArchLabCylinderGenerator[0].cylinder_radius = self.cylinder_radius
    cylinderobject.ArchLabCylinderGenerator[0].cylinder_quality = self.cylinder_quality
    cylinderobject.ArchLabCylinderGenerator[0].cylinder_depth = self.cylinder_depth
    cylinderobject.ArchLabCylinderGenerator[0].cylinder_cup_fill_type = self.cylinder_cup_fill_type

    # we shape the mesh.
    shape_cylinder_mesh(cylinderobject, cylindermesh)

    # we select, and activate, main object for the cylinder.
    cylinderobject.select = True
    bpy.context.scene.objects.active = cylinderobject

# ------------------------------------------------------------------------------
# Shapes mesh and creates modifier solidify (the modifier, only the first time).
# ------------------------------------------------------------------------------
def shape_cylinder_mesh(mycylinder, tmp_mesh, update=False):
    cp = mycylinder.ArchLabCylinderGenerator[0]  # "cp" means "cylinder properties".
    # Create cylinder mesh data
    update_cylinder_mesh_data(tmp_mesh, cp.cylinder_radius, cp.cylinder_quality, cp.cylinder_depth, cp.cylinder_cup_fill_type)
    mycylinder.data = tmp_mesh

    remove_doubles(mycylinder)
    set_normals(mycylinder)

    # deactivate others
    for o in bpy.data.objects:
        if o.select is True and o.name != mycylinder.name:
            o.select = False

# ------------------------------------------------------------------------------
# Creates cylinder mesh data.
# ------------------------------------------------------------------------------
def update_cylinder_mesh_data(mymesh, radius, vertices, depth, fill_type):
    if fill_type == 'NONE':
        (myvertices, myedges, myfaces) = generate_cylinder_nofill_mesh_data(radius, vertices, depth)
    if fill_type == 'NGON':
        (myvertices, myedges, myfaces) = generate_cylinder_ngonfill_mesh_data(radius, vertices, depth)
    if fill_type == 'TRIF':
        (myvertices, myedges, myfaces) = generate_cylinder_tfanfill_mesh_data(radius, vertices, depth)

    mymesh.from_pydata(myvertices, myedges, myfaces)
    mymesh.update(calc_edges=True)

# ------------------------------------------------------------------------------
# Update cylinder mesh.
# ------------------------------------------------------------------------------
def update_cylinder(self, context):
    # When we update, the active object is the main object of the cylinder.
    o = bpy.context.active_object
    oldmesh = o.data
    oldname = o.data.name
    # Now we deselect that cylinder object to not delete it.
    o.select = False
    # and we create a new mesh for the cylinder:
    tmp_mesh = bpy.data.meshes.new("temp")
    # deselect all objects
    for obj in bpy.data.objects:
        obj.select = False
    # Finally we shape the main mesh again,
    shape_cylinder_mesh(o, tmp_mesh, True)
    o.data = tmp_mesh
    # Remove data (mesh of active object),
    bpy.data.meshes.remove(oldmesh)
    tmp_mesh.name = oldname
    # and select, and activate, the main object of the cylinder.
    o.select = True
    bpy.context.scene.objects.active = o


# -----------------------------------------------------
# Property definition creator
# -----------------------------------------------------
def cylinder_radius_property(callback=None):
    return FloatProperty(
            name='Radius',
            soft_min=0.001,
            default=1.0, precision=3, unit='LENGTH',
            description='Cylinder radius', update=callback,
            )

def cylinder_quality_property(callback=None):
    return IntProperty(
            name='Vertices',
            min=3, max=1000,
            default=32,
            description='Cylinder vertices', update=callback,
            )

def cylinder_depth_property(callback=None):
    return FloatProperty(
            name='Depth',
            soft_min=0.001,
            default=2.0, precision=3, unit='LENGTH',
            description='Cylinder depth', update=callback,
            )

def cylinder_cup_fill_type_property(callback=None):
    return EnumProperty(
            items=(
                ('TRIF', 'Triangle Fan', ''),
                ('NGON', 'Ngon', ''),
                ('NONE', 'Nothing', ''),
                ),
            name='Cup Fill Type',
            description='Topology of cylinder cups face', update=callback,
            )

# ------------------------------------------------------------------
# Define property group class to create or modify a cylinders.
# ------------------------------------------------------------------
class ArchLabCylinderProperties(PropertyGroup):
    cylinder_radius = cylinder_radius_property(callback=update_cylinder)
    cylinder_quality = cylinder_quality_property(callback=update_cylinder)
    cylinder_depth = cylinder_depth_property(callback=update_cylinder)
    cylinder_cup_fill_type = cylinder_cup_fill_type_property(callback=update_cylinder)

bpy.utils.register_class(ArchLabCylinderProperties)
Object.ArchLabCylinderGenerator = CollectionProperty(type=ArchLabCylinderProperties)

# ------------------------------------------------------------------
# Define panel class to modify cylinders.
# ------------------------------------------------------------------
class ArchLabCylinderGeneratorPanel(Panel):
    bl_idname = "OBJECT_PT_cylinder_generator"
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
        if 'ArchLabCylinderGenerator' not in o:
            return False
        if act_op is not None and act_op.bl_idname.endswith('archlab_cylinder'):
            return False
        else:
            return True

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        o = context.object
        # If the selected object didn't be created with the group 'ArchLabCylinderGenerator', this panel is not created.
        try:
            if 'ArchLabCylinderGenerator' not in o:
                return
        except:
            return

        layout = self.layout
        if bpy.context.mode == 'EDIT_MESH':
            layout.label('Warning: Operator does not work in edit mode.', icon='ERROR')
        else:
            cylinder = o.ArchLabCylinderGenerator[0]
            row = layout.row()
            row.prop(cylinder, 'cylinder_quality')
            row = layout.row()
            row.prop(cylinder, 'cylinder_radius')
            row = layout.row()
            row.prop(cylinder, 'cylinder_depth')
            row = layout.row()
            row.prop(cylinder, 'cylinder_cup_fill_type')

# ------------------------------------------------------------------
# Define operator class to create cylinders
# ------------------------------------------------------------------
class ArchLabCylinder(Operator):
    bl_idname = "mesh.archlab_cylinder"
    bl_label = "Add Cylinder"
    bl_description = "Generate cylinder primitive mesh"
    bl_category = 'ArchLab'
    bl_options = {'REGISTER', 'UNDO'}

    # preset
    cylinder_radius = cylinder_radius_property()
    cylinder_quality = cylinder_quality_property()
    cylinder_depth = cylinder_depth_property()
    cylinder_cup_fill_type = cylinder_cup_fill_type_property()

    # -----------------------------------------------------
    # Draw (create UI interface)
    # -----------------------------------------------------
    def draw(self, context):
        layout = self.layout
        space = bpy.context.space_data
        if not space.local_view:
            row = layout.row()
            row.prop(self, 'cylinder_quality')
            row = layout.row()
            row.prop(self, 'cylinder_radius')
            row = layout.row()
            row.prop(self, 'cylinder_depth')
            row = layout.row()
            row.prop(self, 'cylinder_cup_fill_type')
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
                create_cylinder(self, context)
                return {'FINISHED'}
            else:
                self.report({'WARNING'}, "ArchLab: Option only valid in global view mode")
                return {'CANCELLED'}
        else:
            self.report({'WARNING'}, "ArchLab: Option only valid in Object mode")
            return {'CANCELLED'}
