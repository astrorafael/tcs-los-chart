# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# Copyright (c) 2021
#
# See the LICENSE file for details
# see the AUTHORS file for authors
# ----------------------------------------------------------------------

#--------------------
# System wide imports
# -------------------

import logging

# ---------------------
# Thrid-party libraries
# ---------------------

import numpy as np
import matplotlib.pyplot as plt

from lica.cli import execute


# ------------------------
# Own modules and packages
# ------------------------

from ._version import __version__

# -----------------------
# Module global variables
# -----------------------

log = logging.getLogger(__name__)

# -----------------
# Matplotlib styles
# -----------------

# Load global style sheets
plt.style.use("tcs.resources.global")

# ------------------
# Auxiliary fnctions
# ------------------

def plot_grid(axes, x0, x1, xd, z0, z1, zd, xlabel, ylabel):
    axes.grid(True,  which='major', color='black', linestyle='solid')
    #axes.grid(True,  which='minor', color='black', linestyle=(0, (1, 10)))
    axes.grid(True,  which='minor', color='black', linestyle=":")
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    # Major gridline
    axes.set_xticks(np.arange(x0, x1+1, xd))
    axes.set_yticks(np.arange(z0, z1+1, zd))
    # Minor gridline
    axes.set_xticks(np.arange(x0, x1+1, 1), minor=True)
    axes.set_yticks(np.arange(z0, z1+1, zd//2), minor=True)

    axes.set_xlim([x0, x1])
    axes.set_ylim([z0, z1])
    axes.minorticks_on()


# ------------------------
# AUXILIARY MAIN FUNCTIONS
# ------------------------


def grid(args):
    fig, axes = plt.subplots()
    log.info(axes)
    fig.suptitle(args.title)
    plot_grid(
        axes   = axes,
        x0     = args.from_hex,
        x1     = args.to_hex,
        xd     = args.x_delta,
        z0     = args.hmin,
        z1     = args.hmax, 
        zd     = args.z_delta,
        xlabel = "Distance (hexes)", 
        ylabel = "Elevation (meters)",   
    )
    plt.show()


# ===================================
# MAIN ENTRY POINT SPECIFIC ARGUMENTS
# ===================================

def add_args(parser):

    # -----------------------------
    # TCS Line of Sight Grid parser
    # -----------------------------

    parser.add_argument('-x0','--from', dest="from_hex", type=int, default=0, help='Starting distance [hexes] (default %(default)d)')
    parser.add_argument('-x1', '--to', dest="to_hex", type=int, default=20, help='Ending hex distance [hexes] (default %(default)d)')
    parser.add_argument('-xd', '--x-delta', type=int, default=5, help='Grid line every \u039Bx hexes (default %(default)d)')
    parser.add_argument('-z0', '--hmin', type=int, default=0, help='Starting elevation [meters] (default %(default)d)')
    parser.add_argument('-z1', '--hmax', type=int, default=30, help='Ending elevation [meters] (default %(default)d)')
    parser.add_argument('-zd', '--z-delta', type=int, default=10, help='Grid line every \u039Bz meters (default %(default)d)')
    parser.add_argument('-t','--title', type=str, default ="TCS Line of Sight Grid", help='Chart title (default "%(default)s")')
   
# ================
# MAIN ENTRY POINT
# ================

def main():
    execute(main_func=grid, 
        add_args_func=add_args, 
        name=__name__, 
        version=__version__,
        description="TCS Line of Sight Grid"
    )