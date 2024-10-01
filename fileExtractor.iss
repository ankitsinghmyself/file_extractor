[Setup]
AppName=File Extractor
AppVersion=1.0
DefaultDirName={pf}\File Extractor
DefaultGroupName=File Extractor
OutputDir=.
OutputBaseFilename=FileExtractorInstaller
Compression=lzma
SolidCompression=yes
UninstallDisplayIcon={app}\fileExtractor.ico  ; Path to the icon for the uninstaller
Uninstallable=yes

[Files]
Source: "file_extractor.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "fileExtractor.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\File Extractor"; Filename: "{app}\file_extractor.exe"
Name: "{group}\Uninstall File Extractor"; Filename: uninstall;
