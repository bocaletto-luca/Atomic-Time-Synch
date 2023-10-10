# Atomic Time Synch

**Author**: Bocaletto Luca  
**Website**: [https://www.elektronoide.it](https://www.elektronoide.it)  
**License**: GPLv3

## Overview

Atomic Time Synch is a Python application that allows you to synchronize your system time with an atomic time source using the Network Time Protocol (NTP). It provides both manual and automatic time synchronization options and allows you to choose from different NTP servers.

## Features

- Manually update the system time.
- Automatically synchronize the system time at specified intervals.
- Choose from a list of NTP servers for time synchronization.
- Display both atomic time and local time.

## Installation

To run Atomic Time Synch, you need to have Python and PyQt5 installed. You can install PyQt5 using the following command:

pip install PyQt5

# Usage

1. Run the application by executing `AtomicTimeSynch.py`.
2. The main window will appear with options for manual and automatic time synchronization.
3. Click the "Update Time" button to manually update the system time.
4. Choose an NTP server from the drop-down list and set the synchronization interval in seconds.
5. Click the "Start Automatic Update" button to start automatic synchronization.
6. To stop automatic synchronization, click the "Stop Automatic Update" button.
7. You can also update the system time with the "Sync System Time" button.

## Code Structure

The application is built using PyQt5 and consists of the following components:

- `AtomicTimeApp`: The main application window.
- `get_atomic_time()`: Function to retrieve atomic time from an NTP server.
- `get_local_time()`: Function to get the current local time.
- `sync_system_time_with_ntp()`: Function to synchronize the system time with an NTP server.

# README Italiano
# Atomic Time Synch

**Autore**: Bocaletto Luca  
**Sito Web**: [https://www.elektronoide.it](https://www.elektronoide.it)  
**Licenza**: GPLv3

## Panoramica

Atomic Time Synch è un'applicazione Python che consente di sincronizzare l'orario del sistema con una fonte di tempo atomico utilizzando il Protocollo di Tempo di Rete (NTP). Fornisce opzioni di sincronizzazione temporale sia manuali che automatiche e consente di scegliere tra diversi server NTP.

## Funzionalità

- Aggiornamento manuale dell'orario di sistema.
- Sincronizzazione automatica dell'orario di sistema a intervalli specificati.
- Scelta da un elenco di server NTP per la sincronizzazione dell'orario.
- Visualizzazione dell'orario atomico e dell'orario locale.

## Installazione

Per eseguire Atomic Time Synch, è necessario avere Python e PyQt5 installati. Puoi installare PyQt5 usando il seguente comando:

```bash
pip install PyQt5
