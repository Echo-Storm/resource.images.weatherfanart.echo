#!/usr/bin/env python3
"""
Delete clone folders from resource.images.weatherfanart.echo

Run AFTER deploying weather.kodiweather 2.4.2 which redirects
clone codes to master folders.

Usage:
    python delete_clone_folders.py E:\resource.images.weatherfanart.echo
    
Add --dry-run to preview without deleting:
    python delete_clone_folders.py E:\resource.images.weatherfanart.echo --dry-run
"""

import os
import sys
import shutil
from pathlib import Path

# Clone folders to delete (these redirect to master folders in weather addon)
CLONE_FOLDERS = [
    '4',   # -> 3 (Thunderstorms)
    '6',   # -> 5 (Mixed Rain and Sleet)
    '7',   # -> 5 (Mixed Snow and Sleet)
    '8',   # -> 5 (Freezing Drizzle)
    '10',  # -> 5 (Freezing Rain)
    '14',  # -> 13 (Light Snow Showers)
    '15',  # -> 13 (Blowing Snow)
    '16',  # -> 13 (Snow)
    '18',  # -> 5 (Sleet)
    '21',  # -> 20 (Haze)
    '24',  # -> 23 (Windy)
    '28',  # -> 26 (Mostly Cloudy Day)
    '29',  # -> 27 (Partly Cloudy Night)
    '30',  # -> 26 (Partly Cloudy Day)
    '33',  # -> 31 (Fair Night)
    '34',  # -> 32 (Fair Day)
    '35',  # -> 17 (Mixed Rain and Hail)
    '36',  # -> 32 (Hot)
    '37',  # -> 3 (Isolated Thunderstorms)
    '38',  # -> 3 (Scattered Thunderstorms Night)
    '39',  # -> 3 (Scattered Thunderstorms Day)
    '40',  # -> 12 (Scattered Showers)
    '41',  # -> 13 (Heavy Snow Night)
    '42',  # -> 13 (Scattered Snow Showers)
    '43',  # -> 13 (Heavy Snow Day)
    '44',  # -> 26 (Partly Cloudy)
    '45',  # -> 3 (Thundershowers)
    '46',  # -> 13 (Snow Showers)
    '47',  # -> 3 (Isolated Thundershowers)
]

# Master folders to KEEP (sanity check)
MASTER_FOLDERS = [
    '0',      # Tornado
    '1',      # Tropical Storm
    '2',      # Hurricane
    '3',      # Severe Thunderstorms (master)
    '5',      # Mixed Rain and Snow (master)
    '9',      # Drizzle
    '11',     # Light Showers Night
    '12',     # Heavy Showers Day (master)
    '13',     # Snow Flurries (master)
    '17',     # Hail (master)
    '19',     # Dust
    '20',     # Foggy (master)
    '22',     # Smoky
    '23',     # Blustery (master)
    '25',     # Cold
    '26',     # Cloudy (master)
    '27',     # Mostly Cloudy Night (master)
    '31',     # Clear Night (master)
    '32',     # Sunny (master)
    'na',     # Not Available
    'alert',  # Weather Alert
]


def delete_clones(addon_path, dry_run=False):
    """Delete clone folders from the addon."""
    
    root = Path(addon_path)
    resources = root / 'resources'
    
    # Check if we're at addon root or resources folder
    if not resources.exists():
        if (root / '0').exists():  # We're already in resources
            resources = root
        else:
            print(f"ERROR: Cannot find resources folder in {addon_path}")
            return False
    
    print(f"{'DRY RUN - ' if dry_run else ''}Processing: {resources}\n")
    
    deleted_count = 0
    deleted_files = 0
    deleted_bytes = 0
    
    for folder_name in CLONE_FOLDERS:
        folder_path = resources / folder_name
        
        if folder_path.exists():
            # Count files and size
            files = list(folder_path.glob('*'))
            file_count = len(files)
            folder_size = sum(f.stat().st_size for f in files if f.is_file())
            
            if dry_run:
                print(f"  Would delete: {folder_name}/ ({file_count} files, {folder_size / 1024 / 1024:.1f} MB)")
            else:
                shutil.rmtree(folder_path)
                print(f"  Deleted: {folder_name}/ ({file_count} files, {folder_size / 1024 / 1024:.1f} MB)")
            
            deleted_count += 1
            deleted_files += file_count
            deleted_bytes += folder_size
        else:
            print(f"  Skipped: {folder_name}/ (not found)")
    
    # Verify masters still exist
    print(f"\nVerifying master folders...")
    missing_masters = []
    for folder_name in MASTER_FOLDERS:
        folder_path = resources / folder_name
        if not folder_path.exists():
            missing_masters.append(folder_name)
    
    if missing_masters:
        print(f"  WARNING: Missing master folders: {', '.join(missing_masters)}")
    else:
        print(f"  All {len(MASTER_FOLDERS)} master folders present ✔")
    
    # Summary
    print(f"\n{'='*50}")
    if dry_run:
        print(f"DRY RUN COMPLETE")
        print(f"Would delete: {deleted_count} folders, {deleted_files} files")
        print(f"Would free: {deleted_bytes / 1024 / 1024 / 1024:.2f} GB")
        print(f"\nRun without --dry-run to actually delete.")
    else:
        print(f"DELETION COMPLETE")
        print(f"Deleted: {deleted_count} folders, {deleted_files} files")
        print(f"Freed: {deleted_bytes / 1024 / 1024 / 1024:.2f} GB")
    
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python delete_clone_folders.py <path_to_addon> [--dry-run]")
        print("Example: python delete_clone_folders.py E:\\resource.images.weatherfanart.echo")
        print("         python delete_clone_folders.py E:\\resource.images.weatherfanart.echo --dry-run")
        sys.exit(1)
    
    addon_path = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    
    if not dry_run:
        print("WARNING: This will permanently delete clone folders!")
        print("Run with --dry-run first to preview.")
        response = input("Continue? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted.")
            sys.exit(0)
    
    success = delete_clones(addon_path, dry_run)
    sys.exit(0 if success else 1)
