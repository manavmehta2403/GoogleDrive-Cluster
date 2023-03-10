

#include<stdio.h>

#include<string.h>

#define BUFSIZE 32

int main(int argc, char **argv)

{

            char *buffer;

            buffer = (char *)malloc(sizeof(char)*BUFSIZE);

            strcpy(buffer, argv[1]);
			
           printf("%p",buffer);
           printf(buffer);
		
}
