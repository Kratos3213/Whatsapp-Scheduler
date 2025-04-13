# Function to test a command
function Test-Command {
    param($Command, $Description)
    Write-Host "`nTesting $Description..."
    try {
        $result = Invoke-Expression $Command
        Write-Host "✅ Success: $Description" -ForegroundColor Green
        return $true
    } catch {
        Write-Host "❌ Failed: $Description" -ForegroundColor Red
        Write-Host "Error: $_" -ForegroundColor Red
        return $false
    }
}

# Set paths
$androidSdk = "C:\Users\vg541\AppData\Local\Android\Sdk"
$gitPath = "C:\Program Files\Git"

# Clear and set environment variables
Write-Host "`nSetting environment variables..."

# Android SDK
[System.Environment]::SetEnvironmentVariable('ANDROID_HOME', $androidSdk, 'Process')
[System.Environment]::SetEnvironmentVariable('ANDROID_SDK_ROOT', $androidSdk, 'Process')
$env:ANDROID_HOME = $androidSdk
$env:ANDROID_SDK_ROOT = $androidSdk

# Add to PATH
$pathsToAdd = @(
    "$androidSdk\platform-tools",
    "$androidSdk\tools",
    "$androidSdk\tools\bin",
    "$androidSdk\build-tools\36.0.0",
    "$gitPath\cmd",
    "$gitPath\bin",
    "$gitPath\mingw64\bin"
)

$env:Path = ($env:Path.Split(';') + $pathsToAdd | Select-Object -Unique) -join ';'

# Verify setup
Write-Host "`nVerifying environment setup..."
Write-Host "ANDROID_HOME: $env:ANDROID_HOME"
Write-Host "ANDROID_SDK_ROOT: $env:ANDROID_SDK_ROOT"

# Test Git
$gitOk = Test-Command "git --version" "Git installation"

# Test Android SDK
$adbOk = Test-Command "adb --version" "Android Debug Bridge (ADB)"

# Test Python and Briefcase
$pythonOk = Test-Command "python --version" "Python installation"
$pipOk = Test-Command "pip --version" "Pip installation"
$briefcaseOk = Test-Command "python -m briefcase --version" "Briefcase installation"

# Summary
Write-Host "`nEnvironment Setup Summary:"
Write-Host "------------------------"
Write-Host "Git: $(if ($gitOk) {'✅'} else {'❌'})"
Write-Host "ADB: $(if ($adbOk) {'✅'} else {'❌'})"
Write-Host "Python: $(if ($pythonOk) {'✅'} else {'❌'})"
Write-Host "Pip: $(if ($pipOk) {'✅'} else {'❌'})"
Write-Host "Briefcase: $(if ($briefcaseOk) {'✅'} else {'❌'})"

# Save the environment variables permanently if all tests pass
if ($gitOk -and $adbOk -and $pythonOk -and $pipOk -and $briefcaseOk) {
    Write-Host "`nAll tests passed! Saving environment variables permanently..."
    [System.Environment]::SetEnvironmentVariable('ANDROID_HOME', $androidSdk, 'User')
    [System.Environment]::SetEnvironmentVariable('ANDROID_SDK_ROOT', $androidSdk, 'User')
    
    $userPath = [System.Environment]::GetEnvironmentVariable('Path', 'User')
    $newPath = ($userPath.Split(';') + $pathsToAdd | Select-Object -Unique) -join ';'
    [System.Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
    
    Write-Host "✅ Environment variables saved permanently" -ForegroundColor Green
} else {
    Write-Host "`n❌ Some tests failed. Please fix the issues before proceeding." -ForegroundColor Red
}
