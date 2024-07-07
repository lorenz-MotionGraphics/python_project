[Setup]
AppName=YourAppName
AppVersion=1.0
DefaultDirName={pf}\YourAppName
DefaultGroupName=YourAppName
OutputDir=.
OutputBaseFilename=YourAppSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Path\To\Your\Python\Executable\python.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Path\To\Your\Python\Scripts\Scripts\*"; DestDir: "{app}\Scripts"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Path\To\Your\Application\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\YourAppName"; Filename: "{app}\python.exe"; Parameters: """{app}\YourMainScript.py"""

[Run]
Filename: "{app}\python.exe"; Parameters: """{app}\YourMainScript.py"""; Description: "Launch YourAppName"; Flags: nowait postinstall skipifsilent
