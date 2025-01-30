# The class CarSimulator is a simple 2D vehicle simulator.
# The vehicle states are:
# - x: is the position on the x axis on a xy plane
# - y: is the position on the y axis on a xy plane
# - v is the vehicle speed in the direction of travel of the vehicle
# - theta: is the angle wrt the x axis (0 rad means the vehicle
#   is parallel to the x axis, in the positive direction;
#   pi/2 rad means the vehicle is parallel
#   to the y axis, in the positive direction)
# - NOTE: all units are SI: meters (m) for distances, seconds (s) for
#   time, radians (rad) for angles...
#
# (1)
# Write the method "simulatorStep", which should update
# the vehicle states, given 3 inputs:
#  - a: commanded vehicle acceleration
#  - wheel_angle: steering angle, measured at the wheels;
#    0 rad means that the wheels are "straight" wrt the vehicle.
#    A positive value means that the vehicle is turning counterclockwise
#  - dt: duration of time after which we want to provide
#    a state update (time step)
#
# (2)
# Complete the function "main". This function should run the following simulation:
# - The vehicle starts at 0 m/s
# - The vehicle drives on a straight line and accelerates from 0 m/s to 10 m/s
#   at a constant rate of 0.4 m/s^2, then it proceeds at constant speed.
# - Once reached the speed of 10 m/s, the vehicle drives in a clockwise circle of
#   roughly 100 m radius
# - the simulation ends at 100 s
#
# (3)
# - plot the vehicle's trajectory on the xy plane
# - plot the longitudinal and lateral accelerations over time

import numpy as np
import matplotlib.pyplot as plt

class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        self.wheelbase = wheelbase  # Distance between front and rear wheels
        self.x = 0  # Initial x position
        self.y = 0  # Initial y position
        self.v = v0  # Initial speed
        self.theta = theta0  # Initial heading angle

    def simulatorStep(self, a, wheel_angle, dt):
        # Update the speed
        self.v += a * dt
        
        # Update the heading angle
        self.theta += (self.v / self.wheelbase) * np.tan(wheel_angle) * dt
        
        # Update position
        self.x += self.v * np.cos(self.theta) * dt
        self.y += self.v * np.sin(self.theta) * dt

def main():
    wheelbase = 4  # Wheelbase of 4 meters
    v0 = 0  # Initial speed (m/s)
    theta0 = 0  # Initial angle (rad)
    
    simulator = CarSimulator(wheelbase, v0, theta0)
    
    dt = 0.1  # Time step (s)
    time = np.arange(0, 100, dt)  # Time array from 0 to 100 seconds
    x_positions = []
    y_positions = []
    accelerations = []
    
    # Phase 1: Accelerate from 0 m/s to 10 m/s
    for t in time:
        if simulator.v < 10:  # Accelerate to 10 m/s
            a = 0.4  # Constant acceleration (m/s^2)
            wheel_angle = 0  # Going straight
        else:
            a = 0  # No acceleration at constant speed
            wheel_angle = np.deg2rad(30)  # Turning right

        simulator.simulatorStep(a, wheel_angle, dt)

        # Store positions
        x_positions.append(simulator.x)
        y_positions.append(simulator.y)
        accelerations.append(a)
    
    # Convert the trajectory lists to numpy arrays for plotting
    x_positions = np.array(x_positions)
    y_positions = np.array(y_positions)

    # Plotting the trajectory on the xy plane
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(x_positions, y_positions)
    plt.title("Vehicle Trajectory")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.axis('equal')

    # Plotting the accelerations over time
    plt.subplot(1, 2, 2)
    plt.plot(time[:len(accelerations)], accelerations)
    plt.title("Longitudinal Acceleration Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s²)")
    
    plt.tight_layout()
    plt.show()

main()