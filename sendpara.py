import os
import sys
path1 = os.path.abspath(os.path.dirname(os.getcwd()))

from getopt import getopt
from toolstouse.log_handle import ConsoleLogger
from toolstouse.config_handle import readConfig, writeConfig

log = ConsoleLogger()
configPath = os.path.abspath(__file__)+"/../config/env.ini"


def paramsRec(argv):
    if len(argv) == 0:
        log.error("input error")
        sys.exit(0)
    opts, args = getopt(argv[1:], '-r:-c:-e:-p:')  #rate,ck,pk,e
    dict1 = {}
    for opt_name, opt_value in opts:
        dict1[opt_name] = opt_value
    for opt_name, opt_value in opts:
        if opt_name == '-r':
            rate = opt_value
            writeConfig("differential_rate","differential_rate",rate)
            log.info(f"choose comparison rate:{rate}")
        elif opt_name == '-c':
            cmckey = opt_value
            writeConfig("cmc_key", "cmcapikey", cmckey)
            log.info(f"cmc key:{cmckey}")
        elif opt_name == '-e':
            env = opt_value
            res = "Basic " + dict1["-p"]
            writeConfig("env", "enginekey", res)
            if env == "dev":
                dev_env = readConfig("dev","priceengine")
                writeConfig("env","url",dev_env)
                log.info(f"choose env:{dev_env}")
                log.info(f"choose key:{res}")
            elif env == "stag":
                stag_env = readConfig("stag","priceengine")
                writeConfig("env","url",stag_env)
                log.info(f"choose env:{stag_env}")
                log.info(f"choose key:{res}")
            elif env == "prod":
                prod_env = readConfig("prod","priceengine")
                writeConfig("env","url",prod_env)
                log.info(f"choose env:{prod_env}")
                log.info(f"choose key:{res}")

subcommand = sys.argv[1]
paramsRec(sys.argv[0:])
