#!/usr/bin/python3
"""
Interroge l'API Reddit et
retourne le nombre d'abonnés pour un subreddit donné.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Renvoie le nombre total d'abonnés pour un subreddit donné.

    Args:
        subreddit (str): Le nom du subreddit à interroger.

    Returns:
        int: Le nombre total d'abonnés du subreddit.
        Si le subreddit est invalide ou
        si la réponse de l'API est inattendue,
        renvoie 0.
    """
    # Construire l'URL pour interroger les informations du subreddit
    lnk = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Définir un en-tête User-Agent personnalisé
    # pour éviter les problèmes potentiels avec l'API Reddit
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Envoyer une requête GET à l'API
    response = requests.get(lnk, headers=headers)

    # Vérifier si la réponse est réussie (code d'état 200)
    if response.status_code == 200:
        # Analyser la réponse au format JSON
        data = response.json()

        # Vérifier si la structure de données attendue existe dans la réponse
        if 'data' in data and 'subscribers' in data['data']:
            # Récupérer le nombre d'abonnés depuis la réponse
            subscribers = data['data']['subscribers']
            return subscribers

    # Retourner 0 si le subreddit est invalide
    # ou si la réponse de l'API est inattendue
    return 0
