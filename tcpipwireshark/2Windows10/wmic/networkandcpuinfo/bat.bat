@echo OFF
>test1.txt (
  echo Manufacturer Information:
  systeminfo|findstr /c:"Host Name" /c:"OS Name" /c:"System Model:" /c:"System Type:" /c:"Total Physical Memory:"

  echo(
  echo CPU Information:
  wmic cpu get Name /Format:list | more | findstr .
  wmic computersystem get NumberofProcessors /Format:list | more | findstr .

  echo(
  echo NIC Information:
  wmic nicconfig where IPEnabled=TRUE get ipaddress, macaddress,defaultipgateway /format:list | more | findstr .
)