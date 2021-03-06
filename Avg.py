from calvin.actor.actor import Actor, condition, guard, ActionResult
from calvin.runtime.north.calvin_token import ExceptionToken

class Avg(Actor):

    """
    Divides input on port 'dividend' with input on port 'divisor'
    Inputs :
        temm1 :
        temm2 :
        temm3 :
    Output :
        op:
    """

    def init(self):
        pass

    @condition(action_input=['temm1','temm2','temm3'], action_output=['op'])
    def avg(self, temperature1, temperature2, temperature3):
        if(temperature1 != 'ignore' and temperature2 !='ignore' and temperature3!='ignore'):
            self.result = (temperature1+temperature2+temperature3)/ 3
        else:
            self.result = 'ignore'
        return ActionResult(production=([self.result, 'validate'],))

    action_priority = (avg,)
