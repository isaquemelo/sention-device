from modules.storage import get_kvs
import machine
from modules.manager import managing

machine.freq(240000000)

get_kvs().wipe()
managing()
