from vpython import *
import matplotlib as plt

# some basic vectors to use later
x_hat = vector(1,0,0)
y_hat = vector(0,1,0)
z_hat = vector(0,0,1)
origin = vector(0,0,0)
t = 0 # time
dt = 0.01 # time difference per loop
# for demonstration purposes: omega is chosen to be big but it does not affect the wobble:spin ratio
# the implementation is done for a small omega wihch can be neglected
omega = pi/2 # first Euler angle of the system
v = pi/2 # angular velocity of the system
wobble = [] # list for wobbling data
spin = [] # list for spin data

# camera configuration
def set_camera():
    scene.camera.pos = 2*y_hat
    scene.camera.axis = -scene.camera.pos

def create_arrows():
    body_arrow = arrow(color=vector(0,0,1), axis=vector(1.2,0,0), pos=origin, shaftwidth=0.02) # body arrow
    arrow_body_axis_z = arrow(color=vector(0,1,0), axis=vector(0,0,0.01)*(100/cos(omega*dt)), pos=origin, shaftwidth=0.02) # z-axis arrow
    arrow_ang_momentum = arrow(color=vector(1,0,0), axis=vector(0,0,1), pos=origin, shaftwidth=0.02) # angular velocity arrow
    return body_arrow, arrow_body_axis_z, arrow_ang_momentum

def main():
    global t
    set_camera()

    plate = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.01), radius=1) # creating the plate
    plate.texture = 'ku.png' # a custom picture texture for the plate
    body_arrow, arrow_body_axis_z, arrow_ang_momentum = create_arrows() # creating the arrows

    plate.rotate(angle=pi/36, axis=y_hat) # rotating the plate 
    body_arrow.rotate(angle=pi/36, axis=y_hat) # rotating the body arrow to match initial position of the plate
    arrow_body_axis_z.rotate(angle=pi/36, axis=y_hat) # rotating the z-axis arrow to match initial position of the plate

    oscillation = graph(xtitle='time', ytitle= 'x-coordinate') # creating the graph
    # giving labels to the curves
    f1 = gcurve(color=color.green, label = 'x-coor of z body axis') 
    f2 = gcurve(color=color.blue, label = 'x-coor of a point on the plane')
    while(True):
        rate(100) # number of loops per second

        # the rotations of arrows and the plate
        plate.rotate(angle=v*dt, axis=vector(0,0,0.01))
        body_arrow.rotate(angle=v*dt, axis=vector(0,0,0.01))
        arrow_body_axis_z.rotate(angle=2*v*dt, axis=vector(0,0,0.01))

        # collecting data for dynamic plotting
        # since it freezes the computer,
        # dynamic plotting is stopped when t hits 10
        if t<10:
            # defining the curves again, otherwise the drawing messes up
            f1 = gcurve(color=color.green)
            f2 = gcurve(color=color.blue)
            # x-coordinate of the arrow head, this demostrates the x-coor of a point on the plate
            spin.append([t,plate.axis.x*100])
            # x-coordinate of z body axis arrow head
            wobble.append([t,arrow_body_axis_z.axis.x])
            t = t + dt # increment the time
            f1.plot(wobble) # plot
            f2.plot(spin) # plot
    

if __name__ == '__main__':
    main()