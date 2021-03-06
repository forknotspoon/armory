import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class MaterialNode(Node, ArmLogicTreeNode):
    '''Material node'''
    bl_idname = 'LNMaterialNode'
    bl_label = 'Material'
    bl_icon = 'GAME'

    property0 = StringProperty(name='', default='')
    
    def init(self, context):
        self.outputs.new('NodeSocketShader', 'Material')

    def draw_buttons(self, context, layout):
        layout.prop_search(self, 'property0', bpy.data, 'materials', icon='NONE', text='')

add_node(MaterialNode, category='Variable')
