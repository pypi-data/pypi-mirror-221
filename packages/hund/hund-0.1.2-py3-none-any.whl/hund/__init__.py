#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright notice
# ----------------
#
# Copyright (C) 2013-2023 Daniel Jung
# Contact: proggy-contact@mailbox.org
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
#
"""Implement a function that applies Hund's rules to a given electronic
(atomic) configuration.
"""

"""
To do:
--> calculate termsymbol of ions
--> return the name of the element that belongs to the given ground state
    electronic configuration
"""

__version__ = '0.1.2'

import numpy

class DummyDecorator(object):
    """Dummy decorator. Returns the passed function unchanged.
    """
    def __init__(self, *args, **kwargs):
        pass
    def __call__(self, func, *args, **kwargs):
        return func

try:
    from frog import Frog
except ImportError:
    Frog = DummyDecorator

# symbols for the orbital quantum number l
orbletters = 'spdfghiklmnoqrtuv'

optdoc = dict(nice='show nice string representation of the term symbol',
              latex='show Latex representation of the term symbol',
              S='return spin angular momentum',
              m='return spin multiplicity',
              L='return orbital angular momentum',
              J='return total angular momentum',
              P='return parity', all_output='return all information')

@Frog(usage='%prog [options] CONF', optdoc=optdoc)
def hund(conf, nice=False, latex=False, S=False, m=False, L=False, J=False,
         P=False, all_output=False):
    """Apply Hund's rules to determine the term symbol of the ground state of a
    given electronic (atomic) configuration.

    Default output is the short string representation (one line) of the term
    symbol. For alternative output, set one of the switches to True:
    nice       : nice string representation of the term symbol (multiline)
    latex      : Latex representation of the term symbol
    S          : spin angular momentum
    m          : spin multiplicity
    L          : orbital angular momentum
    J          : total angular momentum
    P          : parity
    all_output : return dictionary containing all information

    Note:
    The Hund's rules are just rules, not laws. For example: For Gadolinium
    (Gd, Z=64) this function finds the ground state term symbol 9D4o, which
    should actually be 9D2o (Gadolinium has the ground state electron
    configuration "[Xe] 4f7 5d1 6s2").
    """
    # former hund._Hund (2011-09-14 until 2011-11-15)
    # former tb._Hund from 2011-02-03

    Jt, Lt, St, Pt = 0., 0, 0., 1  # total values
    for word in conf.split():
        conflist = sepnumstr(word)
        if not len(conflist) in (2, 3) or len(conflist[1]) != 1 \
                or isinstance(conflist[0], str) \
                or not isinstance(conflist[1], str):
            raise ValueError('bad electron configuration: %s' % word)

        if len(conflist) < 3:
            conflist.append(1)
        n, letter, enum = conflist
        l = orbletters.index(letter)
        if l >= n:
            raise ValueError('bad electron configuration: %s. ' % word +
                             'Orbital angular momentum l must be smaller ' +
                             'than the principal quantum number n')
        if enum < 0:
            raise ValueError('bad electron configuration: %s. ' % word +
                             'Number of electrons in term symbol must be ' +
                             'non-negative integer')
        fullnum = 2*(2*l+1)  # number of electrons the orbital can hold
        if enum > fullnum:
            raise ValueError('bad electron configuration: %s. ' % word +
                             'Too many electrons for orbital %i%s' % (n,
                                                                      letter))

        # fill orbitals according to Hund's rules
        states = numpy.array([1]*enum+[0]*(fullnum-enum), dtype=bool)
        states = numpy.reshape(states, (2, 2*l+1)).T[::-1]
        mlmat = numpy.array([numpy.arange(-l, l+1), numpy.arange(-l, l+1)]).T

        # calculate spin, orbital und total angular momentums of this shell
        Ss = (numpy.sum(states[:, 0])-numpy.sum(states[:, 1]))/2.
        Ls = int(numpy.sum(states*mlmat))
        Js = abs(L-Ss) if enum < fullnum/2 else Ls+Ss
        Ps = (-1)**(numpy.sum(states)*l)

        # add/multiply values of this orbital to the total values
        St += Ss
        Lt += Ls
        Jt += Js
        Pt *= Ps

    S2 = int(2*St+1)  # spin multiplicity

    # make string representations
    Lchar = orbletters[Lt].upper()
    # Sstr = str(int(St)) if St == int(St) else str(int(2*St))+'/2'
    # Lstr = str(int(Lt)) if Lt == int(Lt) else str(int(2*Lt))+'/2'
    Jstr = str(int(Jt)) if Jt == int(Jt) else str(int(2*Jt))+'/2'
    Pstr = '' if Pt == 1 else 'o'  # even or odd parity
    S2str = str(int(S2)) if S2 == int(S2) else str(int(2*S2))+'/2'
    termsymb = S2str+Lchar+Jstr+Pstr
    niceterm = S2str+' '*len(Lchar)+Pstr+'\n'  # nice string representation
    niceterm += ' '*len(S2str)+Lchar+'\n'
    niceterm += ' '*(len(S2str)+len(Lchar))+Jstr
    latexterm = r'${}^{%s} %s_{%s}^{%s}$' % (S2str, Lchar, Jstr, Pstr)

    # return results
    if nice:
        return niceterm
    elif latex:
        return strLatex(latexterm)
    elif S:
        return St
    elif m:
        return S2
    elif L:
        return Lt
    elif J:
        return Jt
    elif P:
        return Pt
    elif all_output:
        return dict(S=St, L=Lt, J=Jt, P=Pt, termsymb=termsymb,
                    niceterm=niceterm, latexterm=latexterm)
    else:
        return termsymb


#===========================#
# Miscellaneous definitions #
#===========================#


class strLatex(str):
    """String with display method, for pretty printing in IPython using
    Latex.
    """
    def _repr_latex_(self):
        return self


def sepnumstr(string):
    """Separate numeric values from characters within a string. Return
    resulting numeric values and strings as a list.

    Example:
    >>> sepnumstr('abc12defg345')
    ['abc', 12, 'defg', 345]
    """
    # former tb.sepnumstr from 2011-02-03 until 2011-04-06

    if not isinstance(string, str):
        raise TypeError('string expected')

    # if string is empty, just return empty list
    if string == '':
        return []

    numchars = '-0123456789.'  # characters that belong to a numeric value
    result = []
    currval = ''  # current value
    currisnum = string[0] in numchars  # if current value is numeric
    for char in string:
        if (char in numchars) == currisnum:
            currval += char
        else:
            if currisnum:
                if currval == '.':
                    result.append(0.)
                elif '.' in currval:
                    result.append(float(currval))
                else:
                    result.append(int(currval))
            else:
                result.append(currval)
            currval = char
            currisnum = not currisnum

    # add last value
    if currisnum:
        if currval == '.':
            result.append(0.)
        elif '.' in currval:
            result.append(float(currval))
        else:
            result.append(int(currval))
    else:
        result.append(currval)

    # return result
    return result
