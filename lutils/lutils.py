#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author : Alix Chagué
Date : 24/09/2021
"""

# LEPIDEMO utils


def flush_dir(path): 
    import shutil
    
    msg = f"Êtes-vous sûr de vouloir supprimer le contenu du dossier '{path}'? (o=oui)"
    user_answer = input(msg)
    if user_answer in ["o"]:
        try:
            shutil.rmtree(path)
        except OSError as e:
            print("Error:", e.strerror, sep="\n")
    else:
        print("Suppression avortée")
        

        
def pywget(url, target_name=None, verify=True):
    import os
    import requests

    r = requests.get(url, allow_redirects=True, verify=verify)
    if r.status_code != 200:
        r.raise_for_status()
    else:
        if not target_name:
            target_name = os.path.basename(url)
        open(target_name, "wb").write(r.content)
    
    

