"Declare MUD entity handles for JPype->Java->JS(Rhino)"

# Current Issues with Design
# ---
#   1. Proxy Implementation:
#      o Entity handle/instance association with proxy object is bad.
#      o JPype weaknesses
#   2. Confusing and not robust!
#      o Why rely on Metaclass?
#      o Redundant CallableMethod instances
#      o Not scalable (complex sub-objects too complex, xxMutativeModulexx?)
#   3. Rhino deployment inconsistancies (name qualifications in different packages?)

from pdb import set_trace as debug
from datetime import datetime
from traceback import print_exc as traceback
import imp

# Basic Object.
class Object(object):
    # This could come from mud.runtime, no need for a new paradigm.

    # Why derive from __builtin__.object?
    #   metaprogramming in Entity type construction:
    #   "a new-style class can't have only classic bases"

    @classmethod
    def isSubInstance(self, inst):
        return issubclass(inst.__class__, self)

class Proxied(Object):
    # JPype::JProxy Implementation.
    INTERFACE = []

    # Instance Methods.
    def getProxy(self):
        try: return self._proxy
        except AttributeError:
            px = self._proxy = _getProxiedInstance(self, self.INTERFACE)
            return px

    proxy = property(getProxy)

def _getProxiedInstance(inst, intf):
    from person.services.jvm import getJavaVM, getJavaVMPackage
    assert getJavaVM().isJVMLoaded()
    return getJavaVMPackage('JProxy')(intf, inst = inst)

# Rhino.
class Scriptable(Proxied):
    #
    # ScriptableObject.defineClass is not an option, because it
    # requires access to a class with a nullary constructor.
    #
    # Since dynamic creation of classes with JPype is only possible
    # using java.lang.reflect.Proxy classes, the only constructor
    # available is the one with the InvocationHandler.
    #
    # This design offers proxied access to dynamic class-objects.
    #

    # XXX Not always in this package!
    INTERFACE = 'sun.org.mozilla.javascript.internal.Scriptable'

    '''
    [RhinoEngine]
    scriptable-interface = org.stuph.javascript.Scriptable

    '''

    try: from stuphos import getConfig
    except ImportError: pass
    else: INTERFACE = getConfig('scriptable-interface',
                                'RhinoEngine') or INTERFACE

class Callable(Proxied):
    INTERFACE = 'sun.org.mozilla.javascript.internal.Callable'

    try: from stuphos import getConfig
    except ImportError: pass
    else: INTERFACE = getConfig('callable-interface',
                                'RhinoEngine') or INTERFACE

