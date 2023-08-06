# Initialize Engine Proper.
from person.services.jvm import getJavaVMPackage
import imp

RHINO_INIT = '''
function dir(o) { var r = []; for (n in o) { r[r.length] = n; } return r; }
function dirs(o) { return dir(o).join(', '); }
'''

RHINO_ENGINE_OBJECT = 'JVM::RhinoEngine'

def createRhinoEngine():
    rhino = getJavaVMPackage('javax').script \
            .ScriptEngineManager()           \
            .getEngineByName('JavaScript')

    rhino.eval(RHINO_INIT)
    return rhino

def getRhinoEngine():
    from stuphos.runtime.registry import getObject
    return getObject(RHINO_ENGINE_OBJECT,
                     create = createRhinoEngine)

# Components.
from .handles import *

class RhinoPlayerModule:
    # Do Java-Script things based on player.
    def __init__(self, engine):
        self.engine = engine
    def setupEnvironment(self, **kwd):
        for (key, value) in kwd.items():
            self.engine.put(key, value)

    # MUD Events.
    def enterGame(self, peer, player):
        pass

    # Telnet Dispatch.
    def evaluate(self, player, script, *params):
        # Compile and execute script.
        pass
    def invoke(self, player, script, *params):
        # Locate stored script and execute.
        pass

    # Command.
    def doEvaluate(self, player, script):
        # Compile and execute script.

        # Todo: Cache these.
        actor = Mobile(player).proxy
        peer = player.peer
        if peer is not None:
            peer = Peer(peer).proxy

        self.setupEnvironment(player = actor,
                              actor = actor,
                              me = actor,
                              peer = peer,
                              mud = buildMudModule())

        # Todo: process javax.script.ScriptException

        try: result = self.engine.eval(script)
        except getJavaVMPackage('JavaException') as e:
            print(e.stacktrace(), file=player.peer)
        else:
            if player.peer and result is not None:
                toString = getattr(result, 'toString', None)
                if callable(toString):
                    print(toString(), file=player.peer)
                else:
                    print(repr(result), file=player.peer)

# Shared Instance.
RHINO_PLAYER_MODULE_OBJECT = 'JVM::Rhino::PlayerModule'

def getRhinoPlayerModule(player):
    from stuphos.runtime.registry import getObject
    return getObject(RHINO_PLAYER_MODULE_OBJECT,
                     create = lambda:RhinoPlayerModule(getRhinoEngine()))

# MUD Instrumentation.
class Instrument:
    def onEnterGame(self, ctlr, peer, player):
        rhinoModule = getRhinoPlayerModule(player)
        rhinoModule.enterGame(peer, player)

def installRhinoController():
    from stuphos.runtime import Component
    class RhinoController(Instrument, Component):
        pass

    # This should be configured in mud.config.
    from stuphmud.server.player.telnet.dispatch import getDefaultDispatchModule
    telnetDispatch = getDefaultDispatchModule()
    # XXX remove previous incarnation.
    telnetDispatch.addModule('javascript', RhinoDispatchModule)

    from stuphmud.server.player import ACMD
    for cmd in ['javas*cript', '#', '%']:
        installCommand = ACMD(cmd)
        installCommand(doJavascript)

class RhinoDispatchModule:
    @classmethod
    def getDispatchAction(self, name):
        if name in ['eval', 'invoke']:
            return self(name)

    def __init__(self, name):
        self.name = name
    def __call__(self, peer, script, *params):
        rhinoModule = getRhinoPlayerModule(peer.avatar)
        if rhinoModule:
            action = getattr(rhinoModule, self.name, None)
            if callable(action):
                return action(peer, script, *params)

def doJavascript(peer, cmd, argstr):
    if argstr == ' reload':
        from stuphos.runtime.registry import delObject
        from person.services.jvm import rhino

        rhino = imp.reload(rhino)
        delObject(rhino.RHINO_PLAYER_MODULE_OBJECT)
        rhino.installRhinoController()

        print('RELOADED [%s]' % rhino.__name__.upper())

    elif argstr == ' program':
        # Messenger.
        pass

    elif argstr:
        rhinoModule = getRhinoPlayerModule(peer.avatar)
        if rhinoModule:
            rhinoModule.doEvaluate(peer.avatar, argstr.lstrip())

    return True

# Test crap.
##    def examine(**kwd):
##        from code import InteractiveConsole as IC
##        import readline
##        IC(locals = kwd).interact(banner = '')
##
##    def test():
##        js = getRhinoEngine()
##        js.put('s', SDict())
##
##        try:
##            js.eval('s.x = "y"')
##            print js.eval('dirs(s)')
##
##        except getJavaVM()['JavaException'], ex:
##            print ex.stacktrace()
##            examine(js = js, ex = ex, jpype = getJavaVM().importJPype())

# Old.
##    def getRepositoryModule():
##        import sys
##        return sys

##    def getRhinoEngine():
##        try: return getattr(getRepositoryModule(), RHINO_ENGINE_OBJECT)
##        except AttributeError:
##            js = createRhinoEngine()
##            setattr(getRepositoryModule(), RHINO_ENGINE_OBJECT, js)
##
##            js.eval(RHINO_INIT)
##            return js
