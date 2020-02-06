# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 08:45:01 2020
@author: David Enoma
"""
site = input("Please enter your restriction site sequence:\n")
seqs = {"GAATTC": "EcoRI", "GGATC": "Bam H1", "GGATCC": "Hind III"}
site = site.upper()
found = False
if len(site) > 1:
    for itr in seqs.keys():
        if itr == site:
            found = True
    if found:
        print("The restrction site belongs to: ", seqs[site])
    else:
        print("That is an unknown restriction site")
else:
    print("That is a single nucleotide,Try again")
