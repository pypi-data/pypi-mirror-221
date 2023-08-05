# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:54:41 2023

@author: Emil
"""

import numpy as np
from numpy.typing import ArrayLike
from numbers import Number
from collections.abc import Sequence, Iterable

from .operator_sum import OpSum


HAM_PAR = Number | ArrayLike

def build_ham_op_sum_S_D(epsilon_d: HAM_PAR,
                         U: HAM_PAR,
                         Gamma: HAM_PAR,
                         Delta: HAM_PAR,
                         gamma: Sequence[float],
                         xi: Sequence[float]) -> OpSum:
    '''
    Generate the operator sum (OpSum) for the Hamiltonian of an S-D junction -
    a surrogate model superconducting (SC) lead tunnel-coupled to a quantum dot
    (QD).
    
    The number of levels in the surrogate lead is the length of 'gamma' and
    'xi'. Note that 'gamma' and 'xi' must have the same length.
    
    The QD is placed at site=0, while the levels of the SC lead are at
    site=1, 2, 3, ..., L.

    Parameters
    ----------
    epsilon_d : HAM_PAR
        QD energy level.
    U : HAM_PAR
        QD charging energy.
    Gamma : HAM_PAR
        Tunneling rate between QD and SC lead.
    Delta : HAM_PAR
        SC gap (order parameter) of the lead.
    gamma : Sequence[float]
        Surrogate model coupling strengths for each effective level.
    xi : Sequence[float]
        Surrogate model energy level position for each effective level.

    Returns
    -------
    h_os : OpSum
        Operator sum for the Hamiltonian of the surrogate model S-D junction.

    '''
    h_os = OpSum()
    add_dot_to_ham_op_sum(h_os, epsilon_d, U, site_dot=0)
    add_sc_to_ham_op_sum(h_os, Gamma, Delta, gamma, xi,
                         sites_sc=range(1, len(xi) + 1), site_dot=0)
    return h_os

def build_ham_op_sum_SN_D(epsilon_d: HAM_PAR,
                          U: HAM_PAR,
                          Gammas: Sequence[HAM_PAR],
                          Deltas: Sequence[HAM_PAR],
                          gamma: Sequence[float],
                          xi: Sequence[float]) -> OpSum:
    '''
    Generate the operator sum (OpSum) for the Hamiltonian of an S_N-D junction -
    N surrogate model superconducting (SC) leads tunnel-coupled to a quantum
    dot (QD). The N leads only couple to the QD - not to each other, directly.
    
    The number of levels in the surrogate leads is the length of 'gamma' and
    'xi'. Note that 'gamma' and 'xi' must have the same length and all N leads
    are identical (same 'gamma' and 'xi' for all N leads).
    
    The QD is placed at site=0, while the levels of the first SC lead are at
    site=1, 2, 3, ..., L, the second lead at site=L+1, L+2, ..., 2*L, and so on.

    Parameters
    ----------
    epsilon_d : HAM_PAR
        QD energy level.
    U : HAM_PAR
        QD charging energy.
    Gammas : Sequence[HAM_PAR]
        Tunneling rate between QD and SC lead i=1, 2, ..., N.
    Deltas : Sequence[HAM_PAR]
        SC gap (order parameter) of lead i=1, 2, ..., N.
    gamma : Sequence[float]
        Surrogate model coupling strengths for each effective level.
    xi : Sequence[float]
        Surrogate model energy level position for each effective level.
    
    Raises
    ------
    ValueError
        'Gammas' and 'Deltas' must have the same length (equal to the number
        of superconductors, N).

    Returns
    -------
    h_os : OpSum
        Operator sum for the Hamiltonian of the surrogate model S_N-D junction.

    '''
    h_os = OpSum()
    add_dot_to_ham_op_sum(h_os, epsilon_d, U, site_dot=0)
    
    if len(Gammas) != len(Deltas):
        raise ValueError("'Gammas' and 'Deltas' must have the same length "
                         "(equal to the number of superconductors).")
    L = len(xi)
    for i, (Gamma, Delta) in enumerate(zip(Gammas, Deltas)):
        add_sc_to_ham_op_sum(h_os, Gamma, Delta, gamma, xi,
                             sites_sc=range(1 + i * L, 1 + (i + 1) * L),
                             site_dot=0)
    return h_os

def add_dot_to_ham_op_sum(h_os: OpSum, epsilon_d: HAM_PAR, U: HAM_PAR,
                          site_dot: int) -> OpSum:
    '''
    Add a quantum dot (QD) to the Hamiltonian operator sum (OpSum) at 'site_dot'.

    Parameters
    ----------
    h_os : OpSum
        Hamiltonian operator sum. This is modified in-place.
    epsilon_d : HAM_PAR
        QD energy level.
    U : HAM_PAR
        QD charging energy.
    site_dot : int
        Site of the QD.

    Returns
    -------
    OpSum
        'h_os' with the QD terms appended.

    '''
    h_os += (epsilon_d, "ntot", site_dot)
    h_os += (U, "nup_ndn", (site_dot, site_dot))
    return h_os
    
def add_sc_to_ham_op_sum(h_os: OpSum, Gamma: HAM_PAR, Delta: HAM_PAR,
                         gamma: Sequence[float], xi: Sequence[float],
                         sites_sc: Iterable[int], site_dot: int) -> OpSum:
    '''
    Add a superconducting (SC) lead at 'sites_sc' to the Hamiltonian operator
    sum (OpSum) that is tunnel-coupled to the quantum dot (QD) at 'site_dot'.

    Parameters
    ----------
    h_os : OpSum
        Hamiltonian operator sum. This is modified in-place.
    Gamma : HAM_PAR
        Tunneling rate between QD and SC lead.
    Delta : HAM_PAR
        SC gap (order parameter) of the lead.
    gamma : Sequence[float]
        Surrogate model coupling strengths for each effective level.
    xi : Sequence[float]
        Surrogate model energy level position for each effective level.
    sites_sc : Iterable[int]
        Sites of the SC lead.
    site_dot : int
        Site of the QD.

    Raises
    ------
    ValueError
        There must be the same number of parameters for the superconductor, i.e.
        'gamma' and 'xi' must have the same length (equal to the number of
        desired levels, L, in the superconductor).

    Returns
    -------
    OpSum
        'h_os' with the QD terms appended.

    '''
    if len(gamma) != len(xi):
        raise ValueError("There must be the same number of parameters for the "
                         "superconductor, i.e. 'gamma' and 'xi' must have the "
                         "same length (equal to the number of desired levels "
                         "in the superconductor).")
        
    for site_sc, xi_l, gamma_l in zip(sites_sc, xi, gamma):
        h_os += (-Delta, "cdagup_cdagdn", (site_sc, site_sc))
        h_os += (-Delta.conjugate(), "cdn_cup", (site_sc, site_sc))
        
        h_os += (xi_l, "ntot", site_sc)
        
        t = np.sqrt(gamma_l * Gamma)
        h_os += (t, "cdagup_cup", (site_sc, site_dot))
        h_os += (t, "cdagdn_cdn", (site_sc, site_dot))
        h_os += (t, "cdagup_cup", (site_dot, site_sc))
        h_os += (t, "cdagdn_cdn", (site_dot, site_sc))
    
    return h_os
