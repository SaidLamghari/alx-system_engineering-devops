#!/usr/bin/python3
"""
2-recurse
Autor: Said LAMGHARI
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Fonction récursive qui interroge l'API Reddit et renvoie
    une liste contenant les titres de
    tous les articles populaires d'un subreddit donné.

    Args:
        subreddit (str): Le nom du subreddit à rechercher.
        hot_list (list): La liste des titres
                        d'articles populaires (par défaut=[]).

    Returns:
        list ou None: La liste des titres d'articles
        populaires ou None si le subreddit est invalide.
    """
    lnk = f"https://www.reddit.com/r/{subreddit}/hot.json"
    hadrs = {'User-Agent': 'Mozilla/5.0'}
    # Limite le nombre de posts à 100 par requête
    prms = {'limit': 100}

    # Envoie une requête GET à l'API
    # Reddit pour récupérer les posts populaires
    response = requests.get(lnk, headers=hadrs, params=prms)

    # Vérifie si la requête a réussi (code d'état 200)
    if response.status_code == 200:
        dt = response.json()
        posts = dt['data']['children']

        # Parcourt les posts et ajoute leurs titres à la hot_list
        for post in posts:
            ttle = post['data']['title']
            hot_list.append(ttle)

        # Vérifie s'il y a d'autres posts à récupérer (pagination)
        after = dt['data']['after']
        if after is not None:
            # Appelle récursivement la fonction
            # pour récupérer la page suivante de posts
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
