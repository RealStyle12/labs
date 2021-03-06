#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""Actualizeaza unidirectional un alt director conform celui dat."""

from __future__ import print_function
import os
from sys import argv
from shutil import copyfile


def unidirectional(loc1, loc2):
    """Recursiv creeaza fisiere conform director modificabil."""
    if os.path.exists(loc1):
        for fisier in os.listdir(loc1):
            fisier_actual_1 = os.path.join(loc1, fisier)
            fisier_actual_2 = os.path.join(loc2, fisier)
            if (os.path.exists(fisier_actual_1) and
                    os.path.isdir(fisier_actual_1)):
                if not os.path.exists(fisier_actual_2):
                    os.mkdir(fisier_actual_2)
                unidirectional(fisier_actual_1, fisier_actual_2)
            else:
                if not os.path.exists(fisier_actual_2):
                    copyfile(fisier_actual_1, fisier_actual_2)


def rm_files(loc1, loc2):
    """Recursiv sterge fisierele in plus din director actualizat automat."""
    if os.path.exists(loc2):
        for fisier in os.listdir(loc2):
            fisier_actual_1 = os.path.join(loc1, fisier)
            fisier_actual_2 = os.path.join(loc2, fisier)
            if (os.path.exists(fisier_actual_2) and
                    os.path.isdir(fisier_actual_2)):
                rm_files(fisier_actual_1, fisier_actual_2)
                if not os.path.exists(fisier_actual_1):
                    if os.path.exists(fisier_actual_2):
                        os.rmdir(fisier_actual_2)
            else:
                if not os.path.exists(fisier_actual_1):
                    os.remove(fisier_actual_2)


if __name__ == "__main__":
    if len(argv) < 3:
        print ("Argumente insuficiente: [dir_1] [dir_2]")
    else:
        if not os.path.exists(argv[1]):
            os.mkdir(argv[1])
        if not os.path.exists(argv[2]):
            os.mkdir(argv[2])
        while True:
            unidirectional(argv[1], argv[2])
            rm_files(argv[1], argv[2])
