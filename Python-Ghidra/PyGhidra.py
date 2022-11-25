import pyhidra
import sys
import argparse
from os.path import exists


def existfile(file):
   return(exists(file))

def showfuncAddress(file, address):
    print("\n------List the function with the address------\n")
    with pyhidra.open_program(file) as api:
        from ghidra.app.decompiler.flatapi import FlatDecompilerAPI
        flat_decompiler = FlatDecompilerAPI(api)
        decompile = flat_decompiler.decompile(api.getFunction(flat_decompiler.ToAddr(address)))
        print(decompile)

def showandDecompile(file):
    print("\n-------List all the functions and decompile it--------\n")
    with pyhidra.open_program(file) as api:
        from ghidra.app.decompiler.flatapi import FlatDecompilerAPI
        program = api.getCurrentProgram() # start the program
        fm = program.getFunctionManager() # start the function manager
        fx = fm.getFunctions(True) # gets all the function
        for func in fx:
            print("{}".format(func.getName())) # print the functiom
            flat_decompiler = FlatDecompilerAPI(api) # decompile the functions
            decompile = flat_decompiler.decompile(api.getFunction(func.getName())) #Return the name of this function
            try:
                print(decompile)
            except ghidra.program.model.pcode.Decoder.clear():
                print("Error has occured")
                
            

def showFunctions(file):
    print("\n---------List all the functions------------\n")
    with pyhidra.open_program(file) as api: # open the program
        program = api.getCurrentProgram() # the program has been started
        fm = program.getFunctionManager()
        fx = fm.getFunctions(True)
        for function in fx:
            print("{}".format(function.getSignature())) # print the functions
    exit(0)
    
def ShowAddress(file, address):
    print("\n------Address with the function------\n")
    with pyhidra.open_program(file) as api:
        from ghidra.app.decompiler.flatapi import FlatDecompilerAPI
        decompile_address = FlatDecompilerAPI(api)
        decompile = decompile_address.decompile(api.getFunctionAt(api.toAddr(address)))
        print(decompile)
                
                
        
def main():
    print("Welcome to ghidra with the help of python")
    pars = argparse.ArgumentParser()
    pars.add_argument("--file", help="file name", required=True)
    pars.add_argument("--addr", help="Address of a function", required=False)
    pars.add_argument("--laf", help="List all the functions", required=False,action="store_true")
    pars.add_argument("--lafd", help="List all the functions and decompile it", required=False, action="store_true")
    pars.add_argument("--lfa", help="address with the function", required=False, action="store_true")
    args = pars.parse_args()
    if(len(sys.argv) < 2):
        args.print_help()
        exit(0)
    if(existfile):
        pyhidra.start()
    if(args.laf):
        showFunctions(args.file)
    if(args.addr):
        ShowAddress(args.file, args.addr) # put the address and it will find.
    if(args.lafd):
        showandDecompile(args.file)

        
if __name__ == "__main__":
    main()
