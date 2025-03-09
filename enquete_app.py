import streamlit as st
import pandas as pd
import os
from streamlit.runtime.scriptrunner import RerunException, RerunData  # Import pour forcer le redémarrage

# Configuration de la page
st.set_page_config(
    page_title="Enquête Cybersécurité en Ligne",
    page_icon="🔒",
    layout="centered",
)

# Fonction pour enregistrer les données dans un fichier CSV
def sauvegarder_donnees(nom_fichier, nouvelles_donnees):
    if not os.path.exists(nom_fichier):
        nouvelles_donnees.to_csv(nom_fichier, index=False)
    else:
        anciennes_donnees = pd.read_csv(nom_fichier)
        toutes_les_donnees = pd.concat([anciennes_donnees, nouvelles_donnees], ignore_index=True)
        toutes_les_donnees.to_csv(nom_fichier, index=False)

# Fonction pour réinitialiser le fichier CSV
def reinitialiser_donnees(nom_fichier):
    if os.path.exists(nom_fichier):
        os.remove(nom_fichier)

# Fonction pour lire le contenu du fichier CSV
def lire_contenu_csv(nom_fichier):
    if os.path.exists(nom_fichier):
        return pd.read_csv(nom_fichier)
    else:
        return pd.DataFrame()  # Retourne un DataFrame vide si le fichier n'existe pas

# Chemin du fichier CSV
nom_fichier = "resultats_enquete_cybersecurite.csv"

# Titre de l'application
st.title("🔒 Enquête Cybersécurité en Ligne")
st.write("Dans le cadre de la rédaction de mon mémoire de DSCG, je réalise une enquête autour de la sensibilisation des collaborateurs aux risques de la cybersécurité.\n\n"
         "Ce questionnaire est entièrement anonyme et réalisé uniquement à des fins de recherche.\n\n"
         "Je remercie par avance toutes les personnes qui prendront quelques minutes pour répondre à ce questionnaire.\n\n"
         "Ce questionnaire est ouvert jusqu’à mi-avril.")

