# feishu-setup

版本：0.9

这个 skill 用来帮 AI 助手或智能体接入飞书 / Lark。它只负责一件事：把 `lark-cli` 安装好、配置好、登录好，并确认 user / bot 身份都能正常使用。后续真正读写文档、Wiki、表格、Base、IM、日历或邮件时，再交给对应的 `lark-*` skill。

## 能做什么

- 安装 `@larksuite/cli`。
- 安装 `lark-cli` 自带的一组 `lark-*` skills。
- 安全配置 App ID 和 App Secret，避免把 secret 写进命令历史或代码仓库。
- 引导完成 OAuth device-flow 用户授权。
- 验证 bot 身份和 user 身份。
- 排查常见认证、权限、scope、资源未共享等问题。
- 在接入完成后，把具体飞书操作交给对应的 `lark-doc`、`lark-wiki`、`lark-sheets`、`lark-base`、`lark-im`、`lark-mail`、`lark-calendar` 等 skill。

## 安装方式

```bash
cd ~/.codex/skills
git clone https://github.com/raymonder/feishu-setup.git
```

安装后重启 Codex，或重新打开会话，让 skill metadata 被重新加载。

## 怎么使用

在对话里提出飞书接入、认证或 `lark-cli` 配置相关需求即可，例如：

```text
帮我接入飞书，配置 lark-cli。
```

```text
我有 Feishu App ID 和 App Secret，帮我完成授权。
```

```text
lark-cli auth status 显示没有登录用户，帮我排查。
```

## 依赖条件

- 已安装 Node.js 和 npm。
- 有一个飞书 / Lark 内部应用。
- 能拿到 App ID 和 App Secret。
- 应用已经添加目标资源需要的权限 scope。
- 有一个可以在目标租户里完成 OAuth 授权的用户。

## 主要限制

- 这个 skill 不负责接入完成后的具体飞书资源操作。文档、Wiki、表格、邮件、日历、IM、Base 等操作应使用对应的 `lark-*` skill。
- bot 只能访问明确授权或共享给应用的资源。
- user OAuth 只能获得当前登录用户本身拥有的权限。
- 无法绕过租户策略、缺失 scope、未发布应用版本或资源成员权限限制。
- App Secret、access token、refresh token、device code、verification URL 和本地配置文件都不能提交到仓库。
