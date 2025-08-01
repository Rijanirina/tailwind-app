#!/usr/bin/env python3
"""
Script d'analyse des performances MIMO (Multiple-Input Multiple-Output)
Ce script simule un système MIMO et affiche ses performances avec diverses métriques.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import linalg
from scipy.signal import find_peaks
import warnings
warnings.filterwarnings('ignore')

class MIMOPerformanceAnalyzer:
    """Classe pour analyser les performances d'un système MIMO"""
    
    def __init__(self, n_tx=4, n_rx=4, n_subcarriers=64):
        """
        Initialise l'analyseur MIMO
        
        Args:
            n_tx: Nombre d'antennes de transmission
            n_rx: Nombre d'antennes de réception
            n_subcarriers: Nombre de sous-porteuses
        """
        self.n_tx = n_tx
        self.n_rx = n_rx
        self.n_subcarriers = n_subcarriers
        self.channel_matrix = None
        self.performance_metrics = {}
        
    def generate_channel_matrix(self, channel_type='rayleigh'):
        """
        Génère une matrice de canal MIMO
        
        Args:
            channel_type: Type de canal ('rayleigh', 'rician', 'awgn')
        """
        if channel_type == 'rayleigh':
            # Canal Rayleigh (fading)
            h_real = np.random.randn(self.n_rx, self.n_tx, self.n_subcarriers)
            h_imag = np.random.randn(self.n_rx, self.n_tx, self.n_subcarriers)
            self.channel_matrix = (h_real + 1j * h_imag) / np.sqrt(2)
            
        elif channel_type == 'rician':
            # Canal Rician (composante LOS + fading)
            k_factor = 3  # Facteur de Rice en dB
            k_linear = 10**(k_factor/10)
            
            # Composante LOS
            h_los = np.ones((self.n_rx, self.n_tx, self.n_subcarriers))
            
            # Composante diffuse
            h_real = np.random.randn(self.n_rx, self.n_tx, self.n_subcarriers)
            h_imag = np.random.randn(self.n_rx, self.n_tx, self.n_subcarriers)
            h_nlos = (h_real + 1j * h_imag) / np.sqrt(2)
            
            # Canal Rician total
            self.channel_matrix = np.sqrt(k_linear/(k_linear+1)) * h_los + \
                                np.sqrt(1/(k_linear+1)) * h_nlos
                                
        elif channel_type == 'awgn':
            # Canal AWGN (pas de fading)
            self.channel_matrix = np.ones((self.n_rx, self.n_tx, self.n_subcarriers))
            
        return self.channel_matrix
    
    def calculate_capacity(self, snr_db_range):
        """
        Calcule la capacité du canal MIMO
        
        Args:
            snr_db_range: Plage de SNR en dB
            
        Returns:
            capacity: Capacité en bits/s/Hz pour chaque SNR
        """
        snr_linear = 10**(np.array(snr_db_range) / 10)
        capacity = []
        
        for snr in snr_linear:
            cap_subcarriers = []
            
            for sc in range(self.n_subcarriers):
                H = self.channel_matrix[:, :, sc]
                
                # Matrice de covariance du bruit
                noise_power = 1 / snr
                I = np.eye(self.n_rx)
                
                # Capacité MIMO avec allocation uniforme de puissance
                HH_hermitian = H @ H.conj().T
                capacity_sc = np.log2(np.real(linalg.det(I + (snr/self.n_tx) * HH_hermitian)))
                cap_subcarriers.append(capacity_sc)
            
            capacity.append(np.mean(cap_subcarriers))
            
        return np.array(capacity)
    
    def calculate_condition_number(self):
        """Calcule le nombre de condition du canal"""
        condition_numbers = []
        
        for sc in range(self.n_subcarriers):
            H = self.channel_matrix[:, :, sc]
            cond_num = np.linalg.cond(H)
            condition_numbers.append(cond_num)
            
        return np.array(condition_numbers)
    
    def calculate_eigenvalues(self):
        """Calcule les valeurs propres de H*H^H"""
        eigenvalues_all = []
        
        for sc in range(self.n_subcarriers):
            H = self.channel_matrix[:, :, sc]
            HH_hermitian = H @ H.conj().T
            eigenvals = np.linalg.eigvals(HH_hermitian)
            eigenvalues_all.append(np.real(eigenvals))
            
        return np.array(eigenvalues_all)
    
    def calculate_ber_performance(self, snr_db_range, modulation='qpsk'):
        """
        Calcule les performances BER pour différentes techniques MIMO
        
        Args:
            snr_db_range: Plage de SNR en dB
            modulation: Type de modulation ('qpsk', '16qam', '64qam')
        """
        snr_linear = 10**(np.array(snr_db_range) / 10)
        
        # Simulation simplifiée du BER
        if modulation == 'qpsk':
            ber_base = 0.5 * np.exp(-snr_linear)
        elif modulation == '16qam':
            ber_base = 0.75 * np.exp(-snr_linear * 0.8)
        elif modulation == '64qam':
            ber_base = 0.9 * np.exp(-snr_linear * 0.6)
        
        # Gain MIMO (diversité spatiale)
        mimo_gain = self.n_tx * self.n_rx
        ber_mimo = ber_base / mimo_gain
        
        # SISO pour comparaison
        ber_siso = ber_base
        
        return ber_siso, ber_mimo
    
    def plot_performance_metrics(self, snr_range=np.arange(-10, 30, 2)):
        """Affiche toutes les métriques de performance"""
        
        # Configuration de la figure
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 15))
        
        # 1. Capacité du canal
        plt.subplot(3, 3, 1)
        capacity = self.calculate_capacity(snr_range)
        plt.plot(snr_range, capacity, 'b-', linewidth=2, label=f'MIMO {self.n_tx}x{self.n_rx}')
        
        # Capacité SISO pour comparaison
        capacity_siso = np.log2(1 + 10**(snr_range/10))
        plt.plot(snr_range, capacity_siso, 'r--', linewidth=2, label='SISO')
        
        plt.xlabel('SNR (dB)')
        plt.ylabel('Capacité (bits/s/Hz)')
        plt.title('Capacité du Canal MIMO vs SISO')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 2. Nombre de condition
        plt.subplot(3, 3, 2)
        cond_numbers = self.calculate_condition_number()
        plt.hist(cond_numbers, bins=30, alpha=0.7, color='green', edgecolor='black')
        plt.xlabel('Nombre de Condition')
        plt.ylabel('Fréquence')
        plt.title('Distribution du Nombre de Condition')
        plt.grid(True, alpha=0.3)
        
        # 3. Valeurs propres
        plt.subplot(3, 3, 3)
        eigenvals = self.calculate_eigenvalues()
        for i in range(min(self.n_rx, 5)):  # Afficher max 5 valeurs propres
            plt.plot(eigenvals[:, i], label=f'λ_{i+1}', alpha=0.7)
        plt.xlabel('Indice de sous-porteuse')
        plt.ylabel('Valeur propre')
        plt.title('Valeurs Propres par Sous-porteuse')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 4. Performances BER QPSK
        plt.subplot(3, 3, 4)
        ber_siso_qpsk, ber_mimo_qpsk = self.calculate_ber_performance(snr_range, 'qpsk')
        plt.semilogy(snr_range, ber_siso_qpsk, 'r--', label='SISO QPSK', linewidth=2)
        plt.semilogy(snr_range, ber_mimo_qpsk, 'b-', label=f'MIMO {self.n_tx}x{self.n_rx} QPSK', linewidth=2)
        plt.xlabel('SNR (dB)')
        plt.ylabel('BER')
        plt.title('Performances BER - QPSK')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 5. Réponse fréquentielle du canal
        plt.subplot(3, 3, 5)
        H_freq_response = np.abs(self.channel_matrix[0, 0, :])  # Premier lien
        plt.plot(np.arange(self.n_subcarriers), 20*np.log10(H_freq_response), 'purple', linewidth=2)
        plt.xlabel('Indice de sous-porteuse')
        plt.ylabel('|H| (dB)')
        plt.title('Réponse Fréquentielle du Canal (lien 1,1)')
        plt.grid(True, alpha=0.3)
        
        # 6. Corrélation spatiale
        plt.subplot(3, 3, 6)
        # Matrice de corrélation entre antennes
        H_flat = self.channel_matrix.reshape(self.n_rx * self.n_tx, self.n_subcarriers)
        corr_matrix = np.corrcoef(H_flat)
        
        im = plt.imshow(np.abs(corr_matrix), cmap='viridis', interpolation='nearest')
        plt.colorbar(im)
        plt.title('Matrice de Corrélation Spatiale')
        plt.xlabel('Index Antenne')
        plt.ylabel('Index Antenne')
        
        # 7. Distribution des gains du canal
        plt.subplot(3, 3, 7)
        channel_gains = 20 * np.log10(np.abs(self.channel_matrix.flatten()))
        plt.hist(channel_gains, bins=50, alpha=0.7, color='orange', edgecolor='black')
        plt.xlabel('Gain du Canal (dB)')
        plt.ylabel('Fréquence')
        plt.title('Distribution des Gains du Canal')
        plt.grid(True, alpha=0.3)
        
        # 8. Comparaison des modulations
        plt.subplot(3, 3, 8)
        snr_comp = np.arange(0, 25, 2)
        _, ber_qpsk = self.calculate_ber_performance(snr_comp, 'qpsk')
        _, ber_16qam = self.calculate_ber_performance(snr_comp, '16qam')
        _, ber_64qam = self.calculate_ber_performance(snr_comp, '64qam')
        
        plt.semilogy(snr_comp, ber_qpsk, 'b-', label='QPSK', linewidth=2)
        plt.semilogy(snr_comp, ber_16qam, 'g-', label='16-QAM', linewidth=2)
        plt.semilogy(snr_comp, ber_64qam, 'r-', label='64-QAM', linewidth=2)
        plt.xlabel('SNR (dB)')
        plt.ylabel('BER')
        plt.title('Comparaison des Modulations MIMO')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # 9. Efficacité spectrale
        plt.subplot(3, 3, 9)
        spectral_efficiency = capacity * np.log2(4)  # Pour QPSK
        plt.plot(snr_range, spectral_efficiency, 'darkblue', linewidth=3)
        plt.xlabel('SNR (dB)')
        plt.ylabel('Efficacité Spectrale (bits/s/Hz)')
        plt.title('Efficacité Spectrale MIMO')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.suptitle(f'Analyse des Performances MIMO {self.n_tx}x{self.n_rx} - {self.n_subcarriers} sous-porteuses', 
                     fontsize=16, y=0.98)
        plt.show()
        
        # Statistiques de performance
        self.print_performance_stats(snr_range, capacity)
    
    def print_performance_stats(self, snr_range, capacity):
        """Affiche les statistiques de performance"""
        print("\n" + "="*80)
        print(f"RAPPORT DE PERFORMANCE MIMO {self.n_tx}x{self.n_rx}")
        print("="*80)
        
        print(f"\n📊 CONFIGURATION SYSTÈME:")
        print(f"   • Antennes TX: {self.n_tx}")
        print(f"   • Antennes RX: {self.n_rx}")
        print(f"   • Sous-porteuses: {self.n_subcarriers}")
        print(f"   • Type de canal: Rayleigh Fading")
        
        # Capacité
        print(f"\n📡 CAPACITÉ DU CANAL:")
        idx_20db = np.argmin(np.abs(snr_range - 20))
        print(f"   • Capacité à 20 dB: {capacity[idx_20db]:.2f} bits/s/Hz")
        print(f"   • Capacité maximale: {np.max(capacity):.2f} bits/s/Hz")
        print(f"   • Gain MIMO théorique: {min(self.n_tx, self.n_rx)}x")
        
        # Condition du canal
        cond_numbers = self.calculate_condition_number()
        print(f"\n🔧 CONDITION DU CANAL:")
        print(f"   • Nombre de condition moyen: {np.mean(cond_numbers):.2f}")
        print(f"   • Nombre de condition max: {np.max(cond_numbers):.2f}")
        print(f"   • Écart-type: {np.std(cond_numbers):.2f}")
        
        # Valeurs propres
        eigenvals = self.calculate_eigenvalues()
        print(f"\n🎯 VALEURS PROPRES:")
        mean_eigenvals = np.mean(eigenvals, axis=0)
        for i, val in enumerate(mean_eigenvals):
            print(f"   • λ_{i+1} moyen: {val:.3f}")
        
        # Diversité
        diversity_gain = np.var(np.abs(self.channel_matrix.flatten()))
        print(f"\n🌟 DIVERSITÉ:")
        print(f"   • Gain de diversité (variance): {diversity_gain:.3f}")
        print(f"   • Ordre de diversité max: {self.n_tx * self.n_rx}")
        
        print("\n" + "="*80)

