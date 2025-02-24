; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Sk Engine Pro"
#define MyAppVersion "3.4.7"
#define MyAppPublisher "My Company, Inc."
#define MyAppURL "https://www.example.com/"
#define MyAppExeName "mainPro.exe"
#define MyAppAssocName "Engine Pro SK"
#define MyAppAssocExt ".exe"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{7D160EDE-44F3-4F31-A55F-AAC74A4ECE1A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=Engine Pro\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
LicenseFile=C:\Users\Admin\Documents\code\Engine Pro\licenceprojet.txt
InfoBeforeFile=C:\Users\Admin\Documents\code\Engine Pro\licenceprojet.txt
InfoAfterFile=C:\Users\Admin\Documents\code\Engine Pro\afterprojet.txt
; Uncomment the following line to run in non administrative install mode (install for current user only).
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename=mysetup
SetupIconFile=C:\Users\Admin\Documents\code\Engine Pro\images\logochess.ico
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "arabic"; MessagesFile: "compiler:Languages\Arabic.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Admin\Documents\code\Engine Pro\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\stockfish\stockfish-windows-x86-64-sse41-popcnt.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\py\enginepro.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\py\hook.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\py\piecespro.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\black-bishop.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\black-king.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\black-knight.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\black-pawn.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\black-queen.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\black-rook.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\icon.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\logochess.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\logochess.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\resized_icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\resized_icon.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\white-bishop.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\white-king.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\white-knight.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\white-pawn.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\white-queen.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Admin\Documents\code\Engine Pro\images\white-rook.png"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

