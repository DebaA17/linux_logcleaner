import os
import argparse
from utils import is_root, get_log_files, clean_file, print_status

def main():
    parser = argparse.ArgumentParser(description="Linux Log Cleaner Tool (Educational Red Team Use Only)")
    parser.add_argument('--dry-run', action='store_true', help='Show which files will be cleaned (no deletion)')
    parser.add_argument('--wipe-all', action='store_true', help='Wipe all relevant logs depending on user privilege')
    parser.add_argument('--target', type=str, help='Clean a specific log file')
    args = parser.parse_args()

    root = is_root()
    log_files = get_log_files(root)

    if args.target:
        files_to_clean = [os.path.expanduser(args.target)]
    elif args.wipe_all:
        files_to_clean = log_files
    else:
        parser.print_help()
        return

    for file_path in files_to_clean:
        if args.dry_run:
            print_status(file_path, dry_run=True)
        else:
            clean_file(file_path)

if __name__ == "__main__":
    main()