def main():
    """Fonction principale pour démontrer l'analyse MIMO"""
    
    print("🚀 DÉMARRAGE DE L'ANALYSE DES PERFORMANCES MIMO")
    print("="*60)
    
    # Configuration de base
    configurations = [
        (2, 2, 64),   # 2x2 MIMO
        (4, 4, 64),   # 4x4 MIMO
        (8, 8, 64),   # 8x8 MIMO
    ]
    
    # Types de canaux à tester
    channel_types = ['rayleigh', 'rician', 'awgn']
    
    for config in configurations:
        n_tx, n_rx, n_sc = config
        print(f"\n🔍 ANALYSE CONFIGURATION {n_tx}x{n_rx} MIMO")
        print("-" * 40)
        
        # Initialiser l'analyseur
        analyzer = MIMOPerformanceAnalyzer(n_tx, n_rx, n_sc)
        
        # Générer le canal (Rayleigh par défaut)
        analyzer.generate_channel_matrix('rayleigh')
        
        # Afficher les performances
        analyzer.plot_performance_metrics()
        
        # Pause entre les configurations
        if config != configurations[-1]:
            input("\nAppuyez sur Entrée pour continuer vers la configuration suivante...")
    
    print("\n✅ ANALYSE TERMINÉE")
    print("Les graphiques montrent les performances détaillées de chaque configuration MIMO.")

if __name__ == "__main__":
    main()