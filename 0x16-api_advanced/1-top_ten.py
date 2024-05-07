#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """
    Interroge l'API Reddit et affiche les titres
    des 10 premiers posts populaires d'un subreddit donné.

    Args:
        subreddit (str): Le nom du subreddit à rechercher.

    Returns:
        None
    """
    # Construire l'URL pour interroger les
    # posts populaires du subreddit spécifié
    lnk = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Définir un en-tête User-Agent personnalisé
    # pour éviter les problèmes potentiels avec l'API Reddit
    hadrs = {'User-Agent': 'Mozilla/5.0'}

    # Paramètres de requête pour limiter le nombre de posts à 10
    prms = {'limit': 10}

    # Envoyer une requête GET à l'API
    # Reddit pour récupérer les posts populaires
    rspnse = requests.get(lnk, headers=hadrs, params=prms)

    # Vérifier si la requête a réussi (code d'état 200)
    if rspnse.status_code == 200:
        # Analyser la réponse au format JSON
        data = rspnse.json()
        psts = data['data']['children']

        # Parcourir les posts et afficher leurs titres
        for post in psts:
            ttle = post['data']['title']
            print(ttle)
    else:
        # Afficher "None" si le subreddit est invalide
        # ou s'il y a une erreur dans la requête API
        print("None")
