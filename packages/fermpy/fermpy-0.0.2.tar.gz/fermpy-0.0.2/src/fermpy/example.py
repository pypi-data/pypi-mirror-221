# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 23:25:19 2023

@author: Emil
"""

import numpy as np
import matplotlib.pyplot as plt

from operator_sum import OpSum
from hamiltonian_constructors import build_ham_op_sum_S_D
from operator_representation import OpRep, operator_exp_val
from bases import BasisS2

# Hamiltonian for an S-D junction with an effective three-level lead
Gamma = np.linspace(0, 10, 201)
h_os = build_ham_op_sum_S_D(epsilon_d=-7.5,
                            U=15,
                            Gamma=Gamma,
                            Delta=1,
                            gamma=[0.5080, 1.8454, 1.8454],
                            xi=[0, 2.7546, -2.7546])

# Basis of eigenstates of total spin S^2 (the Hamiltonian preserves spin
# rotational symmetry)
basis = BasisS2(4) # One quantum dot level + three lead levels

# Build the matrix representation of the Hamiltonian in the basis for s=0,1,2 
# - the quantum numbers of S^2: S^2|n> = s(s+1)|n>
h_op = OpRep(h_os, basis, qns_to_consider=(0, 1, 2))

# Diagonalize the Hamiltonian, giving the eigenenergies and eigenvectors.
# These are dictionaries with quantum numbers as keys (s=0,1,2) and
# corresponding energies as values.
energies, eigenvectors = h_op.diagonalize_all_qns(return_eigenvectors=True)

# Ground state quantum number and ground state energy
s_gs = np.argmin([E[:, 0] for E in energies.values()], axis=0)
E_gs = np.array([energies[s][idx, 0] for idx, s in enumerate(s_gs)])

# z-projection of spin on the quantum dot in the ground state
sz_op = OpRep(opsum=OpSum([('sz', 0)]), basis=basis)
sz_exp = operator_exp_val(op_rep=sz_op, state_rep=eigenvectors, axis=1)
sz_exp_gs = [sz_exp[s][idx, 0] for idx, s in enumerate(s_gs)]

# Plotting the excitation spectrum and average dot spin in the ground state
fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(5.5, 5.5), sharex=True,
                                     constrained_layout=True)

ax_top.set(ylabel=r'$(E - E_\mathrm{GS}) / \Delta$',
           xlim=(0, 10),
           ylim=(-0.05, 2))
ax_bot.set(xlabel=r'$\Gamma / \Delta$',
           ylabel=r'$\langle S_{z, \mathrm{dot}} \rangle$',
           xlim=(0, 10),
           ylim=(-0.05, 0.55))

ax_top.hlines(1, 0, 10, linestyle='dashed', color='k', linewidth=0.5)
ax_bot.hlines(0, 0, 10, linestyle='dashed', color='k', linewidth=0.5)

colors = {0: 'tab:blue', 1: 'tab:orange', 2: 'tab:green'}
lines_to_label = []
for s, energies_s in energies.items():
    lines_to_label.append(ax_top.plot(Gamma,
                                      energies_s - E_gs[:, None],
                                      color=colors[s])[0]
                          )
ax_top.legend(handles=lines_to_label,
              labels=[0, '1/2', 1],
              loc='upper right',
              title='s')
ax_bot.plot(Gamma, sz_exp_gs)

# fig.savefig('example.png', dpi=150)