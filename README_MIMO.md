# Analyse des Performances MIMO

Ce projet contient des scripts Python pour analyser et visualiser les performances des systèmes MIMO (Multiple-Input Multiple-Output).

## 📋 Fichiers inclus

- **`mimo_performance.py`** : Script complet d'analyse MIMO avec toutes les métriques
- **`mimo_demo_simple.py`** : Version simplifiée pour démonstration rapide
- **`requirements.txt`** : Dépendances Python nécessaires

## 🚀 Installation

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Ou installer manuellement :
```bash
pip install numpy matplotlib seaborn scipy
```

## 💻 Utilisation

### Version complète (recommandée)
```bash
python mimo_performance.py
```

### Version simplifiée (test rapide)
```bash
python mimo_demo_simple.py
```

## 📊 Métriques analysées

### Version complète (`mimo_performance.py`)
- **Capacité du canal** MIMO vs SISO
- **Nombre de condition** du canal
- **Valeurs propres** de la matrice de canal
- **Performances BER** (Bit Error Rate)
- **Réponse fréquentielle** du canal
- **Corrélation spatiale** entre antennes
- **Distribution des gains** du canal
- **Comparaison des modulations** (QPSK, 16-QAM, 64-QAM)
- **Efficacité spectrale**

### Version simplifiée (`mimo_demo_simple.py`)
- Capacité MIMO vs SISO
- Distribution des gains du canal
- Réponse fréquentielle
- Valeurs propres principales

## 🔧 Configurations testées

Le script analyse plusieurs configurations MIMO :
- **2x2 MIMO** (2 antennes TX, 2 antennes RX)
- **4x4 MIMO** (4 antennes TX, 4 antennes RX)
- **8x8 MIMO** (8 antennes TX, 8 antennes RX)

## 📡 Types de canaux supportés

- **Rayleigh** : Canal avec fading (par défaut)
- **Rician** : Canal avec composante LOS + fading
- **AWGN** : Canal sans fading

## 📈 Résultats affichés

### Graphiques générés :
1. Courbes de capacité en fonction du SNR
2. Histogrammes de distribution du nombre de condition
3. Évolution des valeurs propres
4. Courbes de BER pour différentes modulations
5. Réponse fréquentielle du canal
6. Matrices de corrélation spatiale
7. Distribution des gains du canal
8. Comparaison des modulations
9. Efficacité spectrale

### Statistiques textuelles :
- Configuration du système
- Capacité à différents SNR
- Gain MIMO théorique vs pratique
- Condition du canal (moyenne, max, écart-type)
- Valeurs propres moyennes
- Gain de diversité

## 🎯 Exemple de sortie

```
🚀 DÉMARRAGE DE L'ANALYSE DES PERFORMANCES MIMO
============================================================

🔍 ANALYSE CONFIGURATION 4x4 MIMO
----------------------------------------

================================================================================
RAPPORT DE PERFORMANCE MIMO 4x4
================================================================================

📊 CONFIGURATION SYSTÈME:
   • Antennes TX: 4
   • Antennes RX: 4
   • Sous-porteuses: 64
   • Type de canal: Rayleigh Fading

📡 CAPACITÉ DU CANAL:
   • Capacité à 20 dB: 15.23 bits/s/Hz
   • Capacité maximale: 18.45 bits/s/Hz
   • Gain MIMO théorique: 4x

🔧 CONDITION DU CANAL:
   • Nombre de condition moyen: 5.67
   • Nombre de condition max: 12.34
   • Écart-type: 2.11

🎯 VALEURS PROPRES:
   • λ_1 moyen: 3.456
   • λ_2 moyen: 2.789
   • λ_3 moyen: 1.234
   • λ_4 moyen: 0.567

🌟 DIVERSITÉ:
   • Gain de diversité (variance): 0.543
   • Ordre de diversité max: 16
```

## 🔬 Personnalisation

Vous pouvez modifier les paramètres dans le script :

```python
# Dans mimo_performance.py
analyzer = MIMOPerformanceAnalyzer(
    n_tx=4,           # Nombre d'antennes TX
    n_rx=4,           # Nombre d'antennes RX
    n_subcarriers=64  # Nombre de sous-porteuses
)

# Type de canal
analyzer.generate_channel_matrix('rayleigh')  # 'rayleigh', 'rician', 'awgn'
```

## 📝 Notes importantes

- Les simulations utilisent des modèles statistiques de canaux
- Les résultats peuvent varier entre les exécutions (caractère aléatoire du canal)
- Pour des résultats reproductibles, fixez la graine aléatoire : `np.random.seed(42)`
- Les graphiques s'affichent automatiquement avec matplotlib

## 🛠️ Dépannage

**Erreur d'import matplotlib :**
```bash
sudo apt-get install python3-tk  # Sur Linux
# ou
pip install matplotlib --upgrade
```

**Pas d'affichage graphique :**
- Vérifiez que vous avez un environnement graphique
- Utilisez `plt.savefig()` au lieu de `plt.show()` pour sauvegarder

## 📚 Références

- Théorie des communications MIMO
- Analyse de la capacité de Shannon
- Modèles de canaux sans fil
- Techniques de diversité spatiale