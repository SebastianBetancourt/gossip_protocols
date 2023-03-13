from itertools import cycle
import random

class Scheduler:
    def agent_fair_choose(self, g):
        is_any_active = False

        initial_counter = self.fairness_counter
        while not is_any_active:
            if(self.fairness_counter >= len(g.protocol)):
                self.fairness_counter = 0
            is_any_active = False

            for i, v in enumerate(g):
                if i is self.fairness_counter:
                   agent = v
            agent_protocol = g.protocol[agent]
            
            for r in agent_protocol:
                if r["guard"](g):
                    is_any_active = True
                    break
            if is_any_active:
                break
            
            self.fairness_counter += 1
            if self.fairness_counter == initial_counter:
                    return

        for rule in agent_protocol:
            if rule["guard"](g):
                break
        
        self.fairness_counter += 1
        return rule
    
    def rule_fair_choose(self, g):
        all_rules = [r for a in g.protocol.values() for r in a]
        initial_counter = self.fairness_counter
        if self.fairness_counter >= len(all_rules):
            self.fairness_counter = 0
            
        while not all_rules[self.fairness_counter]["guard"](g):
            self.fairness_counter += 1
            if self.fairness_counter >= len(all_rules):
                self.fairness_counter = 0
            if self.fairness_counter == initial_counter:
                return
        self.fairness_counter += 1
        return all_rules[self.fairness_counter - 1]

    def first_agent_first_rule_choose(self, g):
        for agent in cycle(g):
            for rule in g.protocol[agent]:
                if rule["guard"](g):
                    return rule
    

    def __init__(self, choice_fn=agent_fair_choose):
        self.choice_fn = choice_fn
        self.fairness_counter = 0

    def run(self, g, n=100):
        for i in range(n):
            call_to_make = self.choice_fn(self, g)
            if call_to_make is None:
                break
            g.make_call(call_to_make["call"][0], call_to_make["call"][1])
