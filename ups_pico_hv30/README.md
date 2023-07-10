# Home Assistant Add-on: UPS Pico HV3.0 FSSD

Enable daemon for UPS Pico notifications and system shutdown.

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

## About

This addon implements the Pi Modules Hat UPS Pico safe shutdown system.

When a power cut occurs and the set time elapses, it triggers a safe shutdown of the system, protecting the data from possible corruption and, if it is configured, it will send an email with a notification of the event.

**Important: this addon is designed for gpio-used firmware**

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-no-red.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-no-red.svg
