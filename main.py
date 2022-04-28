import machine
from modules.manager import managing

machine.freq(240000000)
print(machine.freq())

managing()
