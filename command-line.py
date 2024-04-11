import logging
import sys
import json

class CommandLineAndLogging:
    def do_some_logging(self, config_data):
        logging.info(config_data["aNumber"])
        logging.info(config_data["aString"])

if __name__ == "__main__":  
    ## Get the configuration file 
    configFileLocation = sys.argv[1]  
    print("Configuration file location: {0}".format(configFileLocation))   
    configFile = open(configFileLocation)
    configFileJSON = json.load(configFile)

    ## Setup logging
    logging.basicConfig(filename=configFileJSON["logFileLocation"],
        format="%(asctime)s %(levelname)s:%(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        encoding="utf-8",
        level=logging.DEBUG)

    cmd_logging = CommandLineAndLogging()
    cmd_logging.do_some_logging(configFileJSON)