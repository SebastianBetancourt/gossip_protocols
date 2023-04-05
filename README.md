# Gossip Protocols

Prototype implementation of the gossip protocols model proposed in [1] as part of the PROMUEVA seminar of 03/13/2023 where the paper [2] was discussed.

- Gossip graph specification through the `networkx` API, that includes several ways of graph generation, including digraphs, random graphs, and others.
- Protocol specification through the propositional language proposed in [2], with atomic formulas like "is familiar with" or "is an expert"
- Interface to implement schedulers and run simulations
- All the power from the `networkx` library, including drawing functions and other tools from network science.

## Setup

Run `pip install networkx` before anything. See the `showcase.ipynb` file for some examples.

## References
[1] Apt, K. R., Grossi, D., & van der Hoek, W. (2016). Epistemic Protocols for Distributed Gossiping. Electronic Proceedings in Theoretical Computer Science, 215, 51–66. doi:10.4204/eptcs.215.5

[2] Livesey, J., & Wojtczak, D. (7 2022). Propositional Gossip Protocols under Fair Schedulers. In L. D. Raedt (Ed.), Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence, IJCAI-22 (pp. 391–397). doi:10.24963/ijcai.2022/56
