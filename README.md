# 嵌入式开发学习笔记

这是一个使用 [Fumadocs](https://fumadocs.dev/) 构建的嵌入式开发学习笔记文档网站。

## 文档结构

```
content/
  ├── docs/
  │   ├── getting-started/        # 入门指南
  │   │   ├── environment.md      # 开发环境搭建
  │   │   └── basic-concepts.md   # 基本概念
  │   ├── hardware/              # 硬件相关
  │   │   ├── mcu/               # 微控制器
  │   │   ├── peripherals/       # 外设
  │   │   └── interfaces/        # 接口
  │   ├── software/              # 软件相关
  │   │   ├── rtos/             # 实时操作系统
  │   │   ├── drivers/          # 驱动程序
  │   │   └── protocols/        # 通信协议
  │   └── projects/             # 实践项目
  │       ├── led-control/      # LED控制
  │       └── sensor-reading/   # 传感器读取
```

## 开发指南

1. 安装依赖：

```bash
pnpm install
```

2. 启动开发服务器：

```bash
pnpm dev
```

3. 构建生产版本：

```bash
pnpm build
```

## 写作规范

1. 使用 Markdown 格式编写文档
2. 代码示例需要包含详细的注释
3. 每个文档都应该包含：
   - 标题
   - 简介
   - 正文内容
   - 相关资源链接
   - 实践练习（如果适用）

## 贡献指南

1. Fork 本仓库
2. 创建新的分支
3. 提交更改
4. 发起 Pull Request

## 许可证

MIT
