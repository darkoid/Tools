Files required: ***fuzzer.py***, ***exploit.py***, ***bytearray.py***(to create all bad char - not needed as already added in exploit.py comment)

[fuzzer.py - run with *python3*](/fuzzer.py) || [exploit.py - run with *python* to reduce byte value problems with variable](/exploit.py) || [badchar.py - run with *python3*](/badchar.py)

First run [fuzzer.py](http://fuzzer.py) then `msf-pattern_create`. Add output to payload variable in [exploit.py](http://exploit.py) (let other variables be empty and `offset = 0`)

1. Now run [exploit.py](http://exploit.py) then copy **EIP** to get `offset` via `msf-pattern_offset`. Add the value to offset variable in [exploit.py](http://exploit.py) and uncomment payload with badchar value. Add “BBBB” to retn variable to check for **EIP** as 41414141.

2. Follow **ESP** in dump and note all bad char, make a note of them. You’ll see them in **pair** remove the first ones from [exploit.py](http://exploit.py) and retry to confirm if all bad char are removed.

> Now we have offset value and bad characters.

Lets exploit!
