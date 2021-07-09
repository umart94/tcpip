@echo OFF
>test2.txt (
  echo Manufacturer Information:
  systeminfo|findstr /c:"Host Name" /c:"OS Name" /c:"System Model:" /c:"System Type:" /c:"Total Physical Memory:"

  echo(
  echo CPU Information:
  call :wmic cpu get Name /Format:list
  call :wmic computersystem get NumberofProcessors /Format:list

  echo(
  echo NIC Information:
  call :wmic nicconfig where IPEnabled=TRUE get ipaddress, macaddress,defaultipgateway /format:list
)
exit /b

:wmic
wmic %* >test.tmp
type test.tmp | findstr .
del test.tmp
exit /b