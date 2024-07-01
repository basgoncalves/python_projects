import numpy as np




# full / PD
ap_ratio = 97/176
ml_ratio = 58/157
v_ratio = 12/49

ap_ratio2 = 256/768
ml_ratio2 = 774/785
v_ratio2 = 80/250

print('ap_ratio:', ap_ratio)
print('ml_ratio:', ml_ratio)
print('v_ratio:', v_ratio)

# Assuming your point coordinates are stored in NumPy arrays
point_A_norm = np.array([-218, 130, 53])
point_B_norm = np.array([225, 126, 53])

# Calculate the transformation vector
transformation_vector = point_B_norm - point_A_norm

point_A_dis = np.array([3, 124, -0.01])
point_B_dis = np.array([257, 124, 0.6])

# Apply transformation to DIS points
point_A_converted = point_A_dis + transformation_vector
point_B_converted = point_B_dis + transformation_vector

scaling_factor = np.linalg.norm(point_A_converted - point_B_converted) / np.linalg.norm(point_A_norm - point_B_norm)

scaled_point_A_dis = point_A_dis / scaling_factor
scaled_point_B_dis = point_B_dis / scaling_factor

print('point_A_converted:', point_A_converted)
print('point_B_converted:', point_B_converted)

print('Distance DIS:', np.linalg.norm(point_A_dis - point_B_dis))
print('Distance NORM:', np.linalg.norm(point_A_norm - point_B_norm))
print('Distance CONV:', np.linalg.norm(point_A_converted - point_B_converted))
print('Scaling factor:', scaling_factor)
print('Distance scaled DIS:', np.linalg.norm(scaled_point_A_dis - scaled_point_B_dis))


print('point_A_converted:', point_A_converted)
print('point_B_converted:', point_B_converted)
print('point_A_Norm:', point_A_norm)
print('point_B_Norm:', point_B_norm)

exit()

full_HJC = np.array([82.48,	126.9,	30.8])
full_GT = np.array([52.1,	149.8,	40.9])
full_LC = np.array([-77.4,	-245.9,	-0.5])

# calculate difference between full_HJC and full_GT
distance = np.linalg.norm(full_LC - full_GT)
print('distance full:' , distance)


PD_HJC = np.array([78.84546921853715,	3.2008812601033867,	-13.742165630039107])
PD_GT = np.array([125.70271401673622,	34.65580310508881,	-54.47454710372199,])

# calculate difference between PD_HJC and PD_GT
distance = np.linalg.norm(PD_HJC - PD_GT)
print('distance PD:' , distance)



