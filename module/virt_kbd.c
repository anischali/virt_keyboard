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

static ssize_t store_key(struct device *dev, struct device_attribute *attr,
			  const char *buf, size_t len)
{
	int err = 0;
	unsigned long key = 0;

	err = kstrtoul(buf, 0, &key);
	if (err)
		return err;

	dev_info(dev, "you tapped key: %lu", key);

	return len;
}



static DEVICE_ATTR(key, S_IWUSR, NULL, store_key);

static struct attribute *virt_keyboard_attrs[] = {
	&dev_attr_key.attr,
	NULL
};

static const struct attribute_group virt_keyboard_attr_group = {
	.attrs	= virt_keyboard_attrs,
};

static int virt_kbd_probe(struct platform_device *pdev)
{
	struct virt_keyboard *kbd = NULL;
	struct input_dev *input = NULL;
	int err = 0;

	
	kbd = devm_kzalloc(&pdev->dev, sizeof(struct virt_keyboard), GFP_KERNEL);
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
	if (err)
	{
		dev_err(&pdev->dev,
			"Failed to register input device: %d\n", err);
		goto input_err;
	}

	err = sysfs_create_group(&pdev->dev.kobj,
				 &virt_keyboard_attr_group);
	if (err) {
		dev_err(&pdev->dev,
			"Failed to create attribute group: %d\n", err);
		goto input_err;
	}

	platform_set_drvdata(pdev, kbd);
	
	dev_info(&pdev->dev, 
		"Virtual keyboard successfully probed...\n");
	
	return 0;

input_err:
	input_free_device(kbd->input);
	kbd->input = NULL;

	return err;
}

static int virt_kbd_remove(struct platform_device *pdev)
{
	struct virt_keyboard *kbd = platform_get_drvdata(pdev);

	if (kbd->input) {
		input_unregister_device(kbd->input);
		kbd->input = NULL;
	}

	sysfs_remove_group(&pdev->dev.kobj,
				 &virt_keyboard_attr_group);

	dev_info(&pdev->dev, 
		"Virtual keyboard successfully removed...\n");
	return 0;
}


static const struct of_device_id id_table[] = {
	{ .name = "virt-keyboard" },
	{},
};

static struct platform_driver virt_kbd_driver = {
	.driver = {
		.name = "virtual_keyboard",
		.of_match_table = id_table,
	},
	.probe = virt_kbd_probe,
	.remove = virt_kbd_remove
};


module_platform_driver(virt_kbd_driver);
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION(DRIVER_DESC);
MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_ALIAS("platform:virt-keyboard");
