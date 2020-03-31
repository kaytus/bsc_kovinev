import math

from QPanda3D.Helpers.Env_Grid_Maker import *
from QPanda3D.Panda3DWorld import Panda3DWorld

from benchmark.panda3dwidget.CameraController import CameraController


class ModelView(Panda3DWorld):
    def __init__(self, path_model):
        Panda3DWorld.__init__(self)
        self.disable_mouse()

        self.camera_controller_ = CameraController(self, 600, math.radians(45), math.radians(60))

        self.set_collisions_handlers()
        self.set_light()
        self.draw_model(path_model)
        self.draw_grid()

        self.setFrameRateMeter(True)
        self.setSceneGraphAnalyzerMeter(True)

    @property
    def camera_controller(self):
        return self.camera_controller_

    def set_collisions_handlers(self):
        # Collision traverser
        self.cTrav = CollisionTraverser("collisionTraverser")

        # Collision handlers
        self.carCollisionHandler = CollisionHandlerEvent()
        self.carCollisionHandler.addInPattern("%fn-into-%in")

    def set_light(self):
        # Lights
        dlight = DirectionalLight("dlight")
        dlnp = self.render.attachNewNode(dlight)
        dlnp.setHpr(180.0, -70.0, 0)
        self.render.setLight(dlnp)

        alight = AmbientLight("alight")
        alnp = self.render.attachNewNode(alight)
        alight.setColor(VBase4(0.4, 0.4, 0.4, 1))
        self.render.setLight(alnp)

    def draw_model(self, path_model):
        self.model = self.loader.loadModel(path_model)
        self.model.setPos(0, 0, 0)
        #self.model.setLightOff()
        self.model.reparentTo(self.render)

    def draw_grid(self):
        self.grid_maker = Env_Grid_Maker()
        self.grid = self.grid_maker.create()
        self.grid.reparentTo(self.render)
        self.grid.setLightOff()

    def get_scene_graph_analyzer_meter(self):
        return self.sceneGraphAnalyzerMeter