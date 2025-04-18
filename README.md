# ESP32 AI Chat

一个基于ESP32的AI聊天程序，可以通过Web界面或串口与AI进行对话。

## 功能特点

- 支持通过Web界面与AI聊天
- 支持通过串口与AI聊天
- 使用mDNS实现友好的主机名访问
- 使用LittleFS文件系统存储Web界面文件
- 支持WiFi站点模式和AP模式

## 硬件要求

- ESP32开发板
- USB数据线

## 软件依赖

- Arduino框架
- ArduinoJson库
- LittleFS_esp32库

## 安装步骤

1. 克隆或下载本仓库
2. 使用PlatformIO打开项目
3. 在`include/config.h`文件中配置WiFi和API设置
4. 编译并上传代码到ESP32
5. 上传文件系统镜像到ESP32

## 上传文件系统镜像

上传文件系统镜像是必要的步骤，否则Web界面将无法正常工作。有以下几种方法可以上传文件系统镜像：

### 方法1：使用PlatformIO界面

1. 在PlatformIO侧边栏中，展开您的项目
2. 点击"Platform"
3. 找到并点击"Upload Filesystem Image"任务

### 方法2：使用命令行

```
pio run --target uploadfs
```

### 方法3：使用自定义任务

1. 在PlatformIO侧边栏中，展开您的项目
2. 点击"Custom"
3. 找到并点击"Upload LittleFS Image"任务

## 使用方法

### Web界面访问

1. 连接到ESP32的WiFi网络（AP模式）或将ESP32连接到您的WiFi网络（站点模式）
2. 在浏览器中访问：
   - `http://esp32-ai-chat.local`（使用mDNS）
   - 或ESP32的IP地址

### 串口访问

1. 打开串口监视器（波特率115200）
2. 输入消息并按回车键发送
3. 查看AI的回复

## 配置选项

所有配置选项都在`include/config.h`文件中：

- WiFi设置（SSID和密码）
- AP模式设置（SSID和密码）
- Web服务器端口
- mDNS主机名
- API设置（服务器、端口、密钥和模型）

## 文件系统结构

- `/data/index.html` - 主Web界面
- `/data/fallback.html` - 备用Web界面（当主界面不可用时使用）

## 故障排除

- 如果Web界面无法访问，请确保已上传文件系统镜像
- 如果mDNS不工作，请尝试使用IP地址访问
- 如果串口没有输出，请检查波特率设置和USB连接

## 许可证

[MIT](LICENSE)
