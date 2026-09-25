# Local File Organizer

A command-line utility built in Python that automates the sorting of cluttered directories by categorizing files into subfolders based on their extensions.

## Features
* **Automated Categorization:** Scans target directories and maps file extensions to logical folders (e.g., `Images`, `Documents`, `Executables`).
* **Dependency-Free:** Built entirely using Python's standard library (`os`, `shutil`, `sys`) to ensure lightweight, secure execution without external bloat.
* **Idempotent Operations:** Safely skips existing folders and handles duplicate file names without crashing or overwriting user data.
* **Edge Case Handling:** Automatically isolates system files and files without extensions into an "Uncategorized" directory.

## Getting Started

### Prerequisites
* Python 3.8 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/local-file-organizer.git](https://github.com/yourusername/local-file-organizer.git)