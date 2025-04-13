# Set Android SDK path
$androidSdkPath = "C:\Users\vg541\AppData\Local\Android\Sdk"

# Set ANDROID_HOME
[System.Environment]::SetEnvironmentVariable('ANDROID_HOME', $androidSdkPath, 'User')
Write-Host "Set ANDROID_HOME to: $androidSdkPath"

# Set ANDROID_SDK_ROOT
[System.Environment]::SetEnvironmentVariable('ANDROID_SDK_ROOT', $androidSdkPath, 'User')
Write-Host "Set ANDROID_SDK_ROOT to: $androidSdkPath"

# Add Android SDK tools and Git to PATH
$pathsToAdd = @(
    "$androidSdkPath\platform-tools",
    "$androidSdkPath\tools",
    "$androidSdkPath\tools\bin",
    "$androidSdkPath\build-tools\36.0.0",
    "C:\Program Files\Git\cmd",
    "C:\Program Files\Git\bin",
    "C:\Program Files\Git\mingw64\bin"
)

$userPath = [System.Environment]::GetEnvironmentVariable('Path', 'User')
$pathArray = $userPath.Split(';')

foreach ($path in $pathsToAdd) {
    if ($pathArray -notcontains $path) {
        $userPath = "$userPath;$path"
        Write-Host "Added to PATH: $path"
    }
}

[System.Environment]::SetEnvironmentVariable('Path', $userPath, 'User')
Write-Host "Environment variables have been updated successfully!"

# Configure Git if not already configured
$gitExe = "C:\Program Files\Git\cmd\git.exe"
& $gitExe config --global --get user.name
if ($LASTEXITCODE -ne 0) {
    & $gitExe config --global user.name "WhatsApp Scheduler"
    & $gitExe config --global user.email "whatsappscheduler@example.com"
    Write-Host "Configured Git user settings"
}