# Questions de l'enquête (visibles à tous les utilisateurs)
with st.form("form_enquete"):
    # Section I
    st.header("I. Certains comportements des collaborateurs peuvent accroître les risques de cybersécurité.")
    q1 = st.selectbox("1\u00A0.\u00A0Utilisez-vous des mots de passe forts et uniques pour chaque compte professionnel ?", 
                      ["", "Toujours", "Parfois", "Jamais"], key="q1")
    q2 = st.selectbox("2\u00A0.\u00A0Partagez-vous vos mots de passe avec vos collègues ou les stockez-vous dans un endroit non sécurisé ?", 
                      ["", "Oui régulièrement", "Rarement", "Jamais"], key="q2")
    q3 = st.selectbox("3\u00A0.\u00A0Vérifiez-vous systématiquement la source d’un lien avant de cliquer dessus ?", 
                      ["", "Toujours", "Parfois", "Jamais"], key="q3")
    q4 = st.selectbox("4\u00A0.\u00A0Utilisez-vous des appareils personnels pour accéder à des données professionnelles ?", 
                      ["", "Oui", "Non"], key="q4")
    q5 = st.selectbox("5\u00A0.\u00A0Vous connectez-vous à des réseaux Wi-Fi publics pour travailler sans utiliser le VPN ?", 
                      ["", "Oui", "Non"], key="q5")
    q6 = st.selectbox("6\u00A0.\u00A0Verrouillez-vous votre poste de travail lorsque vous vous absentez ?", 
                      ["", "Toujours", "Parfois", "Jamais"], key="q6")
    q7 = st.selectbox("7\u00A0.\u00A0Comprenez-vous les conséquences possibles d’une attaque de cybersécurité sur l’entreprise ?", 
                      ["", "Oui", "Non", "Partiellement"], key="q7")
    q8 = st.selectbox("8\u00A0.\u00A0Savez-vous identifier un e-mail de phishing ?", 
                      ["", "Oui facilement", "Parfois cela dépend", "Non je ne sais pas"], key="q8")
    q9 = st.selectbox("9\u00A0.\u00A0Avez-vous été formé(e) aux bonnes pratiques dans votre entreprise ?", 
                      ["", "Oui", "Non", "Je ne suis pas sûr(e)"], key="q9")

    # Section II
    st.header("II. Les cyberattaques, telles que les Malwares et le Phishing, figurent parmi les tendances les plus fréquentes.")
    q10 = st.selectbox("10\u00A0.\u00A0Selon vous, qu’est-ce qu’une cyberattaque ?", 
                       ["", "Une attaque informatique visant à compromettre un système", 
                        "Une panne de réseau", 
                        "Un virus informatique qui nettoie les données"], key="q10")
    q11 = st.selectbox("11\u00A0.\u00A0Les Malwares sont :", 
                       ["", "Des logiciels malveillants destinés à causer des dommages", 
                        "Des outils pour améliorer la performance des ordinateurs", 
                        "Des extensions pour navigateurs"], key="q11")
    q12 = st.selectbox("12\u00A0.\u00A0Avez-vous déjà subi un ou des Malwares ?", ["", "Oui", "Non"], key="q12")
    q13 = st.selectbox("13\u00A0.\u00A0Avez-vous déjà subi des Phishing ?", ["", "Oui", "Non"], key="q13")
    q14 = st.selectbox("14\u00A0.\u00A0Combien d’autres types de cyberattaques connaissez-vous hormis les Malwares et le Phishing ?", 
                       ["", "0", "1", "3", "4", "5"], key="q14")
    q15 = st.selectbox("15\u00A0.\u00A0Pensez-vous que le Malware et le Phishing sont les attaques les plus fréquentes ?", 
                       ["", "Oui", "Non"], key="q15")
    q16 = st.selectbox("16\u00A0.\u00A0Selon vous, quel pourcentage des cyberattaques repose sur des erreurs humaines ?", 
                       ["", "10%", "50%", "Plus de 80%"], key="q16")

    # Section III
    st.header("III. Les réponses en matière de cybersécurité pourraient s’avérer inefficaces face aux risques de cyberattaque.")
    q17 = st.selectbox("17\u00A0.\u00A0Quel est le secteur d’activité principal de votre entreprise ?", 
                       ["", "Comptabilité", "Finance", "Technologie", "Éducation", "Autre :"], key="q17")
    q18 = st.selectbox("18\u00A0.\u00A0Combien d’employés travaillent dans votre entreprise ?", 
                       ["", "Moins de 50", "50-250", "250-1000", "Plus de 1000"], key="q18")
    q19 = st.selectbox("19\u00A0.\u00A0Quelle est la fréquence des audits ou évaluations de cybersécurité ?", 
                       ["", "Jamais", "Une fois par an", "Tous les trimestres", "Plus fréquemment"], key="q19")

    st.write("20\u00A0.\u00A0Quelles mesures de cybersécurité sont en place dans votre entreprise ?")
    q20_antivirus = st.selectbox("Antivirus/Malware ?", ["", "Oui", "Non"], key="q20_antivirus")
    q20_pare_feu = st.selectbox("Pare-feu ?", ["", "Oui", "Non"], key="q20_pare_feu")
    q20_formation = st.selectbox("Formation des employés à la cybersécurité ?", ["", "Oui", "Non"], key="q20_formation")
    q20_sauvegardes = st.selectbox("Sauvegardes régulières des données ?", ["", "Oui", "Non"], key="q20_sauvegardes")
    q20_mdp = st.selectbox("Politique de gestion des mots de passe ?", ["", "Oui", "Non"], key="q20_mdp")
    q20_detection = st.selectbox("Logiciel de détection aux intrusions ?", ["", "Oui", "Non"], key="q20_detection")

    st.write("21\u00A0.\u00A0Par le passé, lesquelles de ces mesures ont été jugées inefficaces face à une cyberattaque ?")
    q21_antivirus = st.selectbox("Antivirus/Malware ?", ["", "Oui", "Non"], key="q21_antivirus")
    q21_pare_feu = st.selectbox("Pare-feu ?", ["", "Oui", "Non"], key="q21_pare_feu")
    q21_formation = st.selectbox("Formation des employés à la cybersécurité ?", ["", "Oui", "Non"], key="q21_formation")
    q21_sauvegardes = st.selectbox("Sauvegardes régulières des données ?", ["", "Oui", "Non"], key="q21_sauvegardes")
    q21_mdp = st.selectbox("Politique de gestion des mots de passe ?", ["", "Oui", "Non"], key="q21_mdp")
    q21_autre = st.selectbox("Autres ?", ["", "Oui", "Non"], key="q21_autres")

    # Section IV
    st.header("IV. Un environnement de travail qui encourage le signalement des incidents favorise une détection précoce.")
    q22 = st.selectbox("22\u00A0.\u00A0Au sein de votre entreprise, existe-t-il une procédure de signalement des menaces ?", 
                       ["", "Oui", "Non"], key="q22")
    q23 = st.selectbox("23\u00A0.\u00A0Comprenez-vous les procédures actuelles de signalement des incidents dans votre entreprise ?", 
                       ["", "Oui", "Non", "Pas sûr"], key="q23")
    q24 = st.selectbox("24\u00A0.\u00A0Avez-vous reçu une formation sur l’importance de signaler les incidents ?", ["", "Oui", "Non"], key="q24")
    q25 = st.selectbox("25\u00A0.\u00A0Savez-vous où trouver les outils ou canaux pour signaler les incidents ?", ["", "Oui", "Non"], key="q25")
    q26 = st.selectbox("26\u00A0.\u00A0Dans quelle mesure vous sentez-vous à l’aise pour signaler un incident ou un problème de sécurité ?", 
                       ["", "Très à l’aise", "Assez à l’aise", "Peu à l’aise", "Pas à l’aise du tout"], key="q26")
    q27 = st.selectbox("27\u00A0.\u00A0Avez-vous déjà hésité à signaler un incident par crainte de représailles ou répercussions ?", 
                       ["", "Oui", "Non"], key="q27")
    q28 = st.selectbox("28\u00A0.\u00A0Pensez-vous que les signalements d’incidents sont pris au sérieux par la direction ?", 
                       ["", "Toujours", "Souvent", "Parfois", "Rarement", "Jamais"], key="q28")
    q29 = st.selectbox("29\u00A0.\u00A0Les procédures de signalement sont-elles faciles à utiliser ?", ["", "Oui", "Non"], key="q29")
    q30 = st.selectbox("30\u00A0.\u00A0Après avoir signalé un incident, recevez-vous un retour sur les actions prises ?", ["", "Oui", "Non"], key="q30")
    q31 = st.selectbox("31\u00A0.\u00A0Les incidents signalés sont-ils traités dans un délai raisonnable ?", ["", "Oui", "Non"], key="q31")

    # Soumettre le formulaire
    submitted = st.form_submit_button("Soumettre")
    if submitted:
        # Enregistrer les réponses dans un DataFrame
        nouvelles_donnees = pd.DataFrame([{
            "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5, "Q6": q6, "Q7": q7, "Q8": q8, "Q9": q9,
            "Q10": q10, "Q11": q11, "Q12": q12, "Q13": q13, "Q14": q14, "Q15": q15, "Q16": q16,
            "Q17": q17, "Q18": q18, "Q19": q19,
            "Q20_Antivirus": q20_antivirus, "Q20_Pare_feu": q20_pare_feu,
            "Q20_Formation": q20_formation, "Q20_Sauvegardes": q20_sauvegardes,
            "Q20_Politique_MDP": q20_mdp, "Q20_Detection": q20_detection,
            "Q21_Antivirus": q21_antivirus, "Q21_Pare_feu": q21_pare_feu,
            "Q21_Formation": q21_formation, "Q21_Sauvegardes": q21_sauvegardes,
            "Q21_Politique_MDP": q21_mdp, "Q21_Autres": q21_autre,
            "Q22": q22, "Q23": q23, "Q24": q24, "Q25": q25, "Q26": q26, "Q27": q27, 
            "Q28": q28, "Q29": q29, "Q30": q30, "Q31": q31
        }])
        sauvegarder_donnees(nom_fichier, nouvelles_donnees)
        st.success("Merci pour votre participation ! Vos réponses ont été enregistrées.")

