#!/usr/bin/env python3
"""
Script d'exécution principal pour l'analyse des performances MIMO
"""

import sys
import subprocess

def print_menu():
    """Affiche le menu principal"""
    print("\n" + "="*60)
    print("🚀 ANALYSEUR DE PERFORMANCES MIMO")
    print("="*60)
    print("\nChoisissez une option:")
    print("1. 📊 Analyse complète MIMO (recommandée)")
    print("2. ⚡ Démonstration rapide")
    print("3. 📖 Afficher l'aide")
    print("4. 🚪 Quitter")
    print("\n" + "-"*60)

def run_complete_analysis():
    """Lance l'analyse complète"""
    print("\n🔍 Lancement de l'analyse complète MIMO...")
    print("⏳ Cela peut prendre quelques minutes...")
    try:
        result = subprocess.run(['python3', 'mimo_performance.py'], 
                              capture_output=False, text=True)
        if result.returncode == 0:
            print("✅ Analyse terminée avec succès!")
        else:
            print("❌ Erreur lors de l'exécution")
    except Exception as e:
        print(f"❌ Erreur: {e}")

def run_quick_demo():
    """Lance la démonstration rapide"""
    print("\n⚡ Lancement de la démonstration rapide...")
    try:
        result = subprocess.run(['python3', 'mimo_demo_simple.py'], 
                              capture_output=False, text=True)
        if result.returncode == 0:
            print("✅ Démonstration terminée avec succès!")
        else:
            print("❌ Erreur lors de l'exécution")
    except Exception as e:
        print(f"❌ Erreur: {e}")

def show_help():
    """Affiche l'aide"""
    print("\n📖 AIDE - ANALYSEUR MIMO")
    print("="*40)
    print("\n🎯 OBJECTIF:")
    print("Ce programme analyse les performances des systèmes MIMO")
    print("(Multiple-Input Multiple-Output) utilisés en communications sans fil.")
    
    print("\n📊 MÉTRIQUES ANALYSÉES:")
    print("• Capacité du canal MIMO vs SISO")
    print("• Nombre de condition du canal")
    print("• Valeurs propres de la matrice de canal")
    print("• Performances BER (Bit Error Rate)")
    print("• Réponse fréquentielle")
    print("• Corrélation spatiale")
    print("• Distribution des gains")
    print("• Efficacité spectrale")
    
    print("\n🔧 CONFIGURATIONS TESTÉES:")
    print("• 2x2 MIMO (2 antennes TX, 2 antennes RX)")
    print("• 4x4 MIMO (4 antennes TX, 4 antennes RX)")
    print("• 8x8 MIMO (8 antennes TX, 8 antennes RX)")
    
    print("\n📡 TYPES DE CANAUX:")
    print("• Rayleigh: Canal avec fading (par défaut)")
    print("• Rician: Canal avec composante LOS + fading")
    print("• AWGN: Canal sans fading")
    
    print("\n💡 CONSEILS:")
    print("• Commencez par l'analyse complète pour une vue d'ensemble")
    print("• Utilisez la démonstration rapide pour un test rapide")
    print("• Les graphiques peuvent prendre quelques secondes à s'afficher")
    print("• Fermez les fenêtres graphiques pour continuer")
    
    print("\n📚 POUR EN SAVOIR PLUS:")
    print("Consultez le fichier README_MIMO.md pour la documentation complète")

def main():
    """Fonction principale"""
    while True:
        print_menu()
        
        try:
            choice = input("Votre choix (1-4): ").strip()
            
            if choice == '1':
                run_complete_analysis()
            elif choice == '2':
                run_quick_demo()
            elif choice == '3':
                show_help()
            elif choice == '4':
                print("\n👋 Au revoir!")
                sys.exit(0)
            else:
                print("\n❌ Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programme interrompu. Au revoir!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Erreur: {e}")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    print("🔧 Vérification des dépendances...")
    try:
        import numpy as np
        import matplotlib.pyplot as plt
        import scipy
        print("✅ Toutes les dépendances sont installées")
        main()
    except ImportError as e:
        print(f"❌ Dépendance manquante: {e}")
        print("\n🛠️  Pour installer les dépendances:")
        print("sudo apt install python3-numpy python3-matplotlib python3-scipy python3-seaborn")
        sys.exit(1)