#!/usr/bin/env python3
"""
Validate weather fanart images.
Checks all files in subdirectories are .jpg and exactly 1920x1080.
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("ERROR: Pillow not installed. Run: pip install Pillow")
    sys.exit(1)


def validate_folder(root_path):
    """Check all images in root_path subdirectories."""
    
    root = Path(root_path)
    
    if not root.exists():
        print(f"ERROR: Path does not exist: {root_path}")
        return False
    
    issues = []
    folders_checked = 0
    files_checked = 0
    
    # Get all subdirectories (condition folders)
    subdirs = sorted([d for d in root.iterdir() if d.is_dir()])
    
    # Filter to just the resources folder if we're at addon root
    resources = root / "resources"
    if resources.exists():
        subdirs = sorted([d for d in resources.iterdir() if d.is_dir()])
        print(f"Found resources/ folder, checking inside that.\n")
    
    for folder in subdirs:
        folders_checked += 1
        folder_issues = []
        
        files = list(folder.iterdir())
        
        for f in files:
            if f.is_dir():
                # Skip subdirectories within condition folders
                continue
                
            files_checked += 1
            
            # Check extension
            if f.suffix.lower() != '.jpg':
                folder_issues.append(f"  {f.name}: wrong extension ({f.suffix})")
                continue
            
            # Check dimensions
            try:
                with Image.open(f) as img:
                    width, height = img.size
                    if width != 1920 or height != 1080:
                        folder_issues.append(f"  {f.name}: wrong size ({width}x{height})")
            except Exception as e:
                folder_issues.append(f"  {f.name}: cannot read ({e})")
        
        if folder_issues:
            issues.append(f"\n[{folder.name}/] - {len(folder_issues)} issue(s):")
            issues.extend(folder_issues)
        else:
            print(f"[{folder.name}/] ✔ {len(files)} files OK")
    
    # Summary
    print(f"\n{'='*50}")
    print(f"Checked {files_checked} files in {folders_checked} folders")
    
    if issues:
        print(f"\n⚠ ISSUES FOUND:")
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"\n✔ ALL CLEAR - every file is .jpg at 1920x1080")
        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_fanart.py <path_to_addon_folder>")
        print("Example: python validate_fanart.py E:\\resource.images.weatherfanart.echo")
        sys.exit(1)
    
    path = sys.argv[1]
    success = validate_folder(path)
    sys.exit(0 if success else 1)