# Section administrateur déplacée en bas
st.write("---")  # Séparation visuelle
mot_de_passe = st.text_input("Entrez le mot de passe pour accéder à la section administrateur :", type="password")
if mot_de_passe == "Christine@taveres2025":
    # Section visible uniquement si le mot de passe est correct
    st.success("Accès administrateur accordé.")
    st.subheader("🔒 Section Administrateur")
    
    # Afficher le contenu du fichier CSV
    st.write("### Contenu du fichier CSV des réponses")
    contenu_csv = lire_contenu_csv(nom_fichier)
    if not contenu_csv.empty:
        st.dataframe(contenu_csv)  # Afficher le contenu du fichier CSV sous forme de tableau
    else:
        st.info("Aucune donnée disponible pour le moment.")

    # Boutons pour gérer les actions administratives
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Rafraîchir la page"):
            raise RerunException(RerunData(None))  # Forcer le redémarrage
    with col2:
        if st.button("🗑️ Réinitialiser l'enquête"):
            reinitialiser_donnees(nom_fichier)
            st.success("Les réponses ont été réinitialisées.")
            raise RerunException(RerunData(None))  # Forcer le redémarrage
elif mot_de_passe:
    # Si un mot de passe incorrect est saisi
    st.error("Mot de passe incorrect.")
