all : test.so

%.so : %.c
	$(CC) -shared -o $@ -fPIC $<
