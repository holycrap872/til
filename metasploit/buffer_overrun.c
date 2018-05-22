#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <errno.h>
#include <fcntl.h>

void
jump_esp() {
    __asm__ ("jmp *%esp;");
}

void
read_into_buffer(int fd)
{
    char buf[10];
    read(fd, buf, 1000);
}

int
main(int argc, char ** argv)
{
    if (argc != 2) {
        printf("usage: buffer_overrun $FILE\n");
        return 1;
    }

    int fd = open(argv[1], O_RDONLY);

    if (fd < 0) {
        printf("No such file\n");
        return 1;
    }

    read_into_buffer(fd);
    return 0;
}
