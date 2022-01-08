Any process holding this privilege can impersonate (but not create) any token for which it is able to gethandle.
You can get a privileged token from a Windows service (DCOM) making it perform an NTLM authentication against the exploit, then execute a process as SYSTEM.
Exploit it with [juicy-potatato](https://github.com/ohpe/juicy-potato)
