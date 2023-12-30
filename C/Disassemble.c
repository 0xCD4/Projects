#include <stdlib.h>
#include <inttypes.h>
#include <stdio.h>
#include <capstone/capstone.h>

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_RESET   "\x1b[0m"

int main()
{
	csh handle; // API of capstone
	cs_insn *insn; // points to all memory
	size_t count; // count instructions
	if(cs_open(CS_ARCH_X86, CS_MODE_64, &handle) != CS_ERR_OK){
		fprintf(stderr, "Error initializing capstone\n");
	}
	FILE *file = fopen("register", "rb"); // change the file
	if(!file){
		 fprintf(stderr, "Error opening file\n");
		 cs_close(&handle);
		 return 1;
	}
	fseek(file,0,SEEK_END); // set position
	long int file_size = ftell(file); // size of the file
	rewind(file); // reset the file position

	unsigned char *buffer = malloc(file_size); // allocate the memory 
	fread(buffer, 1, file_size,file); // read 1 byte of file_size
	fclose(file); // close the file

	count = cs_disasm(handle, buffer, file_size, 0x1000, 0, &insn);
	if(count > 0){
		for(size_t i = 0; i<count;i++){
		 //	 printf("0x%" PRIx64 ":\t%s\t\t%s\n", insn[i].address, insn[i].mnemonic, insn[i].op_str);
			printf("0x%" PRIx64 ":\t" ANSI_COLOR_GREEN "%s\t\t" ANSI_COLOR_RED "%s" ANSI_COLOR_RESET "\n",
                   insn[i].address, insn[i].mnemonic, insn[i].op_str);
		}
		cs_free(insn, count);
	

	}else{
		fprintf(stderr,"failed to be disassembled");
	}
	// clean
	cs_close(&handle);
	free(buffer);
}
