# Spell Checker

## Overview

The Spell Checker project is an industrial-oriented application that identifies and corrects spelling errors in text. This project leverages efficient data structures and algorithms to provide fast and accurate spell-checking capabilities.

## Features

- **Efficient Word Storage:** Uses a Trie data structure to store and lookup words quickly.
- **Error Detection:** Detects misspelled words using a Trie and Levenshtein distance algorithm.
- **Error Correction:** Provides suggestions for misspelled words based on edit distance.
- **Simple GUI:** Includes a Tkinter-based GUI for user-friendly interaction with the spell checker.

## Project Structure

```plaintext
spell_checker/
│
├── spell_checker.py       # Main file with spell checker logic
├── trie.py                # Trie data structure implementation
├── edit_distance.py       # Edit distance calculation
├── corrections.py         # Error correction logic
├── gui_spell_checker.py   # Tkinter-based GUI for spell checker
└── dictionary.txt         # Dictionary file with valid words
```

## Getting Started

### Prerequisites

    Python 3.x: Ensure Python 3.x is installed on your system.
    Tkinter: This is required for the GUI. It comes pre-installed with most Python distributions.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Aryan-Gupta2003/Spell_Checker.git
   ```

2. **Prepare the dictionary**:

   The dictionary.txt file should contain a list of correctly spelled words, one word per line.
   You can use a publicly available word list or create your own.

### Running the Spell Checker

1. **Command-Line Interface (CLI)**
   You can run the spell checker in the command line using the following command:

   ```bash
   python spell_checker.py
   ```

   - Enter text to check when prompted.
   - The spell checker will output whether the words are spelled correctly and provide suggestions for misspelled words.

2. Graphical User Interface (GUI)
   To use the Tkinter-based GUI, run:

   ```bash
   python gui_spell_checker.py
   ```

   - A window will open where you can input text, check spelling, and view results.

## Acknowledgements

- The Levenshtein distance algorithm implementation is adapted for use in the error correction module.
- Tkinter is used for building the GUI.

## Contribution

Contributions are welcome! If you have any ideas or improvements, feel free to submit a pull request or open an issue.
