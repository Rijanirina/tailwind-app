#!/usr/bin/env python3
"""
Démonstration simplifiée des performances MIMO
Version légère pour test rapide
"""

import numpy as np
import matplotlib.pyplot as plt

def demo_mimo_simple():
    """Démonstration simple des performances MIMO"""
    
    print("🚀 DÉMONSTRATION SIMPLE MIMO")
    print("="*40)
    
    # Configuration
    n_tx, n_rx = 4, 4
    n_subcarriers = 64
    snr_range = np.arange(-10, 30, 2)
    
    print(f"Configuration: {n_tx}x{n_rx} MIMO, {n_subcarriers} sous-porteuses")
    
    # Génération du canal Rayleigh
    print("Génération du canal Rayleigh...")
    h_real = np.random.randn(n_rx, n_tx, n_subcarriers)
    h_imag = np.random.randn(n_rx, n_tx, n_subcarriers)
    H = (h_real + 1j * h_imag) / np.sqrt(2)
    
    # Calcul de la capacité
    print("Calcul de la capacité...")
    snr_linear = 10**(snr_range / 10)
    capacity_mimo = []
    capacity_siso = []
    
    for snr in snr_linear:
        # Capacité MIMO
        cap_sc = []
        for sc in range(n_subcarriers):
            H_sc = H[:, :, sc]
            I = np.eye(n_rx)
            HH_hermitian = H_sc @ H_sc.conj().T
            cap = np.log2(np.real(np.linalg.det(I + (snr/n_tx) * HH_hermitian)))
            cap_sc.append(cap)
        capacity_mimo.append(np.mean(cap_sc))
        
        # Capacité SISO pour comparaison
        capacity_siso.append(np.log2(1 + snr))
    
    # Visualisation
    print("Génération des graphiques...")
    plt.figure(figsize=(15, 10))
    
    # 1. Capacité
    plt.subplot(2, 2, 1)
    plt.plot(snr_range, capacity_mimo, 'b-', linewidth=3, label=f'MIMO {n_tx}x{n_rx}')
    plt.plot(snr_range, capacity_siso, 'r--', linewidth=2, label='SISO')
    plt.xlabel('SNR (dB)')
    plt.ylabel('Capacité (bits/s/Hz)')
    plt.title('Capacité du Canal MIMO vs SISO')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 2. Gain du canal
    plt.subplot(2, 2, 2)
    channel_gains_db = 20 * np.log10(np.abs(H.flatten()))
    plt.hist(channel_gains_db, bins=50, alpha=0.7, color='green', edgecolor='black')
    plt.xlabel('Gain du Canal (dB)')
    plt.ylabel('Fréquence')
    plt.title('Distribution des Gains du Canal')
    plt.grid(True, alpha=0.3)
    
    # 3. Réponse fréquentielle
    plt.subplot(2, 2, 3)
    H_freq = np.abs(H[0, 0, :])  # Premier lien
    plt.plot(20*np.log10(H_freq), 'purple', linewidth=2)
    plt.xlabel('Indice de sous-porteuse')
    plt.ylabel('|H| (dB)')
    plt.title('Réponse Fréquentielle')
    plt.grid(True, alpha=0.3)
    
    # 4. Valeurs propres moyennes
    plt.subplot(2, 2, 4)
    eigenvals_mean = []
    for sc in range(n_subcarriers):
        H_sc = H[:, :, sc]
        HH = H_sc @ H_sc.conj().T
        eigs = np.real(np.linalg.eigvals(HH))
        eigenvals_mean.append(eigs)
    eigenvals_mean = np.array(eigenvals_mean)
    
    for i in range(min(n_rx, 4)):
        plt.plot(eigenvals_mean[:, i], label=f'λ_{i+1}', alpha=0.8)
    plt.xlabel('Sous-porteuse')
    plt.ylabel('Valeur propre')
    plt.title('Valeurs Propres')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.suptitle(f'Performances MIMO {n_tx}x{n_rx} - Démonstration Simplifiée', 
                 fontsize=14, y=0.98)
    plt.show()
    
    # Statistiques
    print("\n📊 RÉSULTATS:")
    print(f"• Capacité max MIMO: {max(capacity_mimo):.2f} bits/s/Hz")
    print(f"• Capacité max SISO: {max(capacity_siso):.2f} bits/s/Hz")
    print(f"• Gain MIMO: {max(capacity_mimo)/max(capacity_siso):.2f}x")
    print(f"• Gain théorique: {min(n_tx, n_rx)}x")
    
    # Condition du canal
    cond_numbers = []
    for sc in range(n_subcarriers):
        cond_numbers.append(np.linalg.cond(H[:, :, sc]))
    
    print(f"• Condition moyenne: {np.mean(cond_numbers):.2f}")
    print(f"• Variance des gains: {np.var(np.abs(H)):.3f}")
    
    print("\n✅ Démonstration terminée!")

if __name__ == "__main__":
    demo_mimo_simple()