#!/usr/bin/env python3
"""
Check file numbering in weatherfanart folders.
Verifies sequential naming with no gaps or duplicates.

Supports both formats:
  - 000.jpg, 001.jpg, 002.jpg...
  - 0-000.jpg, 0-001.jpg, 0-002.jpg... (folder prefix)

Usage:
    python check_numbering.py E:\resource.images.weatherfanart.echo
"""

import os
import sys
import re
from pathlib import Path


def check_folder(folder_path):
    """Check numbering in a single folder. Returns (ok, issues)."""
    
    files = sorted(folder_path.glob('*.jpg'))
    
    if not files:
        return True, "empty"
    
    issues = []
    numbers = []
    folder_name = folder_path.name
    
    for f in files:
        # Try format: {folder}-{number}.jpg (e.g., 3-000.jpg, alert-005.jpg)
        match = re.match(rf'^{re.escape(folder_name)}-(\d+)\.jpg$', f.name)
        
        # Fallback: try format {number}.jpg (e.g., 000.jpg)
        if not match:
            match = re.match(r'^(\d+)\.jpg$', f.name)
        
        if not match:
            issues.append(f"bad name: {f.name}")
            continue
        
        num = int(match.group(1))
        numbers.append(num)
    
    if not numbers:
        if issues:
            return False, issues
        return True, "empty (no valid files)"
    
    # Check for duplicates
    seen = set()
    for n in numbers:
        if n in seen:
            issues.append(f"duplicate: {n:03d}")
        seen.add(n)
    
    # Check sequence starts at 0
    if min(numbers) != 0:
        issues.append(f"doesn't start at 000 (starts at {min(numbers):03d})")
    
    # Check for gaps
    expected = set(range(min(numbers), max(numbers) + 1))
    actual = set(numbers)
    gaps = expected - actual
    if gaps:
        gap_list = sorted(gaps)
        if len(gap_list) <= 5:
            issues.append(f"gaps: {', '.join(f'{g:03d}' for g in gap_list)}")
        else:
            issues.append(f"gaps: {len(gap_list)} missing ({gap_list[0]:03d}...{gap_list[-1]:03d})")
    
    if issues:
        return False, issues
    else:
        return True, f"{len(numbers)} files (000-{max(numbers):03d})"


def check_addon(addon_path):
    """Check all folders in the addon."""
    
    root = Path(addon_path)
    resources = root / 'resources'
    
    # Check if we're at addon root or resources folder
    if not resources.exists():
        if (root / '0').exists() or (root / 'na').exists():
            resources = root
        else:
            print(f"ERROR: Cannot find resources folder in {addon_path}")
            return False
    
    print(f"Checking: {resources}\n")
    
    # Get all subdirectories, sort numerics first then alpha
    folders = sorted([d for d in resources.iterdir() if d.is_dir()], 
                     key=lambda x: (not x.name.isdigit(), int(x.name) if x.name.isdigit() else 0, x.name))
    
    all_ok = True
    total_files = 0
    
    for folder in folders:
        ok, result = check_folder(folder)
        
        if ok:
            # Extract file count from result
            if "files" in str(result):
                count = int(result.split()[0])
                total_files += count
            print(f"[{folder.name}/] ✔ {result}")
        else:
            all_ok = False
            if isinstance(result, list):
                print(f"[{folder.name}/] ✗ {', '.join(result)}")
            else:
                print(f"[{folder.name}/] ✗ {result}")
    
    print(f"\n{'='*50}")
    if all_ok:
        print(f"✔ ALL FOLDERS OK — {total_files} files, sequential numbering verified")
    else:
        print("✗ ISSUES FOUND — see above")
    
    return all_ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_numbering.py <path_to_addon>")
        print("Example: python check_numbering.py E:\\resource.images.weatherfanart.echo")
        sys.exit(1)
    
    addon_path = sys.argv[1]
    success = check_addon(addon_path)
    sys.exit(0 if success else 1)
