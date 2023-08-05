from transitions import Machine, State
import re

class hgcal_state_machine:
    def __init__(self,model):
        steady_states = [
            'initial',
            'halted',
            'configured',
            'running',
            'paused'
        ]
        transient_states  = [
            State(name = 'initializing' , on_enter='on_initialize'), 
            State(name = 'configuring'  , on_enter='on_configure'),
            State(name = 'starting'     , on_enter='on_start'),
            State(name = 'pausing'      , on_enter='on_pause'),
            State(name = 'resuming'     , on_enter='on_resume'),
            State(name = 'stopping'     , on_enter='on_stop'),
            State(name = 'reconfiguring', on_enter='on_reconfigure'),
            State(name = 'halting'      , on_enter='on_halt'),
            State(name = 'resetting'    , on_enter='on_reset'),
            State(name = 'ending'       , on_enter='on_end')
        ]
        states = steady_states + transient_states
        self.machine = Machine(model=model, states=states,initial='initial')
        self.machine.add_transition('initialize',  source='initial'   , dest='initializing' , after='to_halted')
        self.machine.add_transition('configure',   source='halted'    , dest='configuring'  , after='to_configured')
        self.machine.add_transition('start',       source='configured', dest='starting'     , after='to_running')
        self.machine.add_transition('pause',       source='running'   , dest='pausing'      , after='to_paused')
        self.machine.add_transition('resume',      source='paused'    , dest='resuming'     , after='to_running')
        self.machine.add_transition('stop',        source='running'   , dest='stopping'     , after='to_configured')
        self.machine.add_transition('stop',        source='paused'    , dest='stopping'     , after='to_configured')
        self.machine.add_transition('reconfigure', source='configured', dest='reconfiguring', after='to_configured')
        self.machine.add_transition('halt',        source='configured', dest='halting'      , after='to_halted')
        self.machine.add_transition('reset',       source='halted'    , dest='resetting'    , after='to_initial')
        self.machine.add_transition('end',         source='initial'   , dest='ending')

class dummy_hgcal(object):
    def on_initialize(self,cfg:dict) : print(f"call back initialize {cfg}")
    def on_configure(self,cfg:dict)  : print("call back configure")
    def on_start(self,cfg:dict)      : print("call back start")
    def on_pause(self,cfg:dict)      : print("call back pause")
    def on_resume(self,cfg:dict)     : print("call back resume")
    def on_stop(self,cfg:dict)       : print("call back stop")
    def on_reconfigure(self,cfg:dict): print("call back reconfigure")
    def on_halt(self,cfg:dict)       : print("call back halt")
    def on_reset(self,cfg:dict)      : print("call back reset")
    def on_end(self,cfg:dict)        : print("call back end")

if __name__ == "__main__":
    hgcal_handler = dummy_hgcal()
    sc_machine = hgcal_state_machine(hgcal_handler)
    # help(sc_machine.machine)
    cfg = {'utc':10}
    print(hgcal_handler.state)
    # allowed_events = sc_machine.machine.get_triggers(hgcal_handler.state)
    # pattern = re.compile( 'to_*' )
    # allowed_events = [ event for event in allowed_events if not pattern.match(event) ]
    # print( allowed_events )
    hgcal_handler.initialize(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.configure(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.start(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.pause(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.resume(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.stop(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.halt(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.reset(cfg=cfg)
    print(hgcal_handler.state)
    hgcal_handler.end(cfg=cfg)
