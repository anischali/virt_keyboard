#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/io.h>
#include <linux/string.h>
#include <linux/moduleparam.h>
#include <linux/platform_device.h>
#include <linux/input.h>

#define DRIVER_DESC "Virtual keyboard simulating a physical keyboard"
#define DRIVER_AUTHOR "<anis.chali1@outlook.com>"



static struct platform_device virt_keyboard_dev = {
	.name		= "virt-keyboard",
	.id = 0,
    .dev = {
		.platform_data		= NULL,
	},
};

static struct platform_device *keyboard_devices[] __initdata = {
	&virt_keyboard_dev,
};

static int keyboard_devices_init(void)
{
	return platform_add_devices(keyboard_devices, ARRAY_SIZE(keyboard_devices));
}
module_init(keyboard_devices_init);


MODULE_LICENSE("GPL");
MODULE_DESCRIPTION(DRIVER_DESC);
MODULE_AUTHOR(DRIVER_AUTHOR);
