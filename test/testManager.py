import sys
sys.path.append("../")

from utils.manager import Manager

if "__main__" == __name__:
    try:
        m = Manager()
        m.run()
    except KeyboardInterrupt: 
        exit()