<p align="center">
  <img src="res/logo-header.svg" alt="RustDesk - 您的远程桌面"><br>
  <a href="#免费的公共服务器">服务器</a> •
  <a href="#构建步骤">编译</a> •
  <a href="#文件结构">结构</a> •
  <a href="#截图">截图</a>
</p>

> [!CAUTION]
> **免责声明:** <br>
> RustDesk 的开发人员不纵容或支持任何不道德或非法的软件使用行为。滥用行为，例如未经授权的访问、控制或侵犯隐私，严格违反我们的准则。作者对应用程序的任何滥用行为概不负责。

与我们交流: [知乎](https://www.zhihu.com/people/rustdesk) | [Discord](https://discord.gg/nDceKgxnkV) | [Reddit](https://www.reddit.com/r/rustdesk) | [YouTube](https://www.youtube.com/@rustdesk)

远程桌面软件，开箱即用，无需任何配置。您完全掌控数据，不用担心安全问题。您可以使用我们的注册/中继服务器，
或者[自己设置](https://rustdesk.com/server)，
亦或者[开发您的版本](https://github.com/rustdesk/rustdesk-server-demo)。

![image](https://user-images.githubusercontent.com/71636191/171661982-430285f0-2e12-4b1d-9957-4a58e375304d.png)

RustDesk 期待各位的贡献. 如何参与开发? 详情请看 [CONTRIBUTING.md](CONTRIBUTING.md).

[**FAQ**](https://github.com/rustdesk/rustdesk/wiki/FAQ)

[**BINARY DOWNLOAD**](https://github.com/rustdesk/rustdesk/releases)

[**NIGHTLY BUILD**](https://github.com/rustdesk/rustdesk/releases/tag/nightly)

> [!IMPORTANT]
> **当前支持平台:** <br>
> 本项目目前专注于 **Windows** 和 **Android** 平台的维护与开发。其他平台的支持已移除以简化 CI/CD 和代码库维护。

## 构建步骤

本项目主要使用 Flutter 进行 UI 开发。

### 准备工作

- 请准备好 Rust 开发环境和 C++ 编译环境。
- 安装 [vcpkg](https://github.com/microsoft/vcpkg), 正确设置 `VCPKG_ROOT` 环境变量。

### Windows 构建

1. 安装依赖:
   ```powershell
   vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
   ```
2. 运行构建脚本:
   ```powershell
   python3 build.py --flutter
   ```

### Android 构建

请参考 `flutter/` 目录下的构建脚本，或在 GitHub Actions 中查看 `flutter-build.yml` 的步骤。主要的构建逻辑位于 `flutter/build_android.sh`。

## 文件结构

- **[libs/hbb_common](https://github.com/rustdesk/rustdesk/tree/master/libs/hbb_common)**: 视频编解码, 配置, tcp/udp 封装, protobuf, 文件传输相关文件系统操作函数, 以及一些其他实用函数
- **[libs/scrap](https://github.com/rustdesk/rustdesk/tree/master/libs/scrap)**: 屏幕截取
- **[libs/enigo](https://github.com/rustdesk/rustdesk/tree/master/libs/enigo)**: 平台相关的鼠标键盘输入
- **[libs/clipboard](https://github.com/rustdesk/rustdesk/tree/master/libs/clipboard)**: Windows、Android 的文本/文件剪切板实现
- **[src/server](https://github.com/rustdesk/rustdesk/tree/master/src/server)**: 被控端服务音频、剪切板、输入、视频服务、网络连接的实现
- **[src/client.rs](https://github.com/rustdesk/rustdesk/tree/master/src/client.rs)**: 控制端
- **[src/rendezvous_mediator.rs](https://github.com/rustdesk/rustdesk/tree/master/src/rendezvous_mediator.rs)**: 与[rustdesk-server](https://github.com/rustdesk/rustdesk-server)保持UDP通讯, 等待远程连接（通过打洞直连或者中继）
- **[src/platform](https://github.com/rustdesk/rustdesk/tree/master/src/platform)**: 平台服务相关代码
- **[flutter](https://github.com/rustdesk/rustdesk/tree/master/flutter)**: 适用于桌面(Windows)和移动设备(Android)的 Flutter 代码

## 截图

![image](https://user-images.githubusercontent.com/71636191/113112362-ae4deb80-923b-11eb-957d-ff88daad4f06.png)

![image](https://user-images.githubusercontent.com/71636191/113112619-f705a480-923b-11eb-911d-97e984ef52b6.png)
