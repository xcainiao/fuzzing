#include <stdio.h>
#include <signal.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

char *buffer;

void copybuff(char *func)
{
	strcpy(buffer, func);	
}

void handler(int sig)
{
	char filename[256];
	int fd;
	printf("**************************************\n");
	sprintf(filename, "crash_%d_%p_%lu.py", sig, buffer, time(NULL));
	fd = open(filename, O_WRONLY | O_CREAT);
	write(fd, buffer, strlen(buffer));
}

void init()
{
	buffer = malloc(0x80000);
	signal(SIGSEGV, handler);
	printf("hello world\n");
} 
