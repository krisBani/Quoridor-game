from api import debuter_partie, jouer_coup, lister_parties
from quoridor import analyser_commande, formater_jeu, formater_les_parties, recuperer_le_coup

SECRET = "36905bee-29d1-492f-9ba8-714a4cbc8110"

if __name__ == "__main__":
    args = analyser_commande()

    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
    else:
        id_partie, etat = debuter_partie(args.idul, SECRET)
        while True:
            print(formater_jeu(etat))
            type_coup, position = recuperer_le_coup()
            id_partie, etat = jouer_coup(id_partie, type_coup, position, args.idul, SECRET)