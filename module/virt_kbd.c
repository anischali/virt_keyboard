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

static uint32_t keycode[] = {
    KEY_ESC,
    KEY_1,
    KEY_2,
    KEY_3,
    KEY_4,
    KEY_5,
    KEY_6,
    KEY_7,
    KEY_8,
    KEY_9,
    KEY_0,
    KEY_MINUS,
    KEY_EQUAL,
    KEY_BACKSPACE,
    KEY_TAB,
    KEY_Q,
    KEY_W,
    KEY_E,
    KEY_R,
    KEY_T,
    KEY_Y,
    KEY_U,
    KEY_I,
    KEY_O,
    KEY_P,
    KEY_LEFTBRACE,
    KEY_RIGHTBRACE,
    KEY_ENTER,
    KEY_LEFTCTRL,
    KEY_A,
    KEY_S,
    KEY_D,
    KEY_F,
    KEY_G,
    KEY_H,
    KEY_J,
    KEY_K,
    KEY_L,
    KEY_SEMICOLON,
    KEY_APOSTROPHE,
    KEY_GRAVE,
    KEY_LEFTSHIFT,
    KEY_BACKSLASH,
    KEY_Z,
    KEY_X,
    KEY_C,
    KEY_V,
    KEY_B,
    KEY_N,
    KEY_M,
    KEY_COMMA,
    KEY_DOT,
    KEY_SLASH,
    KEY_RIGHTSHIFT,
    KEY_KPASTERISK,
    KEY_LEFTALT,
    KEY_SPACE,
    KEY_CAPSLOCK,
    KEY_F1,
    KEY_F2,
    KEY_F3,
    KEY_F4,
    KEY_F5,
    KEY_F6,
    KEY_F7,
    KEY_F8,
    KEY_F9,
    KEY_F10,
    KEY_NUMLOCK,
    KEY_SCROLLLOCK,
    KEY_KP7,
    KEY_KP8,
    KEY_KP9,
    KEY_KPMINUS,
    KEY_KP4,
    KEY_KP5,
    KEY_KP6,
    KEY_KPPLUS,
    KEY_KP1,
    KEY_KP2,
    KEY_KP3,
    KEY_KP0,
    KEY_KPDOT,
    KEY_ZENKAKUHANKAKU,
    KEY_102ND,
    KEY_F11,
    KEY_F12,
    KEY_RO,
    KEY_KATAKANA,
    KEY_HIRAGANA,
    KEY_HENKAN,
    KEY_KATAKANAHIRAGANA,
    KEY_MUHENKAN,
    KEY_KPJPCOMMA,
    KEY_KPENTER,
    KEY_RIGHTCTRL,
    KEY_KPSLASH,
    KEY_SYSRQ,
    KEY_RIGHTALT,
    KEY_HOME,
    KEY_UP,
    KEY_PAGEUP,
    KEY_LEFT,
    KEY_RIGHT,
    KEY_END,
    KEY_DOWN,
    KEY_PAGEDOWN,
    KEY_INSERT,
    KEY_DELETE,
    KEY_MACRO,
    KEY_MUTE,
    KEY_VOLUMEDOWN,
    KEY_VOLUMEUP,
    KEY_POWER,
    KEY_KPEQUAL,
    KEY_KPPLUSMINUS,
    KEY_PAUSE,
    KEY_KPCOMMA,
    KEY_HANGUEL,
    KEY_HANJA,
    KEY_YEN,
    KEY_LEFTMETA,
    KEY_RIGHTMETA,
    KEY_COMPOSE,
    KEY_STOP,
    KEY_CALC,
    KEY_SETUP,
    KEY_SLEEP,
    KEY_WAKEUP,
    KEY_PROG1,
    KEY_SCREENLOCK,
    KEY_MAIL,
    KEY_BOOKMARKS,
    KEY_COMPUTER,
    KEY_BACK,
    KEY_FORWARD,
    KEY_EJECTCLOSECD,
    KEY_NEXTSONG,
    KEY_PLAYPAUSE,
    KEY_PREVIOUSSONG,
    KEY_STOPCD,
    KEY_HOMEPAGE,
    KEY_REFRESH,
    KEY_F13,
    KEY_F14,
    KEY_F15,
    KEY_F21,
    KEY_SUSPEND,
    KEY_CAMERA,
    KEY_EMAIL,
    KEY_SEARCH,
    KEY_BRIGHTNESSDOWN,
    KEY_BRIGHTNESSUP,
    KEY_MEDIA,
    KEY_SWITCHVIDEOMODE,
    KEY_BATTERY,
    KEY_UNKNOWN,
};

struct virt_keyboard {
    struct input_dev *input;
};

static ssize_t store_keydown(struct device *dev, struct device_attribute *attr,
			  const char *buf, size_t len)
{
	struct virt_keyboard *kbd = dev_get_drvdata(dev);
	int err = 0;
	unsigned long key = 0;

	err = kstrtoul(buf, 0, &key);
	if (err)
		return err;

	input_report_key(kbd->input, key, 1);
	input_sync(kbd->input);

	return len;
}

static ssize_t store_keyup(struct device *dev, struct device_attribute *attr,
			  const char *buf, size_t len)
{
	struct virt_keyboard *kbd = dev_get_drvdata(dev);
	int err = 0;
	unsigned long key = 0;

	err = kstrtoul(buf, 0, &key);
	if (err)
		return err;

	input_report_key(kbd->input, key, 0);
	input_sync(kbd->input);

	return len;
}


static DEVICE_ATTR(keydown, S_IWUSR, NULL, store_keydown);
static DEVICE_ATTR(keyup, S_IWUSR, NULL, store_keyup);

static struct attribute *virt_keyboard_attrs[] = {
	&dev_attr_keydown.attr,
	&dev_attr_keyup.attr,
	NULL
};

static const struct attribute_group virt_keyboard_attr_group = {
	.attrs	= virt_keyboard_attrs,
};

static void setup_keyboard_input(struct input_dev *input)
{
	int i;
	input->name = "virt_keyboard";
	input->id.bustype = BUS_VIRTUAL;
	input->phys = "virt_keyboard/vinput0";
	input->dev.parent = NULL;
	input->keycode = keycode;
	input->evbit[0] = BIT_MASK(EV_KEY) | BIT_MASK(EV_REP);
	input->keycodemax = ARRAY_SIZE(keycode);

	__set_bit(EV_MSC, input->evbit);
	__set_bit(MSC_SCAN, input->mscbit);
	__set_bit(EV_KEY, input->evbit);
	
	
	for (i = 0; i < ARRAY_SIZE(keycode); ++i)
		__set_bit(keycode[i], input->keybit);
	clear_bit(0, input->keybit);
}


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
	
	setup_keyboard_input(input);

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
		.name = "virt-keyboard",
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
