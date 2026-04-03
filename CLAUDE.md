# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 在此存储库中工作时提供指导。

## 开发命令

### 构建命令
- `cargo run` - 构建并运行桌面应用程序（需要 libsciter 库）
- `python3 build.py --flutter` - 构建 Flutter 版本（桌面端）
- `python3 build.py --flutter --release` - 以发布模式构建 Flutter 版本
- `python3 build.py --hwcodec` - 构建硬件编解码器支持
- `python3 build.py --vram` - 构建 VRAM 功能（仅限 Windows）
- `cargo build --release` - 以发布模式构建 Rust 二进制文件
- `cargo build --features hwcodec` - 构建特定功能

### Flutter 移动端命令
- `cd flutter && flutter build android` - 构建 Android APK
- `cd flutter && flutter build ios` - 构建 iOS 应用
- `cd flutter && flutter run` - 以开发模式运行 Flutter 应用
- `cd flutter && flutter test` - 运行 Flutter 测试

### 测试
- `cargo test` - 运行 Rust 测试
- `cd flutter && flutter test` - 运行 Flutter 测试

### 平台特定构建脚本
- `flutter/build_android.sh` - Android 构建脚本
- `flutter/build_ios.sh` - iOS 构建脚本
- `flutter/build_fdroid.sh` - F-Droid 构建脚本

## 项目架构

### 目录结构
- **`src/`** - 主要 Rust 应用程序代码
  - `src/ui/` - 旧版 Sciter UI（已弃用，请改用 Flutter）
  - `src/server/` - 音频/剪贴板/输入/视频服务和网络连接
  - `src/client.rs` - 对等连接处理
  - `src/platform/` - 平台特定代码
- **`flutter/`** - 适用于桌面和移动端的 Flutter UI 代码
- **`libs/`** - 核心库
  - `libs/hbb_common/` - 视频编解码器、配置、网络封装、protobuf、文件传输工具
  - `libs/scrap/` - 屏幕捕获功能
  - `libs/enigo/` - 平台特定键盘/鼠标控制
  - `libs/clipboard/` - 跨平台剪贴板实现

### 关键组件
- **远程桌面协议**：在 `src/rendezvous_mediator.rs` 中实现的自定义协议，用于与 rustdesk-server 通信
- **屏幕捕获**：`libs/scrap/` 中的平台特定屏幕捕获
- **输入处理**：`libs/enigo/` 中的跨平台输入模拟
- **音视频服务**：`src/server/` 中的实时音视频流
- **文件传输**：`libs/hbb_common/` 中的安全文件传输实现

### UI 架构
- **旧版 UI**：基于 Sciter（已弃用） - 文件位于 `src/ui/`
- **现代 UI**：基于 Flutter - 文件位于 `flutter/`
  - 桌面端：`flutter/lib/desktop/`
  - 移动端：`flutter/lib/mobile/`
  - 共享：`flutter/lib/common/` 和 `flutter/lib/models/`

## 重要构建说明

### 依赖项
- C++ 依赖项需要 vcpkg：`libvpx`、`libyuv`、`opus`、`aom`
- 设置 `VCPKG_ROOT` 环境变量
- 下载适用于旧版 UI 支持的 Sciter 库

### 忽略模式
处理文件时，请忽略这些目录：
- `target/` - Rust 构建产物
- `flutter/build/` - Flutter 构建输出
- `flutter/.dart_tool/` - Flutter 工具文件

### 跨平台注意事项
- Windows 构建需要额外的 DLL 和虚拟显示驱动程序
- macOS 构建需要进行签名和公证才能发布
- Linux 构建支持多种包格式（deb、rpm、AppImage）
- 移动端构建需要平台特定的工具链（Android SDK, Xcode）

### 功能标志
- `hwcodec` - 硬件视频编码/解码
- `vram` - VRAM 优化（仅限 Windows）
- `flutter` - 启用 Flutter UI
- `unix-file-copy-paste` - Unix 文件剪贴板支持
- `screencapturekit` - macOS ScreenCaptureKit（仅限 macOS）

### 配置
所有配置或选项都在 `libs/hbb_common/src/config.rs` 文件中，分为 4 种类型：
- Settings（设置）
- Local（本地）
- Display（显示）
- Built-in（内置）
