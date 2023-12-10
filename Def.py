import time

class Character:
    def __init__(self, characname, atk, core, energy, core_max, energy_max):
        self.characname = characname
        self.atk = atk
        self.core = core
        self.energy = energy
        self.core_max = core_max
        self.energy_max = energy_max
        self.actnum = 0
        self.air = False
        self.controls = []
        self.skills = []
        self.actions = []

    def clamp(self,num,a,b):
        # Ensure core and energy do not exceed their maximum values
        return max(min(num, max(a, b)), min(a, b))

    def action_append(self, action):
        # Add an action to the character's action list
        self.actions.append(action)

    def execute_actions(self):
        # Execute all actions in the character's action list
        for action in self.actions:
            action.func(self)

# Define the Skill class with condic and func methods according to provided logic
class Skill(Character):
    def __init__(self, character, skillname, rate, actcount, skillcount, skillduratime):
        super().__init__(character.characname, character.atk, character.core, character.core2, character.core3,
                         character.energy, character.core_max, character.energy_max)
        self.skillname = skillname
        self.rate = rate
        self.actcount = actcount
        self.skillcount = float('inf') if skillcount == 'infinite' else skillcount
        self.skillduratime = convert_time_to_seconds(skillduratime)
        self.skillstartime = convert_time_to_seconds('0:00')
        self.skillendtime = convert_time_to_seconds('0:00')

    def condic(self):
        # Custom condition logic for the skill
        pass

    def func(self):
        # Custom function logic for the skill
        pass

# Define the Control class with a custom func method
class Control(Character):
    def __init__(self, character, controlname, contduratime):
        super().__init__(character.characname, character.atk, character.core, character.core2, character.core3,
                         character.energy, character.core_max, character.energy_max)
        self.controlname = controlname
        self.contduratime = convert_time_to_seconds(contduratime)
        self.contstartime = convert_time_to_seconds('0:00')
        self.contendtime = convert_time_to_seconds('0:00')

    def func(self, contduratime):
        # Custom function logic for the control
        pass


# Define the instance of Character named Qiming according to the provided details
qiming = Character(characname="Qiming", atk=2000, core=0, core2=0, core3=0, energy=0, core_max=3, energy_max=100)


# Instantiate the skills for Qiming
qiming_match3 = Skill(qiming, "match3", 5.4, 0, 5, '0:02')
qiming_pushold = Skill(qiming, "pushold", 4.2, 0, 'infinite', '0:02')
qiming_arcant1 = Skill(qiming, "arcant1", 12.0, 0, 'infinite', '0:04')
qiming_arcant2 = Skill(qiming, "arcant2", 6.0, 0, 'infinite', '0:01')

# Instantiate the control for Qiming
qiming_dash = Control(qiming, "Qiming_dash", '0:01')

# Output the instance and its actions to check if they're defined correctly
print(vars(qiming))
print(vars(qiming_match3))
print(vars(qiming_pushold))
print(vars(qiming_arcant1))
print(vars(qiming_arcant2))
print(vars(qiming_dash))
