## Core1 (.NET Core)

## Frame1 (.NET Framework)
* Edit Frame1.csproj
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net472</TargetFramework>
    <PlatformTarget>AnyCPU</PlatformTarget>
    <DebugType>portable</DebugType>
  </PropertyGroup>
* Edit launch.json
        {
            "name": ".NET Framework Launch",
            "type": "clr",
            "program": "${workspaceFolder}/bin/Debug/net472/Frame1.exe",
        },
        {
            "name": ".NET Framework Attach",
            "type": "clr",
        }
* https://github.com/OmniSharp/omnisharp-vscode/wiki/Desktop-.NET-Framework
* https://stackoverflow.com/questions/47707095/visual-studio-code-for-net-framework
* https://docs.microsoft.com/en-us/dotnet/standard/frameworks

## Java1 (Java)
* Generate .classpath & .project using Eclipse
* Edit settings.json
"java.home": "c:\\to\\java\\jdk08"

## Python1 (Python)
* read a.bat

## VC1 (Visual C++ x64)
* Easy C++
* Edit build.bat
call "c:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" x64

## WSL1 (GCC in WSL)
* Easy C++
