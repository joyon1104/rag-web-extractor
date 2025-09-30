--- 페이지: https://github.com/cline/cline/wiki ---
# Welcome to the Cline Wiki

Cline is an AI assistant for VSCode that can use your CLI and Editor to help with complex software development tasks. This wiki serves as a central hub for information about Cline, its features, and how to use it effectively.

## Getting Started

1. Install the Cline extension from the [VS Marketplace](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev).
2. Configure your preferred API provider in the extension settings.
3. Open the Cline sidebar panel and start interacting with your AI assistant.

## Useful Links

* [Feature Requests](https://github.com/cline/cline/discussions/categories/feature-requests?discussions_q=is%3Aopen+category%3A%22Feature+Requests%22+sort%3Atop)
* [Join our Discord](https://discord.gg/cline)

## Contributing

We welcome contributions to Cline! Check out our [open issues](https://github.com/cline/cline/issues) or join our [Discord](https://discord.gg/cline) to get involved.

---

Explore the sidebar for more detailed information on specific topics and troubleshooting guides.

--- 페이지: https://github.com/cline/cline/wiki/Installing-Git-for-Checkpoints ---
# Installing Git for Checkpoints

Cline uses Git under the hood to create checkpoints of your workspace throughout tasks. Every time Cline makes changes to your files, it automatically creates a Git commit, allowing you to track and revert changes if needed. Follow the instructions below to install Git for your operating system.

## macOS

1. If you don't have Homebrew installed, [install it first](https://brew.sh)
2. Install Git using Homebrew:

   ```
   brew install git
   ```
3. Quit and re-open VSCode. Cline will automatically detect Git and enable checkpoints.

## Windows

1. Download and run the official Git installer from [git-scm.com](https://git-scm.com/downloads/win)
2. Quit and re-open VSCode. Cline will automatically detect Git and enable checkpoints.

## Linux

### Ubuntu/Debian

1. Open Terminal and update your package index:

   ```
   sudo apt update
   ```
2. Install Git:

   ```
   sudo apt install git
   ```
3. Quit and re-open VSCode. Cline will automatically detect Git and enable checkpoints.

## Support

If you've followed these steps and are still experiencing problems, please:

1. Check the [Cline GitHub Issues](https://github.com/cline/cline/issues) to see if others have reported similar problems
2. If not, create a new issue with details about your operating system, VSCode/Cursor version, and the steps you've tried

For additional help, join our [Discord](https://discord.gg/cline).

--- 페이지: https://github.com/cline/cline/wiki/TroubleShooting-%E2%80%90-%22PowerShell-is-not-recognized-as-an-internal-or-external-command%22 ---
If you're seeing an error message like this:

```
Command failed with exit code 1: powershell (Get-CimInstance -ClassName Win32_OperatingSystem).caption
'powershell' is not recognized as an internal or external command,
operable program or batch file.
```

This usually means that Windows can't find the PowerShell executable. This is caused by the user (or system) PATH environment variable not containing the directory where the PowerShell executable resides.

## How to Fix

1. Press `Windows + X` (or right-click on the Start button) and select "System". On the left side, click "Advanced system settings".
2. In the System Properties window, click the "Environment Variables" button near the bottom.
3. In the Environment Variables window, under "System variables" or "User variables" (depending on whether you want to make the change globally or for just your user), find the variable named "Path" and click "Edit".
4. In the Edit Environment Variable window, click "New", then paste the following:

   ```
   %SYSTEMROOT%\System32\WindowsPowerShell\v1.0\
   ```
5. Click "OK" on all windows to save your changes.
6. Restart your computer for the changes to take effect.

![image](https://private-user-images.githubusercontent.com/7799382/368840431-a0e2ec9b-d9f8-4b9d-b7c5-758960e68eaa.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTkxOTcyOTQsIm5iZiI6MTc1OTE5Njk5NCwicGF0aCI6Ii83Nzk5MzgyLzM2ODg0MDQzMS1hMGUyZWM5Yi1kOWY4LTRiOWQtYjdjNS03NTg5NjBlNjhlYWEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDkzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA5MzBUMDE0OTU0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZTdhMTNiYzUwMTI3YjAwMTlkMWVlNDYxNzY1NTJiYzBhMmU0NDg0MzJmNjI2ZTZhNDljYzg0MTY3MjY3NzNkOCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.hmOrpyjNhhz2YPOGYwSjtEAe-t01QEhW4qwuABWyubs)

## Support

If you've followed these steps and are still experiencing problems, please:

1. Check the [Cline GitHub Issues](https://github.com/cline/cline/issues) to see if others have reported similar problems
2. If not, create a new issue with details about your operating system, VSCode/Cursor version, and the steps you've tried

For additional help, join our [Discord](https://discord.gg/cline).

--- 페이지: https://github.com/cline/cline/wiki/Troubleshooting-%E2%80%90-Cline-Deleting-Code-with-%22Rest-of-Code-Here%22-Comments ---
Sometimes when using Cline to edit files, you may notice it replaces large chunks of code with placeholder comments like `// rest of code here`. This behavior occurs due to the AI model's maximum output token limit. For large files, the model may truncate portions of the code to fit within its constraints.

**Note:** Anthropic has announced an upcoming feature called "Fast Edit Mode" for Claude 3.5 Sonnet, which will enable faster and more reliable token output when editing files. It works by letting the model essentially regurgitate previously read tokens, and only have to "think" about *changes* to the file, rather than the entire contents. I will update the extension with this feature as soon as it becomes available, and this lazy coding issue will be a thing of the past. In the meantime, please try the troubleshooting steps below.

## Best Practices

To mitigate this issue:

1. Keep your files relatively small and modular.
2. Consider moving large constants (e.g. big strings) into separate files.

## Workaround: Using VSCode's Diff Editor

When Cline edits a file, it opens in VSCode's diff editor view. This presents two side-by-side versions of the file:

* **Left side:** Virtual document with file's original contents
* **Right side:** Updated file with Cline's changes

### Step 1: Expand the Diff View for Easier Editing

![](https://private-user-images.githubusercontent.com/7799382/370022060-9e466992-7fc4-48cc-b5b8-19b9e27cb94a.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTkxOTcyOTQsIm5iZiI6MTc1OTE5Njk5NCwicGF0aCI6Ii83Nzk5MzgyLzM3MDAyMjA2MC05ZTQ2Njk5Mi03ZmM0LTQ4Y2MtYjViOC0xOWI5ZTI3Y2I5NGEuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDkzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA5MzBUMDE0OTU0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NWUzZDczNzRhMTgwYjIyODgxZWU1YjgyNjI3MmEzYTJiM2RmMGZjMTQ0YTM4NTA1ZTZkNzliZmU3NWYyNDlmMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.P1Vqxr0gK9Qf_mxWYolsNhLGUHO8ASe0Ms9IGQ8bYSE)

1. By default, the diff view may be collapsed, showing changes merged into a single view. This can make editing more challenging.
2. To improve visibility and ease of editing, resize the window or tab to be wider. This will expand the diff view, splitting it into left (original) and right (modified) panels, making it much easier to compare and edit the changes.

### Step 2: Using the Revert Block Button

![](https://private-user-images.githubusercontent.com/7799382/370022119-4d26653f-d755-4b8b-bf9c-823a1146594f.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTkxOTcyOTQsIm5iZiI6MTc1OTE5Njk5NCwicGF0aCI6Ii83Nzk5MzgyLzM3MDAyMjExOS00ZDI2NjUzZi1kNzU1LTRiOGItYmY5Yy04MjNhMTE0NjU5NGYuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDkzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA5MzBUMDE0OTU0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZjFlZGE2ZWQyZWY5NGEyYWJiZDZiMjQ2YzY3OGRmYjU3MWI5OTMzZTc2MzgzYmQxODhmNzJjM2E1ZDhmYWU0OCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.H68HjOkVEydQ3bTH4v3ZLRNP78Pdk4rIuvm-XGH1xpc)

1. Locate the truncated section in the right-side document.
2. Click the "Revert Block" button in the gutter between the two views to restore the original content for that section.

### Alternative: Manual Copy and Paste

![](https://private-user-images.githubusercontent.com/7799382/370027020-57bdf1f2-55ad-4a79-bf1a-de6a753e136d.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTkxOTcyOTQsIm5iZiI6MTc1OTE5Njk5NCwicGF0aCI6Ii83Nzk5MzgyLzM3MDAyNzAyMC01N2JkZjFmMi01NWFkLTRhNzktYmYxYS1kZTZhNzUzZTEzNmQuZ2lmP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDkzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA5MzBUMDE0OTU0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MDZjZDQ2OGQ5OWNhOGRmYWMzNWQ4ZjliMTgzNDc1YmI0MGE0NDU5YTc0MTFhOGY4MGYwNzIyZjk5ZDg1NmE3NCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.gOjEXPMWYINb59i0le1GyKsAAFjst1g02dhJDDvDIF8)

If you're having trouble with the revert block button:

1. Select the missing content from the left-side document.
2. Copy the selected text.
3. Paste it into the appropriate location in the right-side document.

By using these methods, you can easily restore any content that the model may have truncated, ensuring your code remains intact. When you make these manual adjustments, the extension communicates these edits back to the model so it knows the final state of the file before proceeding in the task.

![](https://private-user-images.githubusercontent.com/7799382/377417921-7d6c1799-6dce-4f7f-b21c-5ff920d4ee1f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTkxOTcyOTQsIm5iZiI6MTc1OTE5Njk5NCwicGF0aCI6Ii83Nzk5MzgyLzM3NzQxNzkyMS03ZDZjMTc5OS02ZGNlLTRmN2YtYjIxYy01ZmY5MjBkNGVlMWYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDkzMCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTA5MzBUMDE0OTU0WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODgyNzE0Yjg3OWIwYWRmMWYyODc4N2YyYjRkMDM4NmUwMDk0ZDFlNDMzM2E1NGY4ZTI4ZDNkYzVlM2Y1YmUzMiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.7EhA26kiTqKU-Q6U_UKJAkYduS-4oN9e2qDeYpvT7XU)

## Support

If you've followed these steps and are still experiencing problems, please:

1. Check the [Cline GitHub Issues](https://github.com/cline/cline/issues) to see if others have reported similar problems
2. If not, create a new issue with details about your operating system, VSCode/Cursor version, and the steps you've tried

For additional help, join our [Discord](https://discord.gg/cline).

--- 페이지: https://github.com/cline/cline/wiki/Troubleshooting-%E2%80%90-Shell-Integration-Unavailable ---
**Note**: I've created a [minimal reproducible environment](https://github.com/saoudrizwan/shell-integration-problems) to help report issues with VSCode 1.93's new Terminal Shell Integration API. If the troubleshooting steps below don't resolve your issue, please follow the steps in that repository to report the problems you encounter.

---

* [What is Shell Integration?](#what-is-shell-integration)
* [How to Fix "Shell Integration Unavailable"](#how-to-fix-shell-integration-unavailable)
  + [Step 1: Update VSCode or Cursor](#step-1-update-vscode-or-cursor)
  + [Step 2: Configure VSCode to Use the Correct Shell](#step-2-configure-vscode-to-use-the-correct-shell)
  + [Step 3: Restart VSCode](#step-3-restart-vscode)
* [Additional Troubleshooting for Windows Users](#additional-troubleshooting-for-windows-users)
  + [Git Bash](#git-bash)
  + [PowerShell](#powershell)
    - [Understanding PowerShell Execution Policies](#understanding-powershell-execution-policies)
    - [Steps to Change the Execution Policy](#steps-to-change-the-execution-policy)
* [Still Having Trouble?](#still-having-trouble)
* [Unusual Terminal Output](#unusual-terminal-output)
* [Support](#support)

## What is Shell Integration?

Shell integration is a [new feature in VSCode 1.93](https://code.visualstudio.com/updates/v1_93#_terminal-shell-integration-api) that allows extensions like Cline to run commands in your terminal and read their output. Command output allows Cline to react to the result of the command on his own, without you having to handhold by copy-pasting the output in yourself. It's also quite powerful when running development servers as it allows Cline to fix errors as the server logs them.

## How to Fix "Shell Integration Unavailable"

### Step 1: Update VSCode or Cursor

First, make sure you're using the latest version of VSCode or Cursor:

1. Open VSCode or Cursor
2. Press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux)
3. Type "Check for Updates" (VSCode) or "Attempt Update" (Cursor) and select it
4. Restart VSCode/Cursor after the update

### Step 2: Configure VSCode to Use the Correct Shell

1. Open VSCode
2. Press `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux)
3. Type "Terminal: Select Default Profile" and choose it
4. Select one of the supported shells: zsh, bash, fish, or PowerShell.

### Step 3: Restart VSCode

After making these changes:

1. Quit VSCode completely
2. Reopen VSCode
3. Start a new Cline session (you can resume your previous task and try to run the command again, this time with Cline being able to see the output)

## Additional Troubleshooting for Windows Users

If you're using Windows and still experiencing issues with shell integration after trying the previous steps, it's recommended you use Git Bash.

### Git Bash

Git Bash is a terminal emulator that provides a Unix-like command line experience on Windows. To use Git Bash, you need to:

1. Download and run the Git for Windows installer from <https://git-scm.com/downloads/win>
2. Quit and re-open VSCode
3. Press `Ctrl + Shift + P` to open the Command Palette
4. Type "Terminal: Select Default Profile" and choose it
5. Select "Git Bash"

### PowerShell

If you'd still like to use PowerShell, make sure you're using an updated version (at least v7+).

* Check your current PowerShell version by running: `$PSVersionTable.PSVersion`
* If your version is below 7, [update PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7?view=powershell-7.4#installing-powershell-7).

You may also need to adjust your PowerShell execution policy. By default, PowerShell restricts script execution for security reasons.

#### Understanding PowerShell Execution Policies

PowerShell uses execution policies to determine which scripts can run on your system. Here are the most common policies:

* `Restricted`: No PowerShell scripts can run. This is the default setting.
* `AllSigned`: All scripts, including local ones, must be signed by a trusted publisher.
* `RemoteSigned`: Scripts created locally can run, but scripts downloaded from the internet must be signed.
* `Unrestricted`: No restrictions. Any script can run, though you will be warned before running internet-downloaded scripts.

For development work in VSCode, the `RemoteSigned` policy is generally recommended. It allows locally created scripts to run without restrictions while maintaining security for downloaded scripts. To learn more about PowerShell execution policies and understand the security implications of changing them, visit Microsoft's documentation: [About Execution Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies).

#### Steps to Change the Execution Policy

1. Open PowerShell as an Administrator: Press `Win + X` and select "Windows PowerShell (Administrator)" or "Windows Terminal (Administrator)".
2. Check Current Execution Policy by running this command:

   ```
   Get-ExecutionPolicy
   ```

   * If the output is already `RemoteSigned`, `Unrestricted`, or `Bypass`, you likely don't need to change your execution policy. These policies should allow shell integration to work.
   * If the output is `Restricted` or `AllSigned`, you may need to change your policy to enable shell integration.
3. Change the Execution Policy by running the following command:

   ```
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

   * This sets the policy to `RemoteSigned` for the current user only, which is safer than changing it system-wide.
4. Confirm the Change by typing `Y` and pressing Enter when prompted.
5. Verify the Policy Change by running `Get-ExecutionPolicy` again to confirm the new setting.
6. Restart VSCode and try the shell integration again.

## Still Having Trouble?

If you're still experiencing issues after trying the basic troubleshooting steps, you can try [manually installing shell integration](https://code.visualstudio.com/docs/terminal/shell-integration#_manual-installation).

For example, if you use zsh:

1. Run `code ~/.zshrc` in the terminal to open your zsh configuration file.
2. Add the following line to your `~/.zshrc`:

```
[[ "$TERM_PROGRAM" == "vscode" ]] && . "$(code --locate-shell-integration-path zsh)"
```

3. Save the file.
4. Quit VSCode completely.
5. Reopen VSCode and start a new Cline session.

If you use PowerShell you would do:

1. Run `code $Profile` in the terminal to open your PowerShell profile.
2. Add the following line to the file:

```
if ($env:TERM_PROGRAM -eq "vscode") { . "$(code --locate-shell-integration-path pwsh)" }
```

## Unusual Terminal Output

If you're seeing unusual output with rectangles, lines, escape sequences, or control characters, it may be related to terminal customization tools. Common culprits include:

* Powerlevel10k: A zsh theme that adds visual elements to the prompt
* Oh My Zsh: A framework for managing zsh configurations
* Fish shell themes

To troubleshoot:

1. Temporarily disable these tools in your shell configuration file (e.g., `~/.zshrc` for Zsh)
2. If the issue resolves, gradually re-enable features to identify the conflicting component

For example, if you're using Powerlevel10k with Zsh, you can disable it by commenting out the relevant line in your `~/.zshrc` file:

```
# Comment out the Powerlevel10k source line
# source /path/to/powerlevel10k/powerlevel10k.zsh-theme
```

If disabling these customizations resolves the issue, you may need to find alternative configurations that are compatible with VSCode's shell integration feature.

## OneDrive Windows Users

If you’re using Windows and have OneDrive enabled on your PC, your desktop directory path might differ from a typical user. Terminal processes will look to launch from C:\Users<user>\Desktop, while Onedrive users will have a desktop path that looks like C:\Users<user>\Onedrive\Desktop. To solve this, we can create a symbolic link from the expected Desktop location to the actual OneDrive Desktop location.

1. Launch Command Prompt in administrator mode
2. Enter the command:

`mklink /J "C:\Users\<username>\Desktop" "C:\Users\<username>\OneDrive\Desktop`

3. Press Enter and close Command Prompt
4. Restart VSCode

## Support

If you've followed these steps and are still experiencing problems, please:

1. Check the [Cline GitHub Issues](https://github.com/cline/cline/issues) to see if others have reported similar problems
2. If not, create a new issue with details about your operating system, VSCode/Cursor version, and the steps you've tried

For additional help, join our [Discord](https://discord.gg/cline).