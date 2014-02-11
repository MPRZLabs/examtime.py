pull:
	adb pull /sdcard/sl4a/scripts/examtime.py
	adb pull /sdcard/sl4a/examtime.sqlite

push:
	adb push examtime.py /sdcard/sl4a/scripts
	adb push examtime.sqlite /sdcard/sl4a
