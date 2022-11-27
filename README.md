# Malwation-Tasks

Hey everyone,

Let me explain what Ghidra is:

Ghidra is a software reverse engineering (SRE) framework created and maintained by the National Security Agency Research Directorate.
This framework includes a suite of full-featured, high-end software analysis tools that enable users to analyze compiled code on a variety of platforms including Windows, macOS, and Linux.
Capabilities include disassembly, assembly, decompilation, graphing, and scripting

I have written a code for decompiling elf, exe files to make it more productive. The goal of this code is picking a file and use it through Ghidra APIs.

First of all, i used Ghidra API called (pyhidra) library to call the functions from our specific file. 

You need to make a bridge connection between Pyhton and Ghidra API to be used.


You need to make a few steps to run this code

1. You need to set the path of ghidra directory
2. You need to enable the plugins from ghidra main.

here is the repository of the library [pyhidra](https://github.com/dod-cyber-crime-center/pyhidra) 

follow the steps.







