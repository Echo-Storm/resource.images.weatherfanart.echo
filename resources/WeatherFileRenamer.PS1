# Rename all files inside each subdirectory to <folder>-000.jpg, <folder>-001.jpg, etc.

Get-ChildItem -Directory | ForEach-Object {
    $folder = $_.Name
    $files = Get-ChildItem $_.FullName -File | Sort-Object Name

    $i = 0
    foreach ($file in $files) {
        $newName = "{0}-{1:000}{2}" -f $folder, $i, $file.Extension
        $newPath = Join-Path $file.DirectoryName $newName
        Rename-Item -LiteralPath $file.FullName -NewName $newName
        $i++
    }
}