# MUD Framework (Pattern)
class Entity(Scriptable):
    'Base class for defining scriptable entity handles.'
    # Could be renamed, since it represents pretty much any python object.

    # Entity Handle Model.
    def __init__(self, entity):
        self.entity = entity

        # Re-bind the method accessor to this specific instance,
        # because of get-call separation (see call method).
        for (k, v) in list(self.__class__.__dict__.items()):
            if Entity.CallableMethod.isSubInstance(v):
                setattr(self, k, v.rebind(self))

    @classmethod
    def Metaclass(self, name, bases, values):
        # Aggregates type accessors.
        members = {}
        for (k, v) in values.items():
            assert k not in ['entity', '_entity_members'] # Reserved.
            if Entity.PropertyAccessor.isSubInstance(v):
                # Convert get/put property accessor by attribute.
                p_name = v.name

                try: p = members[p_name]
                except KeyError:
                    members[p_name] = v
                else:
                    # Merge get/put properties.
                    if v.get: p.get = v.get
                    if v.put: p.put = v.put

            elif Entity.Member.isSubInstance(v):
                members[k] = v

        # Rewrite members-only!
        members['_entity_members'] = list(members.keys())
        return type(name, bases, members)

    class Member(Object):
        pass

    class Field(Member):
        def __init__(self, name, writable = False):
            self.name = name
            self.writable = writable

        def _get_(self, instance):
            return self.convertFrom(getattr(instance.entity, self.name))
        def _put_(self, instance, value):
            assert self.writable
            setattr(instance.entity, self.name, self.convertTo(value))

        @staticmethod
        def convert(value):
            return value

        convertFrom = convertTo = convert

    class BooleanField(Field):
        convertTo = convertFrom = convert = bool # builtin
    class IntegerField(Field):
        convertTo = convertFrom = convert = int # builtin
    class StringField(Field):
        convertTo = convertFrom = convert = str # builtin
    class ListField(Field):
        convertTo = convertFrom = convert = list # builtin XXX not directly compatible
    class DateField(Field):
        @staticmethod
        def convertFrom(value):
            return datetime.fromtimestamp(int(value)).ctime()
        @staticmethod
        def convertTo(value):
            raise NotImplementedError # strptime

    # Stored Meta Instances.
    class CallableMethod(Member, Callable):
        def __init__(self, function, handle = None):
            self.function = function
            self.handle = handle

        def rebind(self, handle):
            # Make a specific instance, storing entity handle for each instance.
            # (see call method)
            return self.__class__(self.function, handle = handle)

        def _get_(self, handle):
            return self.proxy

        # Rhino Callable Interface.
        def call(self, ctx, scope, this, params):
            # Todo: extract handle from 'this', so we don't store separate
            # instances for each entity handle.
            result = self.function(self.handle, *params)
            if Proxied.isSubInstance(result):
                return result.proxy

            return result

        def __repr__(self):
            return 'CallableMethod: %r' % self.function

    class PropertyAccessor(Member):
        @staticmethod
        def GetMaker(name):
            def makeGet(function):
                return Entity.PropertyAccessor(name, get = function)
            return makeGet

        @staticmethod
        def PutMaker(name):
            def makePut(function):
                return Entity.PropertyAccessor(name, put = function)
            return makePut

        def __init__(self, name, get = None, put = None):
            self.name = name
            self.get = get
            self.put = put

        def _get_(self, instance):
            if callable(self.get):
                return self.get(instance)
        def _put_(self, instance, value):
            if callable(self.put):
                return self.put(instance, value)

    # Subclass Objects.
    @staticmethod
    def Method(name):
        # Decorator.
        # Todo: propogate name into Metaclasser.
        return Entity.CallableMethod

    @staticmethod
    def Get(name):
        # Decorator.
        return Entity.PropertyAccessor.GetMaker(name)
    @staticmethod
    def Put(name):
        # Decorator.
        return Entity.PropertyAccessor.PutMaker(name)

    Property = Get

    # Rhino Scriptable Interface.
    def getClassName(self):
        # Mangling?
        return '%s.%s' % (self.__class__.__module__,
                          self.__class__.__name__)

    def get(self, name, param):
        # Unfold field property.
        member = getattr(self, name)
        if self.Member.isSubInstance(member):
            # debug()
            return member._get_(self)

        # Straight value or method.
        ##    if name in self._entity_members:
        ##        print member, '!'
        ##        return member

    def has(self, name, param):
        return name in self._entity_members
    def put(self, name, param, value):
        # XXX Will probably have to convert/validate.
        member = getattr(self, name)
        if self.Member.isSubInstance(member):
            # debug()
            return member._put_(self, value)

        # setattr(self.entity, name, value)
        pass
    def delete(self, name, param):
        # delattr(self.entity, name)
        pass

    def getPrototype(self):
        pass
    def setPrototype(self, proto):
        pass

    def getParentScope(self):
        pass
    def setParentScope(self, scope):
        pass

    def getIds(self):
        return list(self._entity_members)

    def getDefaultValue(self, clazz):
        pass

    def hasInstance(self, param):
        pass

    def toString(self):
        return '{%s (%s proxy): %r}' % (self.__class__.__name__,
                                        self.INTERFACE,
                                        self.entity)

    # Python Object Pleasantries.
    def __repr__(self):
        return self.toString()

