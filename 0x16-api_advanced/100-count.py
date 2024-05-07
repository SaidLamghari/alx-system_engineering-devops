#!/usr/bin/python3
"""
100-count
Autor: Said LAMGHARI
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Fonction récursive qui interroge l'API Reddit,
    analyse les titres de tous les articles populaires
    et affiche un décompte trié des mots-clés donnés.

    Args:
        subreddit (str): Le nom du subreddit à rechercher.
        word_list (list): La liste des mots-clés à dénombrer.
        after (str): Le jeton 'after' pour la pagination (par défaut=None).
        count_dict (dict): Un dictionnaire pour
        stocker les décomptes des mots-clés (par défaut=None).

    Returns:
        None
    """

    if count_dict is None:
        # Initialise le dictionnaire de décompte
        count_dict = {}

    lnk = f"https://www.reddit.com/r/{subreddit}/hot.json"
    hadrs = {'User-Agent': 'Mozilla/5.0'}
    prms = {'limit': 100, 'after': after} if after else {'limit': 100}

    # Envoie une requête GET à l'API Reddit
    # pour récupérer les posts populaires
    response = requests.get(lnk, headers=hadrs, params=prms)

    # Vérifie si la requête a réussi (code d'état 200)
    if response.status_code == 200:
        dt = response.json()
        psts = dt['data']['children']

        # Parcourt les posts et analyse
        # les titres pour dénombrer les mots-clés
        for pst in psts:
            title = pst['data']['title']
            wrds = title.lower().split()

            for word in word_list:
                count = wrds.count(word.lower())
                if count > 0:
                    if word in count_dict:
                        count_dict[word] += count
                    else:
                        count_dict[word] = count

        ftr = dt['data']['after']
        if ftr is not None:
            # Appelle récursivement la fonction
            # avec le jeton 'after' pour la pagination
            count_words(subreddit, word_list, after=ftr, count_dict=count_dict)
        else:
            # Trie les décomptes par ordre décroissant
            # de décompte et par ordre alphabétique de mot-clé
            srtd_cnts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in srtd_cnts:
                print(f"{word}: {count}")
    else:
        return None
