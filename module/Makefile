obj-m:=virt_kbd.o virt_kbd_dev.o


KDIR?="/usr/src/linux-headers-$(shell uname -r)"

SRC:=$(shell pwd)

all:
	$(MAKE) -C $(KDIR) M=$(SRC) modules

clean:
	rm -f *.o *~ core .depend .*.cmd *.ko *.mod.c *.mod
	rm -f Module.markers Module.symvers modules.order
	rm -rf .tmp_versions Modules.symvers