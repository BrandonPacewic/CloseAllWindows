# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

"""
WARNING: This script will terminate all processes in the TERMINATE_LIST.
"""

import os

TERMINATE_LIST = [
    "chrome.exe",
    "spotify.exe",
    "Code.exe",
    "Discord.exe",
]

def main():
    [os.system(f"taskkill /f /im {process}") for process in TERMINATE_LIST]


if __name__ == "__main__":
    main()
