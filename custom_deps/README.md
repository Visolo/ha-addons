# Home Assistant Add-on: Custom Deps

_Manage custom Python modules in Home Assistant deps._

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

This addon allows the installation of custom dependencies in the configuration directory, so they can be used by Home Assistant or some custom component.

## How to use

1- Install de addon
2- Configure the list of pip packages you want to install
3- If necessary configure the list of necessary apk packages
4- Run the addon. When finished the packages are installed.

**Important:** 
You only need to run the addon once and the pip packages will remain installed even if you update Home Assistant.
If you need to install any more packages, add them to the configuration list and run the addon again.
**El addon borra todos los paquetes instalados en cada ejecución**

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
