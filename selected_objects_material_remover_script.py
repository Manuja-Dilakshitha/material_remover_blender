import bpy

objects = bpy.context.selected_objects


for obj in objects:
    obj.active_material_index = 0
    
    for i in range(len(obj.material_slots)):
        bpy.ops.object.material_slot_remove({'object' : obj})