"""
    Inverse kinematics robot arm controller

    Process:
    Set end effector to target
    Back out endpoints of segments

    Set base point to base location
    Back out endpoints of effectors

    Check threshold
    """


import math
target = (2, 5)
positions = [(1, 2), (2, 5), (3, 5), (4, 7)]
distances = [2, 1, 4]


def calc_new_position(pi, li, t=True):
    print(t)
    if(t):
        # No target provided
        print("Target NOT provided")
    else:
        # Target provided
        print("Target provided")
    pass


def calc_distance(cord_a, cord_b):
    delta_x = cord_b[0] - cord_a[0]
    delta_y = cord_b[1] - cord_a[1]
    dist = math.sqrt((delta_x**2) + (delta_y**2))
    return dist


def FABRIK(positions, distances, target, tolerance):
    new_positions = []
    # The distance between the root and the target
    dist = calc_distance(target, positions[0])
    # Check whether the target is within reach
    total_arm_reach = sum(distances)
    if(dist > total_arm_reach):
        print("Target is unreachable")
        for i in range(0, len(positions)-1):
            # Find the distance ri between the target t and the joint position pi
            ri = calc_distance(positions[i], target)
            di = distances[i]
            li = di / ri
            # Find new joint positions
            new_positions.append(calc_new_position(positions[i], li, target))
    else:
        # Target is reachable
        # Set b as the initial position of the joint p0
        b = positions[0]
        # Check whether the distance between end effector and target is greater than the tolerance
        dist_end = calc_distance(positions[-1], target)
        while(dist_end > tolerance):
            # Stage 1: FOWARD REACHING
            # Set end effector as target
            positions[-1] = target
            for i in range(len(positions) - 1):
                # Find the distance ri between new joint and next joint
                print(positions[i], positions[i+1])
                ri = calc_distance(positions[i], positions[i+1])
                di = distances[i]
                li = di / ri
                # Find new positions
                new_positions.append(calc_new_position(1, 2))
            # STAGE 2: BACKWARD REACHING
            # Set the root p0 as initial position (base)
            positions[0] = b
            for i in range(len(positions) - 1):
                pass

            print("New dist: ", calc_distance(positions[-1], target))
            dist_end -= .1

    return new_positions


# FABRIK(positions, distances, target, .1)

calc_new_position(1, 2, 5)

print(bool(0))
