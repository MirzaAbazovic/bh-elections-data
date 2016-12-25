# $MyVariable = "https://www.izbori.ba/cik_web_api/race9_electoralunitpartyresult/%22WebResult_2016MUNI_2016_9_23_16_38_25#%22/50/1"
$vjece = "https://www.izbori.ba/cik_web_api/race9_electoralunitpartyresult/%22WebResult_2016MUNI_2016_9_23_16_38_25%22/"
For ($i=1; $i -le 5; $i++) {
	$url = $vjece+$i+"/1" 
	Write-Host $url
	#$build_info = $web_client.DownloadString($url) | ConvertFrom-Json
	$build_info=Invoke-RestMethod -Uri $url
	#$build_info
	wget $url -O $i"-vjece.json"
	#Invoke-WebRequest $url | ConvertFrom-Json | select *
	#Write-Host $J
	$a = Get-Content $i"-vjece.json" -raw | ConvertFrom-Json
	$a
	$a | ConvertTo-Json  | set-content 'mytestBis.json'
	}