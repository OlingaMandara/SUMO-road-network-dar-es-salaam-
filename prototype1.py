import os
import sys
import optparse

if 'SUMO_HOME' in os.environ:
    tools=os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append (tools)


    else:
        sys.exit ("please declare environment variable 'SUMO_HOME'")


        from sumolib import checkBinary
        import traci

        def get_options():
            opt_parser= optparse.OptionParser()
            opt_parser.add_option("--nogui", action="store true",
            default=False, help="run the command line version of sumo")

            options, args= opt_parser.parse_args()

            def run():

     
                step = 0
                while traci.simulation.getMinExpectedNumber() > 0:
                    traci.simulationStep