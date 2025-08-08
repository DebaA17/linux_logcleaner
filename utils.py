import os

def is_root():
    """Return True if running as root, else False."""
    return os.geteuid() == 0


def get_log_files(is_root_user):
    """Return list of log files based on privilege."""
    if is_root_user:
        return [
            '/var/log/syslog',
            '/var/log/messages',
            '/var/log/auth.log',
            '/var/log/wtmp',
            '/var/log/btmp',
            '/var/log/lastlog',
        ]
    else:
        home = os.path.expanduser('~')
        return [
            os.path.join(home, '.bash_history'),
            os.path.join(home, '.zsh_history'),
            os.path.join(home, '.local', 'share', 'recently-used.xbel'),
        ]


def clean_file(file_path):
    """Attempt to clean the file, handling errors gracefully."""
    try:
        if not os.path.exists(file_path):
            print_status(file_path, missing=True)
            return
        with open(file_path, 'w') as f:
            f.truncate(0)
        print_status(file_path, cleaned=True)
    except PermissionError:
        print_status(file_path, permission=True)
    except Exception as e:
        print_status(file_path, error=str(e))


def print_status(file_path, dry_run=False, cleaned=False, missing=False, permission=False, error=None):
    if dry_run:
        print(f"[DRY RUN] Would clean: {file_path}")
    elif cleaned:
        print(f"[OK] Cleaned: {file_path}")
    elif missing:
        print(f"[SKIP] Missing: {file_path}")
    elif permission:
        print(f"[ERROR] Permission denied: {file_path}")
    elif error:
        print(f"[ERROR] {file_path}: {error}")
