# Atomic Time Synch

**Author:** Bocaletto Luca

**Language:** Python

**License**: GPLv3

## Overview

Atomic Time Synch is a Python application that allows you to synchronize your system time with an atomic time source using the Network Time Protocol (NTP). It provides both manual and automatic time synchronization options and allows you to choose from different NTP servers.

![Screenshot 2023-10-10 084823](https://github.com/elektronoide/Atomic-Time-Synch/assets/134635227/265a98a6-43d5-45ed-85d5-63d40659576c)

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

---

**Note**: Ensure that you have installed all the necessary dependencies before running the application.

**Maintainer Update**

My current GitHub account is **@bocaletto-luca**, which is now the official maintainer of all projects previously published under the **@Elektronoide** account. Please direct any issues, pull requests, or stars to **@bocaletto-luca** for future updates.

---
