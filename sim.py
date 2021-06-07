from vpython import *
import matplotlib as plt

x_hat = vector(1,0,0)
y_hat = vector(0,1,0)
z_hat = vector(0,0,1)
origin = vector(0,0,0)
t = 0
dt = 0.01
omega = pi/2
wobble = []
spin = []

def set_camera():
    scene.camera.pos = 2*y_hat
    scene.camera.axis = -scene.camera.pos


def main():
    global t
    set_camera()
    plate = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.01), radius=1)
    plate.texture = 'ku.png'
    body_arrow = arrow(color=vector(0,0,1), axis=vector(1.2,0,0), pos=origin, shaftwidth=0.02)
    arrow_body_axis_z = arrow(color=vector(0,1,0), axis=vector(0,0,0.01)*(100/cos(omega*dt)), pos=origin, shaftwidth=0.02)
    body_arrow.rotate(angle=pi/36, axis=y_hat)
    arrow_body_axis_z.rotate(angle=pi/36, axis=y_hat)
    plate.rotate(angle=pi/36, axis=y_hat)
    arrow_ang_momentum = arrow(color=vector(1,0,0), axis=vector(0,0,1), pos=origin, shaftwidth=0.02)
    while(True):
        rate(100)
        plate.rotate(angle=omega*dt, axis=vector(0,0,0.01))
        body_arrow.rotate(angle=omega*dt, axis=vector(0,0,0.01))
        arrow_body_axis_z.rotate(angle=2*omega*dt, axis=vector(0,0,0.01))
        if t<10:
            spin.append([t,plate.axis.x*100])
            wobble.append([t,arrow_body_axis_z.axis.x])
            t = t + dt
            f1 = gcurve(color=color.green)
            f2 = gcurve(color=color.blue)
            f1.plot(wobble)
            f2.plot(spin)
    

if __name__ == '__main__':
    main()