class Peer(Entity, metaclass=Entity.Metaclass):
    'This handles the descriptor_data * on the mainDescriptorList.'

    # Fields.
    state     = Entity.StringField('state')
    host      = Entity.StringField('host')
    prompt    = Entity.StringField('prompt')
    hasPrompt = Entity.BooleanField('has_prompt')
    loginTime = Entity.DateField('login_time')

    # Properties.
    @Entity.Property('nextCommand')
    def getNextCommand(self):
        return self.entity.next_command()

    @Entity.Put('nextCommand')
    def putNextCommand(self, cmd):
        self.entity.input = str(cmd)

    @Entity.Put('output')
    def putOutput(self, msg):
        self.entity.write(str(msg))

    @Entity.Property('avatar')
    def getAvatar(self):
        try: return self.__avatar_proxy
        except AttributeError:
            av = self.entity.avatar
            if av is not None:
                av = self.__avatar = Mobile(av)
                av = self.__avatar_proxy = av.proxy

            return av

    @Entity.Property('networkMode')
    def getNetworkMode(self):
        # A complex data object (todo).
        pass

    # Methods.
    @Entity.Method('editString')
    def editString(self, string = '', message_handler = None):
        self.entity.string_edit(str(string))
        ##    if callable(message_handler):
        ##        self.entity.messenger = message_handler

    @Entity.Method('pageString')
    def pageString(self, string):
        self.entity.page_string(str(string))

    @Entity.Method('sendLine')
    def sendLine(self, msg):
        self.entity.sendln(msg)

    @Entity.Method('textOut')
    def textOut(self, msg):
        self.entity.write(msg)

    ##    # Prototype Methods?
    ##    @Entity.Method('toString')
    ##    def js_toString(self): # XXX wrong
    ##        return repr(self) # .entity)

    ##    @Entity.Method('toString')
    ##    def toString(self): # XXX wrong
    ##        return repr(self) # .entity)

    ##    bandwidth_in            bandwidth_out           color_mode
    ##    connected               state                   desc_num
    ##    descriptor              email                   has_prompt
    ##    host                    ip                      login_time
    ##    remort                  saved                   clear_output
    ##    dequeue_input_block     editString              string_edit
    ##    next_command            page_string             sendln
    ##    textout                 write                   avatar
    ##    echo                    fileno                  networkMode
    ##    olc{mob,obj}            original                prompt
    ##    socket                  state                   valid
    ##
    ##    withdraw (removes avatar and goes into Internal)
    ##    input (next command, or, force input)
    ##    input_queue (all input; non-destructive)

