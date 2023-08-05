# FermPy
A Python package for exactly solving low-dimensional fermionic Hamiltonians. It was developed with the intention of constructing and diagonalizing matrix representations of low-dimensional, interacting fermionic Hamiltonians, in particular effective (surrogate) models that describe the low-energy (sub-gap) physics of the superconducting Anderson impurity model (see the [arXiv preprint](https://arxiv.org/abs/2307.11646)).

FermPy is based on [NumPy](https://numpy.org/) and [SciPy](https://scipy.org/). Small systems use *dense* NumPy arrays as operator representations while large systems employ *sparse* SciPy arrays.

Functionality of this package includes:
- Construction of matrix representations of operators ($H, S_z$, etc.) from a basis (chosen from symmetry considerations)
- Diagonalization (*numpy.linalg.eigh*, *scipy.sparse.linalg.eigh*) of operators
- Calculation of expectation values and thermal averages of operators

## Installation
FermPy is found on [PyPI](https://pypi.org/project/fermpy/) and easily installed by running
```
pip install fermpy
```
from the command-line.

## Usage
As an example of the intended usage of FermPy, we calculate and plot the excitation spectrum and average spin on a quantum dot (QD), coupled to a superconducting (SC) lead which is described by an effective three-level discretization (see the [arXiv preprint](https://arxiv.org/abs/2307.11646) for more details).

<br />
Import the necessary packages.

```
import numpy as np
import matplotlib.pyplot as plt

from fermpy.operator_sum import OpSum
from fermpy.hamiltonian_constructors import build_ham_op_sum_S_D
from fermpy.operator_representation import OpRep, operator_exp_val
from fermpy.bases import BasisS2
```

Construct the operator sum for the Hamiltonian $H$ of an SC-QD junction with an effective three-level lead. The effective couplings `gamma` and level positions `xi` are collected in Table 1 of the Supplemental Material of [arXiv preprint](https://arxiv.org/abs/2307.11646). Everything is in units of the SC gap `Delta`.
```
Gamma = np.linspace(0, 10, 201)
h_os = build_ham_op_sum_S_D(epsilon_d=-7.5,
                            U=15,
                            Gamma=Gamma,
                            Delta=1,
                            gamma=[0.5080, 1.8454, 1.8454],
                            xi=[0, 2.7546, -2.7546])
```

Define the basis. Here, we choose the eigenstates of total spin $S^2$ (the Hamiltonian preserves spin rotational symmetry).
```
basis = BasisS2(1 + 3) # One quantum dot level + three lead levels
```

Build the matrix representation of the Hamiltonian from the operator sum `h_os` and `basis`. We only consider the singlet, doublet, and triplet states ($s = 0, 1/2, 1$) - the quantum numbers of $S^2$: $S^2 |s\rangle = s(s+1)|s\rangle$.
```
h_op = OpRep(h_os, basis, qns_to_consider=(0, 1, 2)) # quantum numbers: 2*s
```

Diagonalize $H$, giving the eigenenergies and eigenvectors. `energies` and `eigenvectors` are dictionaries with quantum numbers as keys ($2s = 0, 1, 2$) and NumPy arrays as values.
```
energies: dict[int, np.ndarray]
eigenvectors: dict[int, np.ndarray]
energies, eigenvectors = h_op.diagonalize_all_qns(return_eigenvectors=True)
```

Extract the ground state quantum number and energy.
```
s_gs = np.argmin([E[:, 0] for E in energies.values()], axis=0)
E_gs = np.array([energies[s][idx, 0] for idx, s in enumerate(s_gs)])
```

Calculate the z-projection of spin on the quantum dot in the ground state. The syntax of `OpSum` is similar to [ITensor](https://itensor.org/).
```
sz_op = OpRep(opsum=OpSum([('sz', 0)]), basis=basis)
sz_exp = operator_exp_val(op_rep=sz_op, state_rep=eigenvectors, axis=1)
sz_exp_gs = [sz_exp[s][idx, 0] for idx, s in enumerate(s_gs)]
```

Plot the excitation spectrum and average dot spin in the ground state.
```
fig, (ax_top, ax_bot) = plt.subplots(2, 1,
                                     figsize=(5.5, 5.5),
                                     sharex=True,
                                     constrained_layout=True
                                     )

ax_top.set(ylabel=r'$(E - E_\mathrm{GS}) / \Delta$',
           xlim=(0, 10),
           ylim=(-0.05, 2)
          )
ax_bot.set(xlabel=r'$\Gamma / \Delta$',
           ylabel=r'$\langle S_{z, \mathrm{dot}} \rangle$',
           xlim=(0, 10),
           ylim=(-0.05, 0.55)
          )

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
              labels=range(3),
              loc='upper right',
              title='s'
             )
ax_bot.plot(Gamma, sz_exp_gs)
```

Here's the output figure.

<p align="center">
  <img src="https://github.com/emilfrost/fermpy/blob/cd4825a47f1b91a25fe757eaf379343602534296/example.png" width="500" />
</p>

