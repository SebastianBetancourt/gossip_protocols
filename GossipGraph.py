import networkx as nx

class GossipGraph(nx.Graph):

    def __init__(self, incoming_graph_data=None, **attr):
        super().__init__(incoming_graph_data, **attr)
        self.gossip_situation = {n: {n.__str__().upper()} for n in self}
        self.protocol = {n: [] for n in self}

    def reset(self):
        self.gossip_situation = {n: {n.__str__().upper()} for n in self}

    def draw(self):
        labels_with_secrets = {n: s.__str__() + "\n" + n for n, s in self.gossip_situation.items()}
        nx.draw_spectral(self, labels=labels_with_secrets, verticalalignment="baseline")

    def make_call(self, caller, callee):
        # push-pull call
        if not nx.is_path(self, [caller, callee]):
            raise Exception("caller and callee are not neighbors")
        
        self.gossip_situation[caller].update(self.gossip_situation[callee])
        self.gossip_situation[callee].update(self.gossip_situation[caller])
    
    def is_familiar_with(self, a, S):
        return S in self.gossip_situation[a]

    def is_expert(self, a):
        return len(self.gossip_situation[a]) == len(self)

    def add_rule(self, agent, guard, call):
        self.protocol[agent].append({"guard": guard, "call": call})

class GossipDigraph(nx.DiGraph, GossipGraph):

    def __init__(self, incoming_graph_data=None, **attr):
        nx.DiGraph.__init__(self, incoming_graph_data, **attr)
        self.gossip_situation = {n: {n.__str__().upper()} for n in self}
        self.protocol = {n: [] for n in self}
