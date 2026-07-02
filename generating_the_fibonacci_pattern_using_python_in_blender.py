
def get_3d_cordinates(i, value_to_assign):
    value_to_assign= value_to_assign/1000000
    if int(i/2)%2==1 or (i/2)==0:
        value_to_assign*=-1
    result= [0,0,0]
    if i%2:
        result[2]= value_to_assign
    else:
        result[1]=value_to_assign
    return result


current_fibonaci_sequence=1;
last_fibonaci_sequence=1;
bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":get_3d_cordinates(2, current_fibonaci_sequence), "orient_type":'NORMAL', "orient_matrix":((-0.934449, 0.348907, 0.0711997), (-0.348642, -0.93711, 0.0165308), (0.0724897, -0.00937602, 0.997325)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":True, "use_accurate":False, "use_automerge_and_split":False, "translate_origin":False})




i=2 #TURNS OUT SIGN DOES NOT MATTER BECAUSE DIVISION(THE % IN  get_3d_cordinates) IS BLIND TO SIGN
while i>-100:
    i=i-1
    bpy.ops.mesh.extrude_context_move(MESH_OT_extrude_context={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":get_3d_cordinates(i, current_fibonaci_sequence), "orient_type":'NORMAL', "orient_matrix":((-0.934449, 0.348907, 0.0711997), (-0.348642, -0.93711, 0.0165308), (0.0724897, -0.00937602, 0.997325)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":True, "use_accurate":False, "use_automerge_and_split":False, "translate_origin":False})
    temp= current_fibonaci_sequence
    current_fibonaci_sequence= current_fibonaci_sequence+last_fibonaci_sequence
    last_fibonaci_sequence= temp