class Mobile(Entity, metaclass=Entity.Metaclass):
    armorClass  = Entity.IntegerField('armorClass')
    hitroll     = Entity.IntegerField('hitroll')
    damroll     = Entity.IntegerField('damroll')
    experience  = Entity.IntegerField('experience')
    fatigue     = Entity.IntegerField('fatigue')
    max_fatigue = Entity.IntegerField('max_fatigue')
    hit         = Entity.IntegerField('hit')
    max_hit     = Entity.IntegerField('max_hit')
    mana        = Entity.IntegerField('mana')
    max_mana    = Entity.IntegerField('max_mana')
    height      = Entity.IntegerField('height')
    weight      = Entity.IntegerField('weight')
    idnum       = Entity.IntegerField('idnum')
    level       = Entity.IntegerField('level')
    power       = Entity.IntegerField('power')
    vnum        = Entity.IntegerField('vnum')

    description = Entity.StringField('description')
    name        = Entity.StringField('name')
    email       = Entity.StringField('email')
    specialName = Entity.StringField('specialName')
    passwd      = Entity.StringField('passwd')
    position    = Entity.StringField('position')

    god      = Entity.BooleanField('god')
    hasMail  = Entity.BooleanField('hasMail')
    immortal = Entity.BooleanField('immortal')
    supreme  = Entity.BooleanField('supreme')
    npc      = Entity.BooleanField('npc')
    mortal   = Entity.BooleanField('mortal')
    writing  = Entity.BooleanField('writing')

    trusted  = Entity.ListField('trusted')
    mail     = Entity.ListField('mail')

    @Entity.Property('peer')
    def getPeer(self):
        try: return self.__peer_proxy
        except AttributeError:
            p = self.entity.peer
            if p is not None:
                p = self.__peer = Peer(p)
                p = self.__peer_proxy = p.proxy

            return p

    @Entity.Property('room')
    def getRoom(self):
        try: return self.__room_proxy
        except AttributeError:
            room = self.entity.room
            if room is not None:
                room = self.__room = Room(room)
                room = self.__room_proxy = room.proxy

            return room

    @Entity.Property('fighting')
    def getFighting(self):
        try: return self.__fighting_proxy
        except AttributeError:
            fighting = self.entity.fighting
            if fighting is not None:
                fighting = self.__fighting = Mobile(fighting)
                fighting = self.__fighting_proxy = fighting.proxy

            return fighting

    @Entity.Method('save')
    def save(self):
        self.entity.save()

    @Entity.Method('find')
    def find(self, *args, **kwd):
        self.entity.find(*args, **kwd)

    @Entity.Method('perform')
    def perform(self, *args, **kwd):
        self.entity.perform(*args, **kwd)

    @Entity.Method('equip')
    def equip(self, *args, **kwd):
        self.entity.equip(*args, **kwd)

    @Entity.Method('unequip')
    def unequip(self, *args, **kwd):
        self.entity.unequip(*args, **kwd)

    @Entity.Method('rent')
    def rent(self):
        self.entity.rent()

    @Entity.Method('unrent')
    def unrent(self):
        self.entity.unrent()

    # playerstore

    ##    aff_charisma        aff_constitution    aff_dexterity       aff_intelligence    
    ##    aff_strength        aff_wisdom          affectflags         aff_strength_addition
    ##    affections          affectvector        afk_message         alias               
    ##    alignment           arena               armor               attack              
    ##    attackModeOrder     attack_type         breath              canSee              
    ##    carry_items         carry_weight        changeHandle        charisma            
    ##    checkAutoassist     check_subdue        clan                clanrank            
    ##    cmdlock             colorset            commands            constitution        
    ##    damnodice           damroll             damsizedice         deathCry            
    ##    deaths              default_pos         description         destructor          
    ##    dexterity           die                 do_auto_exits       dts                 
    ##    eq_apply_ac         equipment           findchar            finditem            
    ##    findplayer          followers           get_thac0           gold_in_bank        
    ##    gold_on_hand        handle              heldby              holding             
    ##    hometown            incur_damage        instantiate         intelligence        
    ##    invalid_item_align  inventory           killAlignmentChange last_dir            
    ##    load                login_time          long_descr          make_corpse         
    ##    master              members             middleName          mount               
    ##    mountedby           move                new                 next                
    ##    nickname            npcflags            npckills            nr                  
    ##    page_length         perform_attack      pfilepos            plan                
    ##    playerflags         plrkills            power_rating        preferences         
    ##    preferences2        prename             prototype           py_handle           
    ##    qpoints             race                rawKill             read_mobile         
    ##    remort              sameAs              save_player_file    save_room           
    ##    sever_limb          sex                 short_descr         special             
    ##    stop_hunting        strength            strength_addition   syslogLevel         
    ##    timer               title               track_timer         tracking            
    ##    trusted             update_position     valid               visibleBy           
    ##    visibleToLevel      waitState           walk_type           was_in_room         
    ##    wearing             wisdom              wizinvis_level      wizname

class Item(Entity, metaclass=Entity.Metaclass):
    pass

    ##    antiClass           anticlass           antiflags           armorclass          
    ##    biodegradable       carrier             carrying            charges             
    ##    container           container_type      contents            damage              
    ##    detailed_descriptionexdesc              exdescs             extraflags          
    ##    extrakeys           flags               getextra            gold_value          
    ##    key_vnum            keywords            light_hours         liquid_type         
    ##    load                location            lock_type           max_charges         
    ##    move                name                new                 nutrition           
    ##    poisonous           portal_level_range  prototype           rnum                
    ##    room                roomRoot            room_description    root_location       
    ##    setextra            show                showModifiers       special             
    ##    specialName         spell               spell1              spell2              
    ##    spell3              spell_level         spells              store               
    ##    terminus            type                vnum                volume              
    ##    weapon_type         wearer              wearflags           

class Room(Entity, metaclass=Entity.Metaclass):
    pass

    ##    contents            description         down                east                
    ##    exdesc              exdescs             exits               extrakeys           
    ##    flags               getextra            hometown            house               
    ##    keys                light               listMobiles         members             
    ##    name                north               people              sector              
    ##    setextra            south               spawnMoney          special             
    ##    track               trackdir            up                  vnum                
    ##    west                zone

