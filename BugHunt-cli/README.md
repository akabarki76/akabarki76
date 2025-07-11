# BugHunt-cli

BugHunt-cli is an AI-powered command-line interface (CLI) designed to assist with penetration testing and bug hunting. It provides a suite of tools to automate common tasks, identify vulnerabilities, and promote ethical hacking practices.

**Note:** This project is under active development. Features and commands may change.

## Disclaimer

This tool is for educational and authorized security testing purposes only. Unauthorized scanning of systems is illegal. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/BugHunt-cli.git
    cd BugHunt-cli
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Activate the virtual environment:
```bash
source .venv/bin/activate
```

Then, run the `main.py` script with the desired arguments:

```bash
python3 main.py --target <target> [--ports <port1> <port2> ...] [--scan-vulns] [--recon] [--report]
```

**Examples:**

*   **Basic port scan:**
    ```bash
    python3 main.py --target example.com --ports 80 443
    ```

*   **Vulnerability scan and report:**
    ```bash
    python3 main.py --target example.com --scan-vulns --report
    ```

*   **Reconnaissance scan:**
    ```bash
    python3 main.py --target example.com --recon
    ```

