#include <linux/kernel.h>
#include <linux/errno.h>
#include <linux/init.h>
#include <linux/module.h>
#include <linux/platform_device.h>
#include <linux/moduleparam.h>
#include <linux/delay.h>
#include <linux/input.h>



#define DRIVER_DESC "Virtual keyboard simulating a physical keyboard"
#define DRIVER_AUTHOR "<anis.chali1@outlook.com>"


struct virt_keyboard {
    struct input_dev *input;
};






static int virt_kbd_probe(struct platform_device *pdev)
{
	struct device *dev = &pdev->dev;
	struct virt_keyboard *kbd = NULL;
	struct input_dev *input = NULL;
	int err = 0;

	
	kbd = devm_kzalloc(dev, sizeof(struct virt_keyboard), GFP_KERNEL);
	if (!kbd)
		return -ENOMEM;
	
	input = input_allocate_device();
	if (!input)
		return -ENOMEM;
	
	input->name = "virt_keyboard";
	input->id.bustype = BUS_VIRTUAL;
	input->phys = "virt_keyboard/vinput0";
	input->dev.parent = NULL;

	__set_bit(EV_KEY, input->evbit);
	__set_bit(KEY_DOWN, input->keybit);

	kbd->input = input;

	err = input_register_device(kbd->input);
	if (err) {
		input_free_device(kbd->input);
		kbd->input = NULL;
		return err;
	}
	
	platform_set_drvdata(pdev, kbd);
	printk("Virtual keyboard probed...\n");
	return 0;
}

static int virt_kbd_remove(struct platform_device *pdev)
{
	struct virt_keyboard *kbd = platform_get_drvdata(pdev);

	if (kbd->input) {
		input_unregister_device(kbd->input);
		kbd->input = NULL;
	}
	printk("Virtual keyboard removed...\n");

	return 0;
}


static struct platform_driver virt_kbd_driver = {
	.driver = {
		.name = "virtual_keyboard",
	},
	.probe = virt_kbd_probe,
	.remove = virt_kbd_remove
};



/*
static int __init virt_keyboard_init(void)
{
	platform_driver_probe(&virt_kbd_driver, virt_kbd_probe);	
	return 0;
}

static void __exit virt_keyboard_exit(void)
{
	
}

module_init(virt_keyboard_init);
module_exit(virt_keyboard_exit);
*/

module_platform_driver_probe(virt_kbd_driver, virt_kbd_probe);
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION(DRIVER_DESC);
MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_ALIAS("platform:virtual-keyboard");
