# 180 Sentinelles - protocoles de soutien pour aidants

SENTINELLES = [
    {"id": 1, "cat": "bienveillance", "titre": "Prendre soin de soi", "guide": "L'aidant a besoin de respirer. Accordez-vous 15 minutes par jour pour vous."},
    {"id": 2, "cat": "bienveillance", "titre": "Demander de l'aide", "guide": "Appeler un proche, un voisin ou une association. Vous n'êtes pas seul."},
    {"id": 3, "cat": "bienveillance", "titre": "Reconnaître sa fatigue", "guide": "La fatigue n'est pas une faiblesse. C'est un signal.",},
    {"id": 4, "cat": "bienveillance", "titre": "Accepter ses limites", "guide": "Vous ne pouvez pas tout faire seul. Acceptez l'aide.",},
    {"id": 5, "cat": "bienveillance", "titre": "Parler de ses émotions", "guide": "Exprimer sa tristesse, sa colère ou sa peur est nécessaire.",},
    {"id": 6, "cat": "soins", "titre": "Douleur du patient", "guide": "Observer le visage, la respiration. Demander au patient son niveau de douleur de 0 à 10.",},
    {"id": 7, "cat": "soins", "titre": "Difficultés respiratoires", "guide": "Installer le patient en position demi-assise. Aérer la pièce. Appeler le 15 si aggravation.",},
    {"id": 8, "cat": "soins", "titre": "Refus de manger", "guide": "Ne pas forcer. Proposer de petits repas légers. Consulter un médecin si plus de 3 jours.",},
    {"id": 9, "cat": "soins", "titre": "Refus de boire", "guide": "Proposer de l'eau par petites gorgées. Glaçons ou brumisation. Appeler médecin si signes de déshydratation.",},
    {"id": 10, "cat": "soins", "titre": "Agitation du patient", "guide": "Parler doucement. Toucher rassurant. Demander un avis médical si persiste.",},
    {"id": 11, "cat": "urgences", "titre": "Détresse respiratoire soudaine", "guide": "URGENCE. Appelez le 15 immédiatement. Installez le patient confortablement.",},
    {"id": 12, "cat": "urgences", "titre": "Hémorragie", "guide": "URGENCE. Appelez le 15. Compressez la plaie avec un linge propre.",},
    {"id": 13, "cat": "urgences", "titre": "Perte de connaissance", "guide": "URGENCE. Appelez le 15. Mettez la personne en position latérale de sécurité si possible.",},
    {"id": 14, "cat": "urgences", "titre": "Convulsion", "guide": "URGENCE. Protégez la personne, ne mettez rien dans sa bouche. Appelez le 15.",},
    {"id": 15, "cat": "relais", "titre": "Aide professionnelle", "guide": "Contacter l'HAD (Hospitalisation à Domicile) ou une association de soins palliatifs.",},
    {"id": 16, "cat": "relais", "titre": "Garde de répit", "guide": "Demander une aide à domicile pour quelques heures pour souffler.",},
    {"id": 17, "cat": "relais", "titre": "Groupe de parole", "guide": "Rejoindre un groupe d'entraide pour aidants. Parler avec des pairs aide.",},
    {"id": 18, "cat": "relais", "titre": "Appeler la ligne d'écoute", "guide": "Le 0 800 360 360 (France, gratuit). Des écoutants formés.",},
]

def get_sentinelles_summary():
    return "\n".join([f"S{s['id']:03d} | {s['titre']} → {s['guide']}" for s in SENTINELLES])