class Zone(Entity, metaclass=Entity.Metaclass):
    pass

    ##    commands            destroy             empty               flags               
    ##    items               loadFromFile        mobiles             name                
    ##    reset               rooms               save                unlink              
    ##    unload              vnum                zcommands

# System Access Modules
class Module(Entity):
    def _install_module_entities(self, handle, module):
        handle.entity = module
        handle._entity_members = em = []

        for name in dir(module):
            member = getattr(module, name)
            if callable(member):
                if name not in ['entity', '_entity_members']:
                    em.append(name)
                    setattr(handle, name, Entity.CallableMethod(member, handle = handle))

    # Todo: Offer Entity.__metaclass__ configuration.

    def __init__(self, module):
        self._install_module_entities(self, module)

class MutativeModule(Module):
    def getIds(self):
        # Todo: provide dynamic lookup of (dir) members.
        return list(self._entity_members)

_mud_module = None
def buildMudModule():
    global _mud_module
    if _mud_module is None:
        from . import mudaccess
        _mud_module = Module(mudaccess)

    return _mud_module.proxy

# Test Harness.
try: from stuphmud.server.player import ACMD
except ImportError: pass
else:
    @ACMD('test-ent*ities')
    def doTestEntities(peer, cmd, argstr):
        from person.services.jvm.rhino import handles
        return imp.reload(handles).doTest(peer, cmd, argstr)

    def doTest(peer, cmd, argstr):
        from person.services.jvm.rhino import getRhinoEngine
        js = getRhinoEngine()

        px = Peer(peer)
        js.put('peer', px.proxy)

        doTestWith((peer, cmd, argstr), (px, js))
        return True

    def doTestWith(xxx_todo_changeme, xxx_todo_changeme1):
        (peer, cmd, argstr) = xxx_todo_changeme
        (px, js) = xxx_todo_changeme1
        print('\x1b[H\x1b[J')

        print('Original object:')
        print('   ', px)
        print('Original type:')
        print('   ', type(px))
        print('   ', px.__class__)
        print(dir(px))
        print()

        print('Original proxy:')
        print('   ', px.proxy)
        print('   ', px.proxy._proxy)
        print('Original type:')
        print('   ', type(px.proxy))
        print(dir(px.proxy))
        print()

        rx = js.get('peer')
        print('Proxied object:')
        print('   ', rx)
        print('   ', rx.__javaobject__)
        print('Proxied type:')
        print('   ', type(rx)) # is x.__class__
        print('   ', rx.__javaclass__)
        print(dir(rx))
        print()

        ##    print 'Proxy Class:'
        ##    print '   ', rx.getProxyClass(type(rx).__javaobject__)
        ##    print

        print('Invocation Handler:')
        print('   ', rx.h)
        print(dir(rx.h))
        print()

        import __main__ as main
        main.px = px
        main.rx = rx
        main.js = js

    TEST_SCRIPT = \
    '''
    peer;
    // peer.pageString(peer.toString());
    // peer.pageString(peer.avatar.toString());
    '''

    def doTestWith(xxx_todo_changeme2, xxx_todo_changeme3):
        (peer, cmd, argstr) = xxx_todo_changeme2
        (px, js) = xxx_todo_changeme3
        from stuphos import enqueueHeartbeatTask as enqueue
        enqueue(js.eval, TEST_SCRIPT)

def consoleTest(options, args):
    class X:
        def __init__(self):
            self.aValue = 0
        def aMethod(self):
            pass

        def __repr__(self):
            return '<X>'

    h = Peer(X())
    print(h)
    print(h.getIds())
 
def main(argv = None):
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-g', '--debug', action = 'store_true')
    (options, args) = parser.parse_args(argv)

    try: import jpype
    except ImportError:
        print('JPype not available, simulating...')
        class _JProxy:
            def __init__(self, inst, intf):
                self.instance = inst
                self.interface = intf

        # Not actually called until property is accessed.
        global _getProxiedInstance
        _getProxiedInstance = _JProxy

    if options.debug:
        from pdb import runcall
        runcall(consoleTest, options, args)
    else:
        consoleTest(options, args)

if __name__ == '__main__':
    main()
