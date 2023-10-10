# Software Name: Atomic Time Synch
# Author: Bocaletto Luca
# Site Web: https://www.elektronoide.it
# License: GPLv3

import sys
import ntplib
import subprocess
from datetime import datetime
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QComboBox

# Definizione della classe principale dell'applicazione
class AtomicTimeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atomic Time Synch")  # Imposta il titolo della finestra
        self.setGeometry(100, 100, 400, 250)  # Imposta la dimensione della finestra

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()  # Crea un layout principale per la finestra

        # Creazione e configurazione del Label per il titolo
        self.title_label = QLabel("Atomic Time Synch")  # Crea un Label per il titolo
        self.title_label.setStyleSheet("font-size: 20px; text-align: center;")  # Imposta la dimensione dei caratteri e l'allineamento
        self.layout.addWidget(self.title_label)

        # Creazione del pulsante per l'aggiornamento manuale
        self.update_button = QPushButton("Aggiorna Ora")
        self.update_button.setStyleSheet("font-size: 14px;")  # Imposta la dimensione dei caratteri
        self.update_button.clicked.connect(self.update_time)  # Collega il pulsante all'aggiornamento
        self.layout.addWidget(self.update_button)

        # Creazione e configurazione dei controlli per l'aggiornamento automatico
        self.ntp_label = QLabel("Seleziona un Server NTP:")
        self.ntp_label.setStyleSheet("font-size: 14px;")  # Imposta la dimensione dei caratteri
        self.layout.addWidget(self.ntp_label)

        self.ntp_combo = QComboBox()
        self.ntp_combo.addItem("pool.ntp.org", "pool.ntp.org")
        self.ntp_combo.addItem("time.nist.gov", "time.nist.gov")
        # Aggiungi altri server NTP qui
        self.layout.addWidget(self.ntp_combo)

        self.interval_label = QLabel("Seleziona Intervallo di Aggiornamento Automatico (secondi):")
        self.interval_label.setStyleSheet("font-size: 14px;")  # Imposta la dimensione dei caratteri
        self.layout.addWidget(self.interval_label)

        self.interval_combo = QComboBox()
        for seconds in range(1, 11):
            self.interval_combo.addItem(f"{seconds} secondi", seconds)
        self.layout.addWidget(self.interval_combo)

        self.start_auto_update_button = QPushButton("Avvia Aggiornamento Automatico")
        self.start_auto_update_button.setStyleSheet("font-size: 14px;")  # Imposta la dimensione dei caratteri
        self.start_auto_update_button.clicked.connect(self.start_auto_update)
        self.layout.addWidget(self.start_auto_update_button)

        self.stop_auto_update_button = QPushButton("Ferma Aggiornamento Automatico")
        self.stop_auto_update_button.setStyleSheet("font-size: 14px;")  # Imposta la dimensione dei caratteri
        self.stop_auto_update_button.clicked.connect(self.stop_auto_update)
        self.layout.addWidget(self.stop_auto_update_button)
        self.stop_auto_update_button.setEnabled(False)

        # Creazione del pulsante per l'aggiornamento dell'orario di sistema
        self.sync_system_time_button = QPushButton("Aggiorna Ora di Sistema")
        self.sync_system_time_button.setStyleSheet("font-size: 14px;")  # Imposta la dimensione dei caratteri
        self.sync_system_time_button.clicked.connect(self.sync_system_time)
        self.layout.addWidget(self.sync_system_time_button)

        # Creazione del Label per visualizzare l'orario
        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 16px;")  # Imposta la dimensione dei caratteri per l'orario
        self.layout.addWidget(self.time_label)

        # Impostazione del layout principale
        self.central_widget.setLayout(self.layout)

        self.timer = None  # Variabile per gestire il timer dell'aggiornamento automatico
        self.auto_update_enabled = False  # Flag per indicare se l'aggiornamento automatico è attivo

        self.update_time()  # Aggiorna l'orario iniziale

    # Funzione per aggiornare l'orario manualmente
    def update_time(self):
        try:
            atomic_time = get_atomic_time()  # Ottieni l'orario atomico
            self.time_label.setText(f"Ora Atomica: {atomic_time} -- Ora Locale: {get_local_time()}")
        except Exception as e:
            self.show_error_message(f"Errore: {e}")

    # Funzione per mostrare un messaggio di errore
    def show_error_message(self, error_message):
        # Implementa la finestra di errore qui (da fare)
        pass

    # Funzione per sincronizzare l'orario di sistema con un server NTP
    def sync_system_time(self):
        selected_ntp_server = self.ntp_combo.currentData()
        try:
            sync_system_time_with_ntp(selected_ntp_server)
            self.show_success_message("Orario del sistema aggiornato con successo.")
        except Exception as e:
            self.show_error_message(f"Errore nell'aggiornamento dell'orario del sistema: {e}")

    # Funzione per mostrare un messaggio di successo
    def show_success_message(self, message):
        # Implementa la finestra di successo qui (da fare)
        pass

    # Funzione per avviare l'aggiornamento automatico
    def start_auto_update(self):
        interval_seconds = self.interval_combo.currentData()
        if not self.auto_update_enabled:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_time)
            self.timer.start(interval_seconds * 1000)
            self.auto_update_enabled = True
            self.start_auto_update_button.setEnabled(False)
            self.stop_auto_update_button.setEnabled(True)

    # Funzione per fermare l'aggiornamento automatico
    def stop_auto_update(self):
        if self.auto_update_enabled:
            self.timer.stop()
            self.auto_update_enabled = False
            self.start_auto_update_button.setEnabled(True)
            self.stop_auto_update_button.setEnabled(False)

# Funzione per ottenere l'orario atomico da un server NTP
def get_atomic_time():
    try:
        c = ntplib.NTPClient()
        response = c.request('pool.ntp.org')
        atomic_time = datetime.fromtimestamp(response.tx_time)
        return atomic_time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise Exception("Impossibile recuperare l'orario atomico")

# Funzione per ottenere l'orario locale
def get_local_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Funzione per sincronizzare l'orario di sistema con un server NTP
def sync_system_time_with_ntp(ntp_server):
    try:
        subprocess.run(["w32tm", "/resync", "/rediscover", "/nowait"])
    except Exception as e:
        raise Exception("Impossibile sincronizzare l'orario del sistema")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AtomicTimeApp()
    window.show()
    sys.exit(app.exec_())
