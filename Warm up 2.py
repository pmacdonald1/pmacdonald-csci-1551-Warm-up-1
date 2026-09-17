#imports everything needed to run the code
import math, sys, random
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #disables the mouse control and moves the camera to a birds eye view
        base.disableMouse()
        base.camera.setPos(0.0, 0.0, 250.0)
        base.camera.setHpr(0.0, -90.0, 0.0)

        #loads the model for our fighter and makes the color red
        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)

        #lets the user close the program by pressing the escape key
        self.accept('escape', self.quit)

        #loads the cube models
        self.parent = self.loader.loadModel("./Assets/cube")

        #defines x and starts angles at 0
        x = 0

        #duplicates the cube 100 times
        for i in range(100):
            theta = x

            #positions the cube to place them
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            self.placeholder2.setPos(50.0 * math.cos(theta), 50.0 * math.sin(theta), 0.0 * math.tan(theta))

            #lets the colors apear in a random color
            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() * 0.4
            blue = 0.6 + random.random() * 0.4
            self.placeholder2.setColorScale(red, green, blue, 1.0)

            #places the cube
            self.parent.instanceTo(self.placeholder2)

            #changes the angle slightly so the next cube can be placed
            x = x + 0.06

        #all of the left, right, up, down movements that the player can do
        self.accept('arrow_left', self.left, [1])
        self.accept('arrow_right', self.right, [1])
        self.accept('arrow_up', self.up, [1])
        self.accept('arrow_down', self.down, [1])

        #helps stop the movement by detecting when the action has stoped
        self.accept('arrow_left-up', self.left, [0])
        self.accept('arrow_right-up', self.right, [0])
        self.accept('arrow_up-up', self.up, [0])
        self.accept('arrow_down-up', self.down, [0])

    #defines how the quit out will happen
    def quit(self):
        sys.exit()

    #defines all of the left, right, up, down movements
    def left(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveLeft, 'moveLeft')
        else:
            self.taskMgr.remove('moveLeft')

    def right(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveRight, 'moveRight')
        else:
            self.taskMgr.remove('moveRight')

    def up(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveUp, 'moveUp')
        else:
            self.taskMgr.remove('moveUp')

    def down(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveDown, 'moveDown')
        else:
            self.taskMgr.remove('moveDown')

    # #defines the movements of the actions the player can do
    def moveLeft(self, task):
        self.fighter.setX(self.fighter, -1)
        return task.cont

    def moveRight(self, task):
        self.fighter.setX(self.fighter, 1)
        return task.cont

    def moveUp(self, task):
        self.fighter.setY(self.fighter, 1)
        return task.cont

    def moveDown(self, task):
        self.fighter.setY(self.fighter, -1)
        return task.cont

app = MyApp()
app.run()