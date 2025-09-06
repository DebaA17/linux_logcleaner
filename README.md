# Linux Log Cleaner Tool

## Description
A Python-based log cleaner for Linux systems. Intended for educational Red Team use only. Cleans system-wide or user-specific log files depending on privilege level.

## Disclaimer
**For educational purposes only. Do not use this tool for unauthorized or malicious activity. The author is not responsible for misuse.**


## OS Compatibility
- Tested on: **Linux** (Ubuntu, Debian, CentOS, Kali, etc.)
- Not compatible with Windows or macOS.

## Usage
### Python
```
python3 cleaner.py --wipe-all           # Wipe all logs (root: system-wide, non-root: user logs)
python3 cleaner.py --dry-run --wipe-all # Show which files would be cleaned
python3 cleaner.py --target /path/to/file # Clean a specific log file
```

### Bash Script
You can also use the provided bash wrapper:
```
chmod +x run_cleaner.sh
./run_cleaner.sh --wipe-all
./run_cleaner.sh --dry-run --wipe-all
./run_cleaner.sh --target /path/to/file
```

## Privilege Behavior
- **Root:** Cleans system-wide logs:
  - /var/log/syslog
  - /var/log/messages
  - /var/log/auth.log
  - /var/log/wtmp
  - /var/log/btmp
  - /var/log/lastlog
- **Non-root:** Cleans user logs:
  - ~/.bash_history
  - ~/.zsh_history
  - ~/.local/share/recently-used.xbel

## Output
- Prints status for each file (cleaned, missing, permission error)
- Handles missing files and permission errors gracefully
