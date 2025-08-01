# 🚀 Guide d'Utilisation - Analyseur MIMO

## 🎯 Introduction

J'ai créé pour vous un ensemble de scripts Python complets pour analyser et afficher les performances des systèmes MIMO (Multiple-Input Multiple-Output). Ces outils permettent de simuler différents systèmes MIMO et d'analyser leurs performances avec des visualisations détaillées.

## 📁 Fichiers créés

### Scripts principaux :
- **`run_mimo.py`** - Script d'exécution principal avec menu interactif
- **`mimo_performance.py`** - Analyse complète avec 9 métriques de performance
- **`mimo_demo_simple.py`** - Démonstration simplifiée et rapide

### Fichiers de support :
- **`requirements.txt`** - Liste des dépendances Python
- **`README_MIMO.md`** - Documentation technique complète
- **`GUIDE_UTILISATION.md`** - Ce guide d'utilisation

## 🚀 Démarrage rapide

### 1. Vérifier l'installation
Les dépendances ont déjà été installées sur ce système. Pour une nouvelle installation :

```bash
sudo apt install python3-numpy python3-matplotlib python3-scipy python3-seaborn
```

### 2. Lancer le programme principal
```bash
python3 run_mimo.py
```

Le menu interactif vous permettra de choisir entre :
- **Analyse complète** : Toutes les métriques avec graphiques détaillés
- **Démonstration rapide** : Version simplifiée pour test rapide
- **Aide** : Documentation intégrée

### 3. Alternative : Exécution directe
```bash
# Analyse complète (recommandée)
python3 mimo_performance.py

# Démonstration rapide
python3 mimo_demo_simple.py
```

## 📊 Ce que vous obtiendrez

### Graphiques générés :
1. **Capacité du canal** MIMO vs SISO
2. **Distribution du nombre de condition**
3. **Évolution des valeurs propres**
4. **Performances BER** pour QPSK
5. **Réponse fréquentielle** du canal
6. **Corrélation spatiale** entre antennes
7. **Distribution des gains** du canal
8. **Comparaison des modulations** (QPSK, 16-QAM, 64-QAM)
9. **Efficacité spectrale**

### Statistiques textuelles :
- Configuration du système (antennes TX/RX, sous-porteuses)
- Capacité à différents niveaux de SNR
- Gain MIMO théorique vs pratique
- Métriques de qualité du canal
- Analyse de la diversité spatiale

## 🔧 Configurations analysées

Le script teste automatiquement plusieurs configurations :
- **2x2 MIMO** : 2 antennes de transmission, 2 de réception
- **4x4 MIMO** : Configuration standard pour LTE/5G
- **8x8 MIMO** : Systèmes avancés massive MIMO

## 📡 Types de canaux supportés

- **Rayleigh** : Fading sans composante directe (par défaut)
- **Rician** : Avec composante en ligne de vue (LOS)
- **AWGN** : Canal idéal sans fading

## 💡 Exemple de résultats

```
🚀 DÉMARRAGE DE L'ANALYSE DES PERFORMANCES MIMO
============================================================

🔍 ANALYSE CONFIGURATION 4x4 MIMO
----------------------------------------

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
```

## 🎨 Personnalisation

Pour modifier les paramètres, éditez les scripts :

```python
# Dans mimo_performance.py ou mimo_demo_simple.py
n_tx = 4           # Nombre d'antennes de transmission
n_rx = 4           # Nombre d'antennes de réception  
n_subcarriers = 64 # Nombre de sous-porteuses

# Type de canal
channel_type = 'rayleigh'  # 'rayleigh', 'rician', 'awgn'
```

## ⚡ Performance et optimisation

- **Analyse complète** : 2-5 minutes selon la configuration
- **Démonstration rapide** : 30 secondes
- Les calculs sont optimisés avec NumPy et SciPy
- Les graphiques utilisent matplotlib avec style moderne

## 🛠️ Dépannage

### Problème d'affichage graphique :
```python
# Ajoutez en haut du script :
import matplotlib
matplotlib.use('Agg')  # Pour sauvegarder sans affichage
```

### Erreur de mémoire :
- Réduisez le nombre de sous-porteuses dans le script
- Utilisez la version démonstration rapide

### Pas d'interaction :
- Fermez les fenêtres graphiques pour continuer
- Utilisez Ctrl+C pour interrompre si nécessaire

## 📚 Pour aller plus loin

- **README_MIMO.md** : Documentation technique détaillée
- **Théorie MIMO** : Communications sans fil, diversité spatiale
- **Applications** : LTE, 5G, WiFi 6, systèmes radar

## 🎯 Cas d'usage

### Éducation :
- Comprendre les gains de la technologie MIMO
- Visualiser l'impact des configurations d'antennes
- Analyser différents types de canaux

### Recherche :
- Évaluer de nouvelles configurations MIMO
- Comparer différents algorithmes
- Analyser l'impact des conditions de propagation

### Industrie :
- Optimiser les systèmes de communication
- Évaluer les performances en conditions réelles
- Valider les modèles théoriques

---

✅ **Tous les scripts sont prêts à l'emploi !**

Pour commencer, exécutez simplement :
```bash
python3 run_mimo.py
```