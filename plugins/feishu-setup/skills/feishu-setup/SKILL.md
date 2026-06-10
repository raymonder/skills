---
name: feishu-setup
version: "0.9"
description: Use when an agent needs to connect to Feishu/Lark, install or configure lark-cli, set app credentials, complete OAuth device-flow login, verify user or bot authentication, or troubleshoot lark-cli authentication errors before using lark-* skills.
---

# Feishu / Lark Setup

This skill only handles one job: get `lark-cli` installed, configured, authenticated, and verified so later Feishu/Lark work can be handled by the appropriate `lark-*` skill.

## Scope

Use this skill for:

- Installing `@larksuite/cli`.
- Installing the Lark CLI bundled agent skills.
- Configuring an app with App ID and App Secret.
- Completing user OAuth with device flow.
- Verifying `bot` and `user` identities.
- Troubleshooting authentication and permission setup errors.

Do not use this skill for actual Feishu resource operations after authentication is ready. Hand off to the relevant skill:

| User wants to do | Use |
| --- | --- |
| Read, create, or edit documents | `lark-doc` |
| Work with wiki spaces or nodes | `lark-wiki` |
| Work with Drive Markdown files | `lark-markdown` |
| Work with spreadsheets | `lark-sheets` |
| Work with Base / bitable | `lark-base` |
| Send or inspect IM messages | `lark-im` |
| Work with mail | `lark-mail` |
| Work with calendar events | `lark-calendar` |
| Work with contacts | `lark-contact` |

## Identity Model

Feishu/Lark Open API usually has two useful identities:

| Identity | Token | Access boundary | Use when |
| --- | --- | --- | --- |
| `bot` | tenant access token | Resources explicitly granted to the app | Server-side jobs and shared enterprise resources |
| `user` | user access token | The signed-in user's own permissions | Personal docs, personal wiki nodes, joined chats, most interactive work |

Default to `user` when unsure. A bot cannot read a document just because an app exists; the resource must be shared with the app or the API call will fail with a permission error.

## Setup Workflow

### 1. Install lark-cli

```bash
node --version
npm --version
npm install -g @larksuite/cli
lark-cli --version
```

If global npm install fails with an EACCES-style permissions error, use a user-level prefix:

```bash
mkdir -p "$HOME/.npm-global"
npm config set prefix "$HOME/.npm-global"
export PATH="$HOME/.npm-global/bin:$PATH"
npm install -g @larksuite/cli
```

### 2. Install the bundled lark skills

```bash
npx skills add larksuite/cli -y -g
```

After this step, the environment should expose skills such as `lark-doc`, `lark-wiki`, `lark-sheets`, `lark-base`, `lark-im`, and `lark-shared`. Exact install location depends on the agent runtime; do not assume a user-specific path.

### 3. Collect app credentials

Ask the user for:

- App ID.
- App Secret.
- Brand/domain preference: `feishu` for Feishu China, `lark` for Lark global, unless the user already knows which one they need.

If the user does not have an app yet, tell them to create an internal app in the Feishu/Lark developer console, copy the App ID and App Secret, add the scopes needed for their use case, then publish the app version.

Common scope groups:

```text
wiki:wiki / wiki:wiki:readonly / wiki:node:read / wiki:node:write
docx:document / docx:document:readonly
drive:drive / drive:drive:readonly
contact:user.id:readonly
```

Add mail, calendar, IM, or Base scopes only when needed. If a later API reports a missing scope, update the app permissions, publish a new app version, and re-authorize the user.

Security reminder to give the user: App Secret is an application credential. Do not paste it into public channels, logs, issues, pull requests, or files that may be committed.

### 4. Configure app credentials

Use stdin for the secret so it does not appear in the process list:

```bash
printf '%s' '<APP_SECRET>' | lark-cli config init \
  --app-id '<APP_ID>' \
  --app-secret-stdin \
  --brand feishu \
  --new \
  --lang zh
```

Use `--brand lark` instead when the workspace is on Lark global.

Verify bot configuration:

```bash
lark-cli auth status
```

Expected state after app configuration: app metadata is present and bot identity is available. If there is no logged-in user yet, continue to OAuth.

### 5. Complete user OAuth with device flow

Prefer the non-blocking device-flow pattern in agent sandboxes:

```bash
lark-cli auth login --no-wait --domain all --json
```

The command returns a `device_code` and a `verification_url`.

Agent behavior:

1. Show the full `verification_url` to the user.
2. Ask them to open it, authorize, and reply when finished.
3. After the user confirms, immediately run:

```bash
lark-cli auth login --device-code '<DEVICE_CODE>' --json
```

`--domain all` reduces repeat authorization prompts. If the user wants narrower access, use a domain subset such as:

```bash
lark-cli auth login --no-wait --domain wiki,docs,drive --json
```

### 6. Verify connection

```bash
lark-cli auth status
lark-cli api GET /open-apis/authen/v1/user_info --as user --jq '.data | {name, open_id}'
```

If the user-info call succeeds, setup is complete. Stop using this skill and hand off to the requested `lark-*` skill.

## Troubleshooting

### `lark-cli auth status` says not configured

App credentials are missing or the lark-cli config file is unavailable. Re-run `lark-cli config init`.

### Global npm install fails

Use a user-level npm prefix:

```bash
mkdir -p "$HOME/.npm-global"
npm config set prefix "$HOME/.npm-global"
export PATH="$HOME/.npm-global/bin:$PATH"
```

Then retry the install.

### Device code expired

Device codes are short-lived. Re-run `lark-cli auth login --no-wait ...` and use the new verification URL and device code.

### User authorized but token exchange still fails

Check:

- The device code has not expired.
- The user finished the authorization page rather than only opening it.
- The app config still exists in the current runtime.
- The app version containing requested scopes has been published.

### API returns wiki or document permission denied

If the command used `--as bot`, retry with `--as user`. If bot access is required, share the target resource with the app or grant the app membership in the appropriate resource.

### API returns missing scope or permission denied

Read the `permission_violations` or error details, add the missing scope in the developer console, publish a new version, then repeat user OAuth.

## Safety Rules

- Never commit App Secret, access tokens, refresh tokens, device codes, verification URLs, config files, or API responses containing private data.
- Do not write token-bearing files into a project directory.
- Do not pass secrets with `--app-secret <value>`; use `--app-secret-stdin`.
- Treat OAuth verification URLs as sensitive while active.
- Avoid persistent logs that include customer data or API payloads.
- If access is no longer needed, recommend disabling the app or revoking authorization in the developer console.

## References

- Feishu developer console: `https://open.feishu.cn/app`
- Feishu/Lark Open Platform: `https://open.feishu.cn`
- lark-cli repository: `https://github.com/larksuite/cli`
- Feishu API docs: `https://open.feishu.cn/document/`
