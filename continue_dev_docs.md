# Source: https://docs.continue.dev/

![](https://mintcdn.com/continue-docs/fwCiH4jYqddOFwab/images/intro-0c302b9c15b890c251b1ad04586c880f.png?fit=max&auto=format&n=fwCiH4jYqddOFwab&q=85&s=c525774dbca270b7887a0f6c95cb42b7)

**Build faster with AI across your IDE, terminal, and CI/CD pipelines with
Continue.**

## [​](#continue-cli) Continue CLI

Terminal-native AI coding assistance with TUI and headless modes.

npm

yarn

pnpm

Copy

Ask AI

```
npm install -g @continuedev/cli
```

[## TUI Mode

Interactive terminal interface for development workflows  
• Automate builds & refactoring  
• Pre-commit hooks & scripted fixes  
• Terminal-first development](/cli/overview#tui-mode%3A-interactive-development)[## Headless Mode

Automated AI coding for CI/CD and server environments  
• Run in CI/CD pipelines  
• Batch processing & bulk operations  
• Server & container deployments](/cli/overview#headless-mode%3A-production-automation)

## [​](#ide-extensions) IDE Extensions

**Complement your CLI workflow** - Rich editor integrations for interactive
development.

[## VS Code

Install from VS Code Marketplace  
Real-time coding assistance and refactoring](https://marketplace.visualstudio.com/items?itemName=Continue.continue)[## JetBrains

Install from JetBrains Plugin Repository  
Autocomplete and multi-file edits](https://plugins.jetbrains.com/plugin/22707-continue-extension)

## [​](#core-features) Core Features

[## Agent

Multi-step workflows and complex task automation](/features/agent/quick-start)[## Chat

Ask questions and explore your codebase](/features/chat/quick-start)[## Edit

In-place code editing without breaking flow](/features/edit/quick-start)[## Autocomplete

Inline AI suggestions as you type](/features/autocomplete/quick-start)

## [​](#configuration) Configuration

[## Models

Connect your preferred AI models](/customization/models)[## Rules

Configure AI behavior and constraints](/customization/rules)[## MCPs

Extend functionality with MCP tools](/customization/mcp-tools)

## [​](#resources) Resources

[## Continue Hub

Community models, rules, and tools](https://hub.continue.dev/)[## GitHub Discussions

Get help from the community](https://github.com/continuedev/continue/discussions)[## CLI Examples

TUI and headless workflow examples](/guides/overview#continuous-ai)

---

# Source: https://docs.continue.dev/cli/install

Make sure you have [Node.js 18 or higher
installed](https://nodejs.org/en/download/).

## [​](#installation) Installation

Install Continue CLI globally using npm:

Copy

Ask AI

```
npm i -g @continuedev/cli
```

## [​](#two-ways-to-use-continue-cli) Two Ways to Use Continue CLI

**Quick Overview**: Continue CLI works in two modes - TUI for interactive
conversations or headless for automated commands.

* TUI Mode
* Headless Mode

**Interactive development sessions**Start a conversation with AI in your terminal:

Copy

Ask AI

```
cn
> @src/app.js Generate unit tests for this component
```

Perfect for exploration, debugging, and iterative development.

## [​](#setup) Setup

* cn TUI Mode
* cn Headless Mode

For interactive development and exploration:

1

Login to Continue CLI

Copy

Ask AI

```
cn login
```

This will open your browser to authenticate with Continue Hub.

2

Test TUI Mode

Start an interactive session:

Copy

Ask AI

```
cn
```

Try asking a question:

Copy

Ask AI

```
> Tell me about the CLI
```

## [​](#what%E2%80%99s-next%3F) What’s Next?

[## Quick Start Guide

Learn basic usage with practical examples](/cli/quick-start)[## Create your first workflow

Build automated workflows with Continue CLI](/guides/posthog-github-continuous-ai)

## [​](#getting-help) Getting Help

If you encounter issues:

* Ask for help in [our discussions](https://github.com/continuedev/continue/discussions)
* Report bugs on [GitHub](https://github.com/continuedev/continue)

---

# Source: https://docs.continue.dev/cli/overview

![](https://mintcdn.com/continue-docs/qRL4_zMbxjjbfdyM/images/cn-demo.gif?s=3ee6a3779232c3dd81bedfec5850233f)

**Continue enables developers to ship faster with Continuous AI.**

Build features from descriptions. Debug and fix issues. Navigate any codebase.
Automate tedious tasks.

## [​](#get-started-in-30-seconds) Get started in 30 seconds

Prerequisites:

* [Node.js 18 or newer](https://nodejs.org/en/download/)
* A [Continue Hub](https://hub.continue.dev) account (recommended) or local configuration

npm

Copy

Ask AI

```
# Install Continue CLI
npm install -g @continuedev/cli

# Navigate to your project

cd your-awesome-project

# Start coding with Continue

cn

# You'll be prompted to set up on first use
```

That’s it! You’re ready to start automating with Continue CLI.
[Continue with CLI Quickstart →](/cli/quick-start)

## [​](#two-ways-to-use-continue-cli) Two Ways to Use Continue CLI

Continue CLI offers two distinct modes designed for different workflows:

### [​](#tui-mode%3A-interactive-development) TUI Mode: Interactive Development

**Perfect for exploration, debugging, and iterating on AI workflows**

Copy

Ask AI

```
cn
> @src/components/UserProfile.js Review this component for security issues
> Generate comprehensive unit tests
> Suggest performance improvements
```

* **Interactive conversations** with your codebase
* **Iterate and refine** prompts and approaches
* **Explore and understand** complex codebases
* **Perfect for experimentation** and learning

### [​](#headless-mode%3A-production-automation) Headless Mode: Production Automation

**Perfect for CI/CD, automation, and reliable workflows**

Copy

Ask AI

```
cn -p "Generate a conventional commit message for staged changes"
cn -p "Review pull request changes for security vulnerabilities"
cn -p "Update documentation based on recent code changes"
```

* **Single-command execution** for automation
* **Reliable, repeatable results** for production use
* **CI/CD and pipeline integration**
* **Git hooks and automated workflows**

### [​](#development-workflow%3A-tui-%E2%86%92-headless) Development Workflow: TUI → Headless

**Pro Tip**: Start in TUI mode to iterate on your AI agent and prompts. Once
you have a workflow that works reliably, deploy it as a Continuous AI
automation.

1. **Experiment in TUI mode** to perfect your prompts and agent configuration
2. **Test different approaches** interactively until you get consistent results
3. **Convert successful workflows** to automated Continuous AI commands
4. **Deploy in production** with confidence in your proven approach

## [​](#why-developers-love-continue-cli) Why developers love Continue CLI

* **Works in your terminal**: Not another chat window. Not another IDE. Continue CLI meets you where you already work, with the tools you already love.
* **Takes action**: Continue CLI can directly edit files, run commands, and create commits. Need more? Check out our [MCPs](/customize/deep-dives/mcp).
* **Automate tasks**: Create issues from PostHog data, automatically assign labels to issues, and more. Do all this in a single command from your developer machines, or automatically in CI.
* **Flexible development flow**: Start interactive, then automate proven workflows.

## [​](#key-capabilities) Key Capabilities

### [​](#context-engineering) Context Engineering

* Use `@` to reference files and provide context
* Use `/` to run slash commands for specific tasks
* Access the same context providers as IDE extensions

### [​](#tool-integration) Tool Integration

* File editing and creation
* Terminal command execution
* Codebase understanding and analysis
* Git integration
* Web search and documentation access

### [​](#model-flexibility) Model Flexibility

* Switch between models with `/model` command
* Use any model configured in your `config.yaml`
* Access Continue Hub models and configurations

## [​](#continue-hub-integration) Continue Hub Integration

Continue CLI integrates seamlessly with [Continue Hub](https://hub.continue.dev) for:

### [​](#api-access) API Access

Get an API key for automation workflows:

1. Visit [Continue Hub API Keys](https://hub.continue.dev/settings/api-keys)
2. Create a new API key
3. Use with `cn login` or in your automation scripts

### [​](#secrets-management) Secrets Management

Store secure credentials for CLI workflows:

1. Visit [Continue Hub Secrets](https://hub.continue.dev/settings/secrets)
2. Add your API keys and sensitive data
3. Reference in configurations with `${{ secrets.SECRET_NAME }}`

### [​](#configuration-sync) Configuration Sync

* Cloud-managed configurations automatically sync
* Share configurations across team members
* Version control for your AI workflows

## [​](#common-use-cases) Common Use Cases

### [​](#tui-mode-examples) TUI Mode Examples

**Interactive development and exploration:**

Codebase Exploration

Iterative Debugging

Workflow Development

Copy

Ask AI

```
# Start interactive session
cn
> @src/components Find all unused React components
> /explain How does authentication work in this codebase?
> @auth/ What security patterns are used here?
```

### [​](#headless-mode-examples) Headless Mode Examples

**Production automation and scripting:**

Git Automation

CI/CD Integration

Issue Management

Copy

Ask AI

```
# Generate commit messages
cn -p "Generate a conventional commit message for the current changes"

# Code review automation

cn -p "Review the current git changes for bugs and suggest improvements"
```

## [​](#next-steps) Next steps

[## CLI Quickstart

Learn basic commands and common workflows](/cli/quick-start)[## Installation Guide

Install Continue CLI and set up your environment](/cli/install)[## CLI Workflows

Task-specific tutorials and examples](/guides/overview#continuous-ai)

---

# Source: https://docs.continue.dev/cli/quick-start

Get hands-on experience with Continue CLI through practical development workflows.

* TUI Mode
* Headless Mode

TUI Mode (`cn` command) is for **large development tasks** that require
agentic workflows with human oversight. Perfect for complex refactors,
feature implementation, or one-off automation tasks that need monitoring and
iteration.

## [​](#tui-mode%3A-large-development-tasks) TUI Mode: Large Development Tasks

Make sure you have [Continue CLI installed](/cli/install) and are in a project directory.

### [​](#example%3A-implementing-a-new-feature) Example: Implementing a New Feature

Copy

Ask AI

```
# Navigate to your project directory
cd your-awesome-project

# Start TUI Mode for complex development work
cn
```

**Example workflow for adding authentication:**

Copy

Ask AI

```
> I need to add JWT authentication to this Express app. Let me start by showing you the current structure.

> @src/app.js @package.json Here's my current setup. Can you implement JWT auth with middleware, login/register routes, and user model?

> [Agent analyzes codebase and implements auth system]
> [You review changes, test, and provide feedback]
> [Agent iterates based on your input until the feature is complete]
```

### [​](#example%3A-complex-refactoring) Example: Complex Refactoring

Copy

Ask AI

```
cn
```

**Refactoring a monolithic component:**

Copy

Ask AI

```
> @src/components/Dashboard.jsx This component is 800 lines and does too much. Help me break it into smaller, reusable components.

> [Agent analyzes component structure]
> [Proposes component breakdown strategy]
> [You approve approach]
> [Agent implements the refactor with proper props and state management]
> [You test and request adjustments]
```

### [​](#when-to-use-tui-mode) When to Use TUI Mode

✅ **Large development tasks** that need oversight  
✅ **Complex refactors** requiring multiple steps  
✅ **New feature implementation** with unknowns  
✅ **One-off automation tasks** you haven’t done before  
✅ **Debugging complex issues** that need exploration

## [​](#headless-mode%3A-automated-workflows) Headless Mode: Automated Workflows

Once you’ve refined a workflow in TUI Mode, convert it to Continuous AI for automation.

### [​](#example%3A-from-repl-%E2%86%92-continuous-ai) Example: From REPL → Continuous AI

**Step 1: Develop in TUI Mode**

Copy

Ask AI

```
cn
> @package.json @CHANGELOG.md Generate release notes for version 2.1.0
> [Test and refine the prompt until it works perfectly]
```

**Step 2: Convert to Continuous AI**

Copy

Ask AI

```
# Now use the refined workflow in automation
cn -p "Generate release notes for the current version based on package.json and recent commits"
```

### [​](#common-continuous-ai-workflows) Common Continuous AI Workflows

Copy

Ask AI

```
# Git automation
cn -p "Generate a conventional commit message for staged changes"
cn -p "Review the last 3 commits for potential issues"

# Code quality
cn -p "Fix all TypeScript errors in the src/ directory"
cn -p "Update outdated dependencies and fix breaking changes"

# Documentation
cn -p "@README.md Update documentation based on recent changes"
cn -p "Generate API documentation from JSDoc comments"

# CI/CD integration
cn -p "Analyze test failures and create GitHub issue with findings"
cn -p "Update version numbers and create release branch"
```

### [​](#when-to-use-headless-mode) When to Use Headless Mode

✅ **Proven workflows** you’ve tested in TUI Mode  
✅ **Repetitive tasks** that no longer need oversight  
✅ **CI/CD automation** in pipelines  
✅ **Git hooks** for automated checks  
✅ **Scheduled tasks** that run unattended

### [​](#available-slash-commands) Available Slash Commands

Common slash commands available in CLI:

* `/clear` - Clear the chat history
* `/compact` - Summarize chat history into a compact form
* `/config` - Switch configuration or organization
* `/exit` - Exit the chat
* `/fork` - Start a forked chat session from the current history
* `/help` - Show help message
* `/info` - Show session information
* `/init` - Create an AGENTS.md file
* `/login` - Authenticate with your account
* `/logout` - Sign out of your current session
* `/mcp` - Manage MCP server connections
* `/model` - Switch between available chat models
* `/resume` - Resume a previous chat session
* `/whoami` - Check who you’re currently logged in as

Use `/help` to see all available commands.

## [​](#the-development-workflow) The Development Workflow

**Recommended Approach**: Start complex tasks in TUI Mode to iterate and
refine your approach. Once you have a reliable workflow, convert it to
Headless Mode for automation.

### [​](#workflow-pattern) Workflow Pattern

1. **🔬 Experiment in TUI Mode**
   * Try complex development tasks with human oversight
   * Iterate on prompts and approaches until they work reliably
   * Test edge cases and refine the agent’s behavior
2. **⚡ Automate with Continuous AI**
   * Convert proven REPL workflows to single commands
   * Deploy in CI/CD, git hooks, or scheduled tasks
   * Run with confidence knowing the approach is tested

## [​](#next-steps) Next Steps

[## Create Your First Workflow

Build an automated PostHog to GitHub issues workflow](/guides/posthog-github-continuous-ai)[## Continuous AI Guide

Learn to build and deploy AI-powered development workflows](/guides/continuous-ai)

---

# Source: https://docs.continue.dev/customization/mcp-tools

Model Context Protocol (MCP) servers let Continue connect to external tools, systems, and databases by running MCP servers.
These servers make it possible to:

* **Enable integration** with external tools and systems
* **Create extensible interfaces** for custom capabilities
* **Support complex interactions** with your development environment
* **Allow partners** to contribute specialized functionality
* **Connect to databases** to understand schema and data models during development

![MCP servers overview](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/customization/images/mcp-blocks-overview-c9a104f9b586779c156f9cf34da197c2.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=2dd5d93de4e8f8d7a92da7c66627dfdd)

## [​](#learn-more-about-mcp-servers) Learn More About MCP servers

Learn more in the [MCP deep dive](/customize/deep-dives/mcp), and view [`mcpServers`](/reference#mcpservers) in the YAML Reference for more details.

---

# Source: https://docs.continue.dev/customization/models

* **[Chat](/customize/model-roles/chat)**: Power conversational interactions about code and provide detailed guidance
* **[Edit](/customize/model-roles/edit)**: Handle complex code transformations and refactoring tasks
* **[Apply](/customize/model-roles/apply)**: Execute targeted code modifications with high accuracy
* **[Autocomplete](/customize/model-roles/autocomplete)**: Provide real-time suggestions as developers type
* **[Embedding](/customize/model-roles/embeddings)**: Transform code into vector representations for semantic search
* **[Reranker](/customize/model-roles/reranking)**: Improve search relevance by ordering results based on semantic meaning

![Models Overview](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/customization/images/model-blocks-overview-36c30e7e01928d7a9b5b26ff1639c34b.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=70af4ab48cd912e337a2741ad79955fe)

## [​](#recommended-models) Recommended Models

### [​](#best-models-by-role) Best Models by Role

| Model role | Best open models | Best closed models | Notes |
| --- | --- | --- | --- |
| Agent Plan | [Qwen3 Coder (480B)](https://hub.continue.dev/openrouter/qwen3-coder)  [Qwen3 Coder (30B)](https://hub.continue.dev/ollama/qwen3-coder-30b)  [Devstral (27B)](https://hub.continue.dev/ollama/devstral)  [Kimi K2 (1T)](https://hub.continue.dev/openrouter/kimi-k2)  [gpt-oss (120B)](https://hub.continue.dev/openrouter/gpt-oss-120b)  [gpt-oss (20B)](https://hub.continue.dev/ollama/gpt-oss-20b)  [GLM 4.5 (355B)](https://hub.continue.dev/openrouter/glm-4-5)  [GLM 4.5 Air (106B)](https://hub.continue.dev/openrouter/glm-4-5-air) | [Claude Opus 4.1](https://hub.continue.dev/anthropic/claude-4-1-opus)  [Claude Sonnet 4](https://hub.continue.dev/anthropic/claude-4-sonnet)  [GPT-5](https://hub.continue.dev/openai/gpt-5)  [Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) | Closed models are slightly better than open models |
| Chat Edit | [Qwen3 Coder (480B)](https://hub.continue.dev/openrouter/qwen3-coder)  [Qwen3 Coder (30B)](https://hub.continue.dev/ollama/qwen3-coder-30b)  [gpt-oss (120B)](https://hub.continue.dev/openrouter/gpt-oss-120b)  [gpt-oss (20B)](https://hub.continue.dev/ollama/gpt-oss-20b) | [Claude Opus 4.1](https://hub.continue.dev/anthropic/claude-4-1-opus)  [Claude Sonnet 4](https://hub.continue.dev/anthropic/claude-4-sonnet)  [GPT-5](https://hub.continue.dev/openai/gpt-5)  [Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) | Closed and open models have pretty similar performance |
| Autocomplete | [QwenCoder2.5 (1.5B)](https://hub.continue.dev/ollama/qwen2.5-coder-1.5b)  [QwenCoder2.5 (7B)](https://hub.continue.dev/ollama/qwen2.5-coder-7b) | [Codestral](https://hub.continue.dev/mistral/codestral)  [Mercury Coder](https://hub.continue.dev/inception/mercury-coder) | Closed models are slightly better than open models |
| Apply | N/A | [Relace Instant Apply](https://hub.continue.dev/relace/instant-apply)  [Morph Fast Apply](https://hub.continue.dev/morphllm/morph-v2) | Open models are not good enough for this model role |
| Embed | [Nomic Embed Text](https://hub.continue.dev/ollama/nomic-embed-text-latest)  Qwen3 Embedding | [Voyage Code 3](https://hub.continue.dev/voyageai/voyage-code-3)  [Morph Embeddings](https://hub.continue.dev/morphllm/morph-embedding-v2)  Codestral Embed | Closed models are slightly better than open models |
| Rerank | zerank-1  zerank-1-small  Qwen3 Reranker | [Voyage Rerank 2.5](https://hub.continue.dev/voyageai/rerank-2-5)  Relace Code Rerank  [Morph Rerank](https://hub.continue.dev/morphllm/morph-rerank-v2) | Open models are beginning to emerge for this model role |
| Next Edit | [Instinct](https://hub.continue.dev/continuedev/instinct) | [Mercury Coder](https://hub.continue.dev/inception/mercury-coder) | Closed models are better than open models |

## [​](#learn-more-about-models) Learn More About Models

Continue supports [many model providers](/customize/model-providers/top-level/openai), including Anthropic, OpenAI, Gemini, Ollama, Amazon Bedrock, Azure, xAI, and more. Models can have various roles like `chat`, `edit`, `apply`, `autocomplete`, `embed`, and `rerank`.
Read more about [model roles](/customize/model-roles), [model capabilities](/customize/deep-dives/model-capabilities) and view [`models`](/reference#models) in the YAML Reference.

### [​](#example-model-setup-instructions) Example Model Setup Instructions

# [​](#frontier-models) Frontier Models

[Claude 4 Sonnet](https://hub.continue.dev/anthropic/claude-4-sonnet) from Anthropic

1. Get your API key from [Anthropic](https://console.anthropic.com/)
2. Add [Claude 4 Sonnet](https://hub.continue.dev/anthropic/claude-4-sonnet) to an agent on Continue Hub
3. Add `ANTHROPIC_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

[Qwen Coder 3 480B](https://hub.continue.dev/openrouter/qwen3-coder) from Qwen

1. Get your API key from [OpenRouter](https://openrouter.ai/settings/keys)
2. Add [Qwen Coder 3 480B](https://hub.continue.dev/openrouter/qwen3-coder) to an agent on Continue Hub
3. Add `OPENROUTER_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

[GPT-5](https://hub.continue.dev/openai/gpt-5) from OpenAI

1. Get your API key from [OpenAI](https://platform.openai.com)
2. Add [GPT-5](https://hub.continue.dev/openai/gpt-5) to an agent on Continue Hub
3. Add `OPENAI_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

[Kimi K2](https://hub.continue.dev/openrouter/kimi-k2) from Moonshot AI

1. Get your API key from [OpenRouter](https://openrouter.ai/settings/keys)
2. Add [Kimi K2](https://hub.continue.dev/openrouter/kimi-k2) to an agent on Continue Hub
3. Add `OPENROUTER_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

[Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) from Google

1. Get your API key from [Google AI Studio](https://aistudio.google.com)
2. Add [Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) to an agent on Continue Hub
3. Add `GEMINI_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

[Grok Code Fast 1](https://hub.continue.dev/xai/grok-code-fast-1) from xAI

1. Get your API key from [xAI](https://console.x.ai/)
2. Add [Grok Code Fast 1](https://hub.continue.dev/xai/grok-code-fast-1) to an agent on Continue Hub
3. Add `XAI_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

[Devstral Medium](https://hub.continue.dev/mistral/devstral-medium) from Mistral AI

1. Get your API key from [Mistral AI](https://console.mistral.ai/)
2. Add [Devstral Medium](https://hub.continue.dev/mistral/devstral-medium) to an agent on Continue Hub
3. Add `MISTRAL_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

[gpt-oss-120b](https://hub.continue.dev/openrouter/gpt-oss-120b) from OpenAI

1. Get your API key from [OpenRouter](https://openrouter.ai/settings/keys)
2. Add [gpt-oss-120b](https://hub.continue.dev/openrouter/gpt-oss-120b) to an agent on Continue Hub
3. Add `OPENROUTER_API_KEY` as a [User Secret](https://docs.continue.dev/hub/secrets/secret-types#user-secrets) on Continue Hub [here](https://hub.continue.dev/settings/secrets)
4. Click `Reload config` in the agent selector in the Continue IDE extension

### [​](#local-models) Local Models

These models can be run on your computer if you have enough VRAM.
Their limited tool calling and reasoning capabilities will make it challenging to use Agent mode.
[Qwen3 Coder 30B](https://hub.continue.dev/ollama/qwen3-coder-30b)

1. Add [Qwen3 Coder 30B](https://hub.continue.dev/ollama/qwen3-coder-30b) to an agent on Continue Hub
2. Run the model with [Ollama](https://docs.continue.dev/guides/ollama-guide#using-ollama-with-continue-a-developers-guide)
3. Click `Reload config` in the agent selector in the Continue IDE extension

[gpt-oss-20b](https://hub.continue.dev/ollama/gpt-oss-20b)

1. Add [gpt-oss-20b](ttps://hub.continue.dev/ollama/gpt-oss-20b) to an agent on Continue Hub
2. Run the model with [Ollama](https://docs.continue.dev/guides/ollama-guide#using-ollama-with-continue-a-developers-guide)
3. Click `Reload config` in the agent selector in the Continue IDE extension

[Devstral Small 27B](https://hub.continue.dev/ollama/devstral)

1. Add [Devstral Small](https://hub.continue.dev/ollama/devstral) to an agent on Continue Hub
2. Run the model with [Ollama](https://docs.continue.dev/guides/ollama-guide#using-ollama-with-continue-a-developers-guide)
3. Click `Reload config` in the agent selector in the Continue IDE extension

[Qwen2.5-Coder 7B](https://hub.continue.dev/ollama/qwen2.5-coder-7b) from Qwen

1. Add [Qwen2.5-Coder 7B](https://hub.continue.dev/ollama/qwen2.5-coder-7b) to an agent on Continue Hub
2. Run the model with [Ollama](https://docs.continue.dev/guides/ollama-guide#using-ollama-with-continue-a-developers-guide)
3. Click `Reload config` in the agent selector in the Continue IDE extension

[Gemma 3 4B](https://hub.continue.dev/ollama/gemma3-4b) from Google

1. Add [Gemma 3 4B](https://hub.continue.dev/ollama/gemma3-4b) to an agent on Continue Hub
2. Run the model with [Ollama](https://docs.continue.dev/guides/ollama-guide#using-ollama-with-continue-a-developers-guide)
3. Click `Reload config` in the agent selector in the Continue IDE extension

[Qwen2.5-Coder 1.5B](https://hub.continue.dev/ollama/qwen2.5-coder-1.5b) from Qwen

1. Add [Qwen2.5-Coder 1.5B](https://hub.continue.dev/ollama/qwen2.5-coder-1.5b) to an agent on Continue Hub
2. Run the model with [Ollama](https://docs.continue.dev/guides/ollama-guide#using-ollama-with-continue-a-developers-guide)
3. Click `Reload config` in the agent selector in the Continue IDE extension

---

# Source: https://docs.continue.dev/customization/overview

Continue can be deeply customized to fit your specific development workflow and preferences. This guide covers the main ways you can customize Continue to enhance your coding experience.

## [​](#change-your-model-provider) Change Your Model Provider

Continue allows you to choose your favorite or even add multiple model providers. This allows you to use different models for different tasks, or to try another model if you’re not happy with the results from your current model. Continue supports all of the popular model providers, including OpenAI, Anthropic, Microsoft/Azure, Mistral, and more. You can even self host your own model provider if you’d like. Learn more about [model providers](/customize/model-providers/top-level/openai).

## [​](#select-different-models-for-specific-tasks) Select Different Models for Specific Tasks

Different Continue features can use different models. We call these *model roles*. For example, you can use a different model for chat than you do for autocomplete. Learn more about [model roles](/customize/model-roles).

## [​](#create-a-slash-command) Create a Slash Command

Slash commands allow you to easily add custom functionality to Continue. You can use a slash command that allows you to generate a shell command from natural language, or perhaps generate a commit message, or create your own custom command to do whatever you want. Learn more about [slash commands](/customize/deep-dives/prompts).

## [​](#call-external-tools-and-functions) Call External Tools and Functions

Unchain your LLM with the power of tools using [Agent](/features/agent/quick-start). Add custom tools using [MCP Servers](/customization/mcp-tools)
Whatever you choose, you’ll probably start by editing your Agent.

## [​](#edit-your-agent) Edit Your Agent

You can easily access your agent configuration from the Continue Chat sidebar. Open the sidebar by pressing `cmd/ctrl` + `L` (VS Code) or `cmd/ctrl` + `J` (JetBrains) and click the Agent selector above the main chat input. Then, you can hover over an agent and click the `new window` (hub agents) or `gear` (local agents) icon.
![configure an agent](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/customization/images/configure-continue-a5c8c79f3304c08353f3fc727aa5da7e.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=1df2af08f7139eb9967f7b94e1e24482)

## [​](#manage-your-agent) Manage Your Agent

* See [Editing Hub Agents](/hub/agents/edit-an-agent) for more details on managing your hub agent
* See the [Config Deep Dive](/reference) for more details on configuring local agents.

---

# Source: https://docs.continue.dev/customization/prompts

* **Define interaction patterns** for specific tasks or frameworks
* **Encode domain expertise** for particular technologies
* **Ensure consistent guidance** aligned with organizational practices
* **Can be shared and reused** across multiple assistants
* **Act as automated code reviewers** that ensure consistency across teams

![Prompts Overview](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/customization/images/prompts-blocks-overview-17194d870840576f9a0dde548f2c70ec.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=19c9aa7e8c8e7d25c2a7715cf84812f2)

## [​](#learn-more) Learn More

* [Explore prompts](https://hub.continue.dev/?type=prompts) on the Hub
* Learn more in the [prompts deep dive](/customize/deep-dives/prompts)
* View [`prompts`](/reference#prompts) in the YAML Reference for more details

---

# Source: https://docs.continue.dev/customization/rules

Think of these as the guardrails for your AI coding agents:

* **Enforce company-specific coding standards** and security practices
* **Implement quality checks** that match your engineering culture
* **Create paved paths** for developers to follow organizational best practices

By implementing rules, you transform the AI from a generic coding agent into a knowledgeable team member that understands your project’s unique requirements and constraints.

## [​](#how-rules-work) How Rules Work

Your agent detects rules and applies the specified rules while in [Agent](/features/agent/quick-start), [Chat](/features/chat/quick-start), and [Edit](/features/edit/quick-start) modes.
Learn more in the [rules deep dive](/customize/deep-dives/rules), and view [`rules`](/reference#rules) in the YAML Reference for more details.

---

# Source: https://docs.continue.dev/customization/settings

![Continue Settings Panel - Card-based Layout](https://mintcdn.com/continue-docs/wjKb2iNkI1-eHx_R/images/continue-settings-card-layout.png?fit=max&auto=format&n=wjKb2iNkI1-eHx_R&q=85&s=9303abab24eb4e08eaba03616bd55bf6)
The new settings experience introduces a **card-based layout** that reduces visual clutter while maintaining powerful functionality. Every setting is more discoverable and easier to modify, whether you’re on an ultrawide monitor or a small laptop screen.

## [​](#quick-access) Quick Access

## Settings Icon

Click the gear in the Continue sidebar

## VS Code Settings

File → Preferences → Settings → Extensions → Continue

## Config File

Edit `config.yml` directly for advanced options

Use the toolbar buttons for quick access to specific settings: - **Rules**
(pencil icon) - Custom coding preferences - **Tools** (wrench icon) - Manage
integrations - **Models** (cube icon) - Configure AI providers

## [​](#core-settings) Core Settings

* Interface
* Autocomplete
* Indexing
* Experimental

Display Options

| Setting | Description |
| --- | --- |
| Session Tabs | Manage multiple chat sessions |
| Code Wrapping | Auto-wrap long code lines |
| Markdown Display | Show raw markdown vs rendered |
| Chat Scrollbar | Toggle scrollbar visibility |

Behavior

| Setting | Description |
| --- | --- |
| Auto-accept Diffs | Apply code changes automatically |
| Tool Rejection | Continue after tool rejection |
| Auto-naming | Generate session titles automatically |

## [​](#model-%26-assistant-selection) Model & Assistant Selection

![New assistant dropdown with cleaner icons and improved organization display](https://mintcdn.com/continue-docs/Q5xbeAqqC5vR319d/images/assistant-selector-dropdown.png?fit=max&auto=format&n=Q5xbeAqqC5vR319d&q=85&s=278403b782ee3023e1c394448edd795b)
The refined assistant selector features:

* **Organization badges** for easy provider identification
* **Smart error handling** that sorts problematic configurations while keeping them selectable
* **Keyboard navigation** for quick model switching

## [​](#privacy-%26-data) Privacy & Data

## Local Processing

All code analysis happens locally unless explicitly shared

## Telemetry Control

Opt in/out of anonymous usage statistics

## Session Management

Sessions auto-save and restore between IDE restarts

## [​](#troubleshooting) Troubleshooting

Model Connection Issues

* Verify API keys in `config.yml` - Check network connectivity - Confirm
  endpoint URLs are correct

Tool Loading Failures

* Review MCP server configurations - Check tool permissions - Verify tool
  dependencies are installed

Indexing Problems

* Check file permissions
* Review `.gitignore` patterns
* Verify sufficient disk space

Still having issues? Check our comprehensive [troubleshooting
guide](/troubleshooting) or visit the [FAQs](/faqs) for more solutions.

## [​](#next-steps) Next Steps

[## Configure Models

Set up your AI providers](/customization/models)[## Add Tools

Extend Continue with MCP tools](/customization/mcp-tools)[## Custom Rules

Define coding preferences](/customization/rules)[## Prompts

Customize AI behavior](/customization/prompts)

---

# Source: https://docs.continue.dev/faqs

## [​](#networking-issues) Networking Issues

### [​](#configure-certificates) Configure Certificates

If you’re seeing a `fetch failed` error and your network requires custom certificates, you will need to configure them in your config file. In each of the objects in the `"models"` array, add `requestOptions.caBundlePath` like this:

* YAML
* JSON

Copy

Ask AI

```
models:
  - name: My Model
    ...
    requestOptions:
      caBundlePath: /path/to/cert.pem
```

You may also set `requestOptions.caBundlePath` to an array of paths to multiple certificates.
***Windows VS Code Users***: Installing the [win-ca](https://marketplace.visualstudio.com/items?itemName=ukoloff.win-ca) extension should also correct this issue.

### [​](#vs-code-proxy-settings) VS Code Proxy Settings

If you are using VS Code and require requests to be made through a proxy, you are likely already set up through VS Code’s [Proxy Server Support](https://code.visualstudio.com/docs/setup/network#_proxy-server-support). To double-check that this is enabled, use `cmd/ctrl` + `,` to open settings and search for “Proxy Support”. Unless it is set to “off”, then VS Code is responsible for making the request to the proxy.

### [​](#code-server) code-server

Continue can be used in [code-server](https://coder.com/), but if you are running across an error in the logs that includes “This is likely because the editor is not running in a secure context”, please see [their documentation on securely exposing code-server](https://coder.com/docs/code-server/latest/guide#expose-code-server).

## [​](#changes-to-agents-not-showing-in-vs-code) Changes to agents not showing in VS Code

If you’ve made changes to agents (adding, modifying, or removing them) but the changes aren’t appearing in the Continue extension in VS Code, try reloading the VS Code window:

1. Open the command palette (`cmd/ctrl` + `shift` + `P`)
2. Type “Reload Window”
3. Select the reload option

This will restart VS Code and reload all extensions, which should make your agent changes visible.

## [​](#i-installed-continue%2C-but-don%E2%80%99t-see-the-sidebar-window) I installed Continue, but don’t see the sidebar window

By default the Continue window is on the left side of VS Code, but it can be dragged to right side as well, which we recommend in our tutorial. In the situation where you have previously installed Continue and moved it to the right side, it may still be there. You can reveal Continue either by using cmd/ctrl+L or by clicking the button in the top right of VS Code to open the right sidebar.

## [​](#i%E2%80%99m-getting-a-404-error-from-openai) I’m getting a 404 error from OpenAI

If you have entered a valid API key and model, but are still getting a 404 error from OpenAI, this may be because you need to add credits to your billing account. You can do so from the [billing console](https://platform.openai.com/settings/organization/billing/overview). If you just want to check that this is in fact the cause of the error, you can try adding $1 to your account and checking whether the error persists.

## [​](#i%E2%80%99m-getting-a-404-error-from-openrouter) I’m getting a 404 error from OpenRouter

If you have entered a valid API key and model, but are still getting a 404 error from OpenRouter, this may be because models that do not support function calling will return an error to Continue when a request is sent. Example error: `HTTP 404 Not Found from https://openrouter.ai/api/v1/chat/completions`

## [​](#indexing-issues) Indexing issues

If you are having persistent errors with indexing, our recommendation is to rebuild your index from scratch. Note that for large codebases this may take some time.
This can be accomplished using the following command: `Continue: Rebuild codebase index`.

## [​](#agent-mode-is-unavailable-or-tools-aren%E2%80%99t-working) Agent mode is unavailable or tools aren’t working

If Agent mode is grayed out or tools aren’t functioning properly, this is likely due to model capability configuration issues.

Continue uses system message tools as a fallback for models without native tool support, so most models should work with Agent mode automatically.

### [​](#check-if-your-model-has-tool-support) Check if your model has tool support

1. Not all models support native tool/function calling, but Continue will automatically use system message tools as a fallback
2. Try adding `capabilities: ["tool_use"]` to your model config to force tool support
3. Verify your provider supports function calling or that system message tools are working correctly

### [​](#tools-not-working) Tools Not Working

If tools aren’t being called:

1. Ensure `tool_use` is in your capabilities
2. Check that your API endpoint actually supports function calling
3. Some providers may use different function calling formats

### [​](#images-not-uploading) Images Not Uploading

If you can’t upload images:

1. Add `image_input` to capabilities
2. Ensure your model actually supports vision (e.g., gpt-4-vision, claude-3)
3. Check that your provider passes through image data

### [​](#add-capabilities) Add capabilities

If Continue’s autodetection isn’t working correctly, you can manually add capabilities in your `config.yaml`:

Copy

Ask AI

```
models:
  - name: my-model
    provider: openai
    model: gpt-4
    capabilities:
      - tool_use
      - image_input
```

### [​](#verify-with-provider) Verify with provider

Some proxy services (like OpenRouter) or custom deployments may not preserve tool calling capabilities. Check your provider’s documentation.

### [​](#verifying-current-capabilities) Verifying Current Capabilities

To see what capabilities Continue detected for your model:

1. Check the mode selector tooltips - they indicate if tools are available
2. Try uploading an image - if disabled, the model lacks `image_input`
3. Check if Agent mode is available - requires `tool_use`

See the [Model Capabilities guide](/customize/deep-dives/model-capabilities) for complete configuration details.

## [​](#android-studio-%E2%80%9Cnothing-to-show%E2%80%9D-in-chat) Android Studio - “Nothing to show” in Chat

This can be fixed by selecting `Actions > Choose Boot runtime for the IDE` then selecting the latest version, and then restarting Android Studio. [See this thread](https://github.com/continuedev/continue/issues/596#issuecomment-1789327178) for details.

## [​](#i-received-a-%E2%80%9Ccodebase-indexing-disabled-your-linux-system-lacks-required-cpu-features-avx2%2C-fma-%E2%80%9D-notification) I received a “Codebase indexing disabled - Your Linux system lacks required CPU features (AVX2, FMA)” notification

We use LanceDB as our vector database for codebase search features. On x64 Linux systems, LanceDB requires specific CPU features (FMA and AVX2) which may not be available on older processors.
Most Continue features will work normally, including autocomplete and chat. However, commands that rely on codebase indexing, such as `@codebase`, `@files`, and `@folder`, will be disabled.
For more details about this requirement, see the [LanceDB issue #2195](https://github.com/lancedb/lance/issues/2195).

## [​](#ollama-issues) Ollama Issues

For a comprehensive guide on setting up and troubleshooting Ollama, see the [Ollama Guide](/guides/ollama-guide).

### [​](#unable-to-connect-to-local-ollama-instance) Unable to connect to local Ollama instance

If you’re getting “Unable to connect to local Ollama instance” errors:

1. **Verify Ollama is running**: Check <http://localhost:11434> in your browser - you should see “Ollama is running”
2. **Start Ollama properly**: Use `ollama serve` (not just `ollama run model-name`)
3. **Check your config**: Ensure your `config.yaml` has the correct setup:

Copy

Ask AI

```
models:
  - name: llama3
    provider: ollama
    model: llama3:latest
```

### [​](#connection-failed-to-remote-ollama-ehostunreach%2Feconnrefused) Connection failed to remote Ollama (EHOSTUNREACH/ECONNREFUSED)

When connecting to Ollama on another machine:

1. **Configure Ollama to listen on all interfaces**:
   * Set environment variable: `OLLAMA_HOST=0.0.0.0:11434`
   * For systemd: Edit `/etc/systemd/system/ollama.service` and add under `[Service]`:

     Copy

     Ask AI

     ```
     Environment="OLLAMA_HOST=0.0.0.0:11434"
     Environment="OLLAMA_ORIGINS=*"
     ```
   * Restart Ollama: `sudo systemctl restart ollama`
2. **Update your Continue config**:

Copy

Ask AI

```
models:
  - name: llama3
    provider: ollama
    apiBase: http://192.168.1.136:11434  # Use your server's IP
    model: llama3:latest
```

3. **Check firewall settings**: Ensure port 11434 is open on the server

### [​](#ollama-not-working-in-wsl) Ollama not working in WSL

For WSL users having connection issues:

#### [​](#windows-11-22h2%2B-recommended) Windows 11 22H2+ (Recommended)

Create or edit `%UserProfile%\.wslconfig`:

Copy

Ask AI

```
[wsl2]
networkingMode=mirrored
```

Then restart WSL: `wsl --shutdown`

#### [​](#older-windows%2Fwsl-versions) Older Windows/WSL versions

In PowerShell (as Administrator):

Copy

Ask AI

```
# Add firewall rules
New-NetFireWallRule -DisplayName 'WSL Ollama' -Direction Inbound -LocalPort 11434 -Action Allow -Protocol TCP
New-NetFireWallRule -DisplayName 'WSL Ollama' -Direction Outbound -LocalPort 11434 -Action Allow -Protocol TCP

# Get WSL IP (run 'ip addr' in WSL to find eth0 IP)
# Then add port proxy (replace <WSL_IP> with your actual IP)
netsh interface portproxy add v4tov4 listenport=11434 listenaddress=0.0.0.0 connectport=11434 connectaddress=<WSL_IP>
```

### [​](#docker-container-can%E2%80%99t-connect-to-host-ollama) Docker container can’t connect to host Ollama

When running Continue or other tools in Docker that need to connect to Ollama on the host:
**Windows/Mac**: Use `host.docker.internal`:

Copy

Ask AI

```
models:
  - name: llama3
    provider: ollama
    apiBase: http://host.docker.internal:11434
    model: llama3:latest
```

**Linux**: Use the Docker bridge IP (usually `172.17.0.1`):

Copy

Ask AI

```
models:
  - name: llama3
    provider: ollama
    apiBase: http://172.17.0.1:11434
    model: llama3:latest
```

**Docker run command**: Add host mapping:

Copy

Ask AI

```
docker run -d --add-host=host.docker.internal:host-gateway ...
```

### [​](#parse-errors-with-remote-ollama) Parse errors with remote Ollama

If you’re getting parse errors with remote Ollama:

1. **Verify the model is installed on the remote**:

   Copy

   Ask AI

   ```
   OLLAMA_HOST=192.168.1.136:11434 ollama list
   ```
2. **Install missing models**:

   Copy

   Ask AI

   ```
   OLLAMA_HOST=192.168.1.136:11434 ollama pull llama3
   ```
3. **Check URL format**: Ensure you’re using `http://` not `https://` for local network addresses

## [​](#local-agent) Local Agent

### [​](#managing-local-secrets-and-environment-variables) Managing Local Secrets and Environment Variables

For running Continue completely offline without internet access, see the [Running Continue Without Internet guide](/guides/running-continue-without-internet).
Continue supports multiple methods for managing secrets locally, searched in this order:

1. **Workspace `.env` files**: Place a `.env` file in your workspace root directory
2. **Workspace Continue folder**: Place a `.env` file in `<workspace-root>/.continue/.env`
3. **Global `.env` file**: Place a `.env` file in `~/.continue/.env` for user-wide secrets
4. **Process environment variables**: Use standard system environment variables

#### [​](#creating-env-files) Creating `.env` files

Create a `.env` file in one of these locations:

* **Per-workspace**: `<workspace-root>/.env` or `<workspace-root>/.continue/.env`
* **Global**: `~/.continue/.env`

Example `.env` file:

Copy

Ask AI

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
CUSTOM_API_URL=https://api.example.com
```

#### [​](#using-secrets-in-config-yaml) Using secrets in config.yaml

Reference your local secrets using the `secrets` namespace:

Copy

Ask AI

```
models:
  - provider: openai
    apiKey: ${{ secrets.OPENAI_API_KEY }}
```

#### [​](#hub-managed-secrets) Hub-managed secrets

For centralized team secret management, use `${{ inputs.SECRET_NAME }}` syntax in your config.yaml and manage them at <https://hub.continue.dev/settings/secrets>:

Copy

Ask AI

```
models:
  - provider: openai
    apiKey: ${{ inputs.OPENAI_API_KEY }}
```

#### [​](#important-notes) Important notes

* **Never commit `.env` files** to version control - add them to `.gitignore`
* The `.env` file uses standard dotenv format (KEY=value, no quotes needed)
* Secrets are loaded when Continue starts, so restart your IDE after changes
* Local `.env` files take precedence over Hub secrets when both exist

#### [​](#troubleshooting-secrets) Troubleshooting secrets

If your API keys aren’t being recognized:

1. Check the `.env` file is in the correct location
2. Ensure there are no quotes around values in the `.env` file
3. Restart your IDE after adding/changing secrets
4. Verify the variable name matches exactly (case-sensitive)
5. Check that your `.env` file has proper line endings (LF, not CRLF on Windows)

### [​](#using-model-addons-locally) Using Model Addons Locally

You can leverage model addons from the Continue Hub in your local agent configurations using the `uses:` syntax. This allows you to reference pre-configured model blocks without duplicating configuration.

#### [​](#requirements) Requirements

* You must be logged in to Continue
* Internet connection is required (model addons are fetched from the hub)

#### [​](#usage) Usage

In your local `config.yaml`, reference model addons using the format `provider/model-name`:

Copy

Ask AI

```
name: My Local Agent
version: 0.0.1
schema: v1
models:
  - uses: ollama/llama3.1-8b
  - uses: anthropic/claude-3.5-sonnet
  - uses: openai/gpt-4
```

#### [​](#with-local-configuration) With local configuration

You can combine hub model addons with local models:

Copy

Ask AI

```
name: My Local Agent
version: 0.0.1
schema: v1
models:
  # Hub model addon
  - uses: anthropic/claude-3.5-sonnet
  
  # Local model configuration
  - name: Local Ollama
    provider: ollama
    model: codellama:latest
    apiBase: http://localhost:11434
```

#### [​](#override-addon-settings) Override addon settings

You can override specific settings from the model addon:

Copy

Ask AI

```
models:
  - uses: ollama/llama3.1-8b
    override:
      apiBase: http://192.168.1.100:11434  # Use remote Ollama server
      roles:
        - chat
        - autocomplete
```

This feature allows you to maintain consistent model configurations across teams while still allowing local customization when needed.

## [​](#how-do-i-reset-the-state-of-the-extension%3F) How do I reset the state of the extension?

Continue stores its data in the `~/.continue` directory (`%USERPROFILE%\.continue` on Windows).
If you’d like to perform a clean reset of the extension, including removing all configuration files, indices, etc, you can remove this directory, uninstall, and then reinstall.

## [​](#still-having-trouble%3F) Still having trouble?

You can also join our Discord community [here](https://discord.gg/vapESyrFmJ) for additional support and GitHub Discussions. Alternatively, you can create a GitHub issue [here](https://github.com/continuedev/continue/issues/new?assignees=&labels=bug&projects=&template=bug-report-%F0%9F%90%9B.md&title=), providing details of your problem, and we’ll be able to help you out more quickly.

---

# Source: https://docs.continue.dev/features/agent/context-selection

You can use the same methods to manually add context as [Chat](/features/chat/context-selection).
Tool call responses are automatically included as context items. This enables Agent mode to see the result of the previous action and decide what to do next.

---

# Source: https://docs.continue.dev/features/agent/how-it-works

## [​](#how-the-tool-handshake-works) How the Tool Handshake Works

Tools provide a flexible, powerful way for models to interface with the external world. They are provided to the model as a JSON object with a name and an arguments schema. For example, a `read_file` tool with a `filepath` argument will give the model the ability to request the contents of a specific file.
The following handshake describes how Agent uses tools:

1. In Agent mode, available tools are sent along with `user` chat requests
2. The model can choose to include a tool call in its response
3. The user gives permission. This step is skipped if the policy for that tool is set to `Automatic`
4. Continue calls the tool using built-in functionality or the MCP server that offers that particular tool
5. Continue sends the result back to the model
6. The model responds, potentially with another tool call and step 2 begins again

Tool availability varies by mode: - **Chat mode**: No tools included - **Plan
mode**: Only read-only tools included - **Agent mode**: All tools included

## [​](#what-built-in-tools-are-available) What Built-in Tools Are Available

Continue includes several built-in tools which provide the model access to IDE functionality.

### [​](#what-tools-are-available-in-plan-mode-read-only) What Tools Are Available in Plan Mode (Read-Only)

In Plan mode, only these read-only tools are available:

* **Read file** (`read_file`)
* **Read currently open file** (`read_currently_open_file`)
* **List directory** (`ls`)
* **Glob search** (`glob_search`)
* **Grep search** (`grep_search`)
* **Fetch URL content** (`fetch_url_content`)
* **Search web** (`search_web`)
* **View diff** (`view_diff`)
* **View repo map** (`view_repo_map`)
* **View subdirectory** (`view_subdirectory`)
* **Codebase tool** (`codebase_tool`)

### [​](#what-tools-are-available-in-agent-mode-all-tools) What Tools Are Available in Agent Mode (All Tools)

In Agent mode, all tools are available including the read-only tools above plus:

* **Create new file** (`create_new_file`): Create a new file within the project
* **Edit file** (`edit_file`): Make changes to existing files
* **Run terminal command** (`run_terminal_command`): Run commands from the workspace root
* **Create Rule Block** (`create_rule_block`): Create a new rule block in `.continue/rules`
* All other write/execute tools for modifying the codebase

---

# Source: https://docs.continue.dev/features/agent/how-to-customize

## [​](#how-to-add-rules-blocks) How to Add Rules Blocks

Adding Rules can be done in your agent locally or in the Hub. You can explore Rules on the Continue Hub and refer to the [Rules deep dive](/customize/deep-dives/rules) for more details.

## [​](#how-to-customize-system-messages) How to Customize System Messages

You can customize the system messages for Chat, Agent, and Plan modes using model-level configuration:

Copy

Ask AI

```
models:
  - name: GPT-4o
    provider: openai
    model: gpt-4o
    chatOptions:
      baseSystemMessage: "You are a helpful coding agent."
      baseAgentSystemMessage: "You are a systematic coding agent. Break down problems methodically."
      basePlanSystemMessage: "You are a planning agent. Create clear, actionable steps."
```

## [​](#how-to-add-mcp-tools) How to Add MCP Tools

You can add MCP servers to your agent to give Agent access to more tools. Explore [MCP Servers on the Hub](https://hub.continue.dev) and consult the [MCP guide](/customize/deep-dives/mcp) for more details.

## [​](#how-to-configure-tool-policies) How to Configure Tool Policies

You can adjust the Agent’s tool usage behavior to three options:

* **Ask First (default)**: Request user permission with “Cancel” and “Continue” buttons
* **Automatic**: Automatically call the tool without requesting permission
* **Excluded**: Do not send the tool to the model

:::warning
Be careful setting tools to “automatic” if their behavior is not read-only.
:::
To manage tool policies:

1. Click the tools icon in the input toolbar
2. View and change policies by clicking on the policy text
3. You can also toggle groups of tools on/off

Tool policies are stored locally per user.

---

# Source: https://docs.continue.dev/features/agent/model-setup

The models you set up for Chat mode will be used with Agent mode if the model supports tool calling. The recommended models and how to set them up can be found [here](/features/chat/model-setup).

## [​](#how-system-message-tools-work) How System Message Tools Work

Continue implements an innovative approach called **system message tools** that ensures consistent tool functionality across all models, regardless of their native capabilities. This allows Agent mode to work seamlessly with a wider range of models and providers.

### [​](#how-system-message-tools-function) How System Message Tools Function

Instead of relying solely on native tool calling APIs (which vary between providers), Continue converts tools into XML format and includes them in the system message. The model generates tool calls as structured XML within its response, which Continue then parses and executes. This approach provides:

* **Universal compatibility** - Any model capable of following instructions can use tools, not just those with native tool support
* **Consistent behavior** - Tool calls work identically across OpenAI, Anthropic, local models, and others
* **Better reliability** - Models that struggle with native tools often perform better with system message tools
* **Seamless switching** - Change between providers without modifying your workflow

## [​](#recommended-agent-models) Recommended Agent Models

| Model role | Best open models | Best closed models | Notes |
| --- | --- | --- | --- |
| Agent Plan | [Qwen3 Coder (480B)](https://hub.continue.dev/openrouter/qwen3-coder)  [Qwen3 Coder (30B)](https://hub.continue.dev/ollama/qwen3-coder-30b)  [Devstral (27B)](https://hub.continue.dev/ollama/devstral)  [Kimi K2 (1T)](https://hub.continue.dev/openrouter/kimi-k2)  [gpt-oss (120B)](https://hub.continue.dev/openrouter/gpt-oss-120b)  [gpt-oss (20B)](https://hub.continue.dev/ollama/gpt-oss-20b)  [GLM 4.5 (355B)](https://hub.continue.dev/openrouter/glm-4-5)  [GLM 4.5 Air (106B)](https://hub.continue.dev/openrouter/glm-4-5-air) | [Claude Opus 4.1](https://hub.continue.dev/anthropic/claude-4-1-opus)  [Claude Sonnet 4](https://hub.continue.dev/anthropic/claude-4-sonnet)  [GPT-5](https://hub.continue.dev/openai/gpt-5)  [Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) | Closed models are slightly better than open models |
| Chat Edit | [Qwen3 Coder (480B)](https://hub.continue.dev/openrouter/qwen3-coder)  [Qwen3 Coder (30B)](https://hub.continue.dev/ollama/qwen3-coder-30b)  [gpt-oss (120B)](https://hub.continue.dev/openrouter/gpt-oss-120b)  [gpt-oss (20B)](https://hub.continue.dev/ollama/gpt-oss-20b) | [Claude Opus 4.1](https://hub.continue.dev/anthropic/claude-4-1-opus)  [Claude Sonnet 4](https://hub.continue.dev/anthropic/claude-4-sonnet)  [GPT-5](https://hub.continue.dev/openai/gpt-5)  [Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) | Closed and open models have pretty similar performance |
| Autocomplete | [QwenCoder2.5 (1.5B)](https://hub.continue.dev/ollama/qwen2.5-coder-1.5b)  [QwenCoder2.5 (7B)](https://hub.continue.dev/ollama/qwen2.5-coder-7b) | [Codestral](https://hub.continue.dev/mistral/codestral)  [Mercury Coder](https://hub.continue.dev/inception/mercury-coder) | Closed models are slightly better than open models |
| Apply | N/A | [Relace Instant Apply](https://hub.continue.dev/relace/instant-apply)  [Morph Fast Apply](https://hub.continue.dev/morphllm/morph-v2) | Open models are not good enough for this model role |
| Embed | [Nomic Embed Text](https://hub.continue.dev/ollama/nomic-embed-text-latest)  Qwen3 Embedding | [Voyage Code 3](https://hub.continue.dev/voyageai/voyage-code-3)  [Morph Embeddings](https://hub.continue.dev/morphllm/morph-embedding-v2)  Codestral Embed | Closed models are slightly better than open models |
| Rerank | zerank-1  zerank-1-small  Qwen3 Reranker | [Voyage Rerank 2.5](https://hub.continue.dev/voyageai/rerank-2-5)  Relace Code Rerank  [Morph Rerank](https://hub.continue.dev/morphllm/morph-rerank-v2) | Open models are beginning to emerge for this model role |
| Next Edit | [Instinct](https://hub.continue.dev/continuedev/instinct) | [Mercury Coder](https://hub.continue.dev/inception/mercury-coder) | Closed models are better than open models |

### [​](#how-to-configure-agent-mode) How to Configure Agent Mode

Agent mode automatically determines whether to use native or system message tools based on the model’s capabilities. No additional configuration is required - simply select your model and Continue handles the rest.

## [​](#how-to-check-model-compatibility) How to Check Model Compatibility

To see which models support specific features like tool use (for Agent mode) and image input, check out our [Model Capabilities guide](/customize/deep-dives/model-capabilities).

---

# Source: https://docs.continue.dev/features/agent/plan-mode

## [​](#what-is-plan-mode%3F) What is Plan mode?

Plan mode is a restricted environment that provides read-only access to your codebase. It’s designed for safe exploration, understanding code, and planning changes without making any modifications.
![Plan mode in action](https://mintcdn.com/continue-docs/bpNErLbBON28HbZ-/images/plan-mode.gif?s=628aea892fe00e73589209aab2dd2c54)

### [​](#what-are-the-key-features-of-plan-mode%3F) What Are the Key Features of Plan Mode?

* **Read-only tools**: Access files, search, and analyze without risk
* **Safe exploration**: Perfect for understanding unfamiliar codebases
* **Planning focus**: Develop implementation strategies before execution
* **MCP support**: Works with all MCP tools alongside built-in read-only tools

### [​](#how-plan-mode-works) How Plan Mode Works

Plan mode filters the available tools to only include read-only operations. This means you can:

* Read any file in your project
* Search through code with grep and glob patterns
* View repository structure and diffs
* Fetch web content for additional context
* Use all MCP tools

But you cannot:

* Create, edit, or delete files
* Run terminal commands
* Make any system changes

### [​](#how-to-get-started-with-plan-mode) How to Get Started with Plan Mode

Select “Plan” from the mode selector below the chat input, or use `Cmd/Ctrl + .` to cycle through modes.
![Plan mode selector](https://mintcdn.com/continue-docs/bpNErLbBON28HbZ-/images/plan-mode-selector.png?fit=max&auto=format&n=bpNErLbBON28HbZ-&q=85&s=cf163b2b50f6b01d9cdd83ebee7ab8dd)
For detailed information about tools and usage, see the [Agent documentation](/features/agent/how-it-works), which covers both Agent and Plan modes.

### [​](#what-is-the-common-workflow-for-plan-mode%3F) What Is the Common Workflow for Plan Mode?

1. **Start in Plan mode** to explore and understand
2. **Develop your approach** with the model’s help
3. **Switch to Agent mode** when ready to implement

Plan mode shares the same interface and context features as Chat and Agent
modes. You can use `@` context providers and highlight code just like in other
modes.

---

# Source: https://docs.continue.dev/features/agent/quick-start

Agent equips the Chat model with the tools needed to handle a wide range of coding tasks, allowing the model to make decisions and save you the work of manually finding context and performing actions.


Learn how to choose the right mode

## Chat Mode

*Learn and discuss without changing code.***Mental Model:** Talking to a knowledgeable colleague**Best For:** Explaining concepts, comparing approaches, code review discussions.

## Plan Mode

*Safely explore and plan with read-only tools.***Mental Model:** Architect surveying before renovation**Best For:** Understanding a codebase, bug investigation, planning implementations.

## Agent Mode

*Make actual changes with full tool access.***Mental Model:** Contractor executing approved blueprints**Best For:** Implementing features, fixing bugs, running tests and commands.

### [​](#how-to-use-agent-mode) How to Use Agent Mode

You can switch to `Agent` in the mode selector below the chat input box. The mode selector offers three options:

* **Chat**: No tools available, pure conversation
* **Plan**: Read-only tools for safe exploration and planning
* **Agent**: All tools available for making changes

![How to select agent mode](https://mintcdn.com/continue-docs/fwCiH4jYqddOFwab/images/mode-select-agent.png?fit=max&auto=format&n=fwCiH4jYqddOFwab&q=85&s=10848029d93155fd5d2d57c7f8835001)

If Agent or Plan is disabled with a `Not Supported` message, the selected
model or provider doesn’t support tools, or Continue doesn’t yet support tools
with it. See [Model Blocks](/customization/models) for more information.

Use the keyboard shortcut `Cmd/Ctrl + .` to quickly cycle between modes.

### [​](#how-to-chat-with-agent) How to Chat with Agent

Agent lives within the same interface as [Chat](/features/chat/how-it-works), so the same [input](/features/chat/quick-start#how-to-start-a-conversation) is used to send messages and you can still use the same manual methods of providing context, such as [`@` context providers](/features/chat/quick-start#how-to-use--for-additional-context) or adding [highlighted code from the editor](/features/chat/quick-start#how-to-include-code-context).

#### [​](#how-to-use-natural-language-with-agent) How to Use Natural Language with Agent

With Agent, you can provide natural language instruction and let the model do the work. As an example, you might say
> Set the @typescript-eslint/naming-convention rule to “off” for all eslint configurations in this project

Agent will then decide which tools to use to get the job done.

## [​](#how-to-give-agent-permission) How to Give Agent Permission

By default, Agent will ask permission when it wants to use a tool. Click `Continue` to allow Agent mode to proceed with the tool call or `Cancel` to reject it.
![agent requesting permission](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/features/agent/images/agent-permission-c150919a5c43eb4f55d9d4a46ef8b2d6.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=8422184e6ab57a794daf59f44fe6ba96)
You can use tool policies to exclude or make usage automatic for specific tools. See [MCP Tools](/customization/mcp-tools) for more background.

## [​](#how-to-view-tool-responses) How to View Tool Responses

Any data returned from a tool call is automatically fed back into the model as a context item. Most errors are also caught and returned, so that Agent mode can decide how to proceed.
![agent response](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/features/agent/images/agent-response-c7287c82aac93fb4376f9d85b352b2d7.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=8ae50c7597b26d908c5445df453da2d8)

---

# Source: https://docs.continue.dev/features/autocomplete/context-selection

Autocomplete will automatically determine context based on the current cursor position. We use the following techniques to determine what to include in the prompt:

## [​](#file-prefix-and-suffix-context) File Prefix and Suffix Context

We will always include the code from your file prior to and after the cursor position.

## [​](#language-server-protocol-lsp-definitions) Language Server Protocol (LSP) Definitions

Similar to how you can use cmd/ctrl + click in your editor, we use the same tool (the LSP) to power “go to definition”. For example, if you are typing out a function call, we will include the function definition. Or, if you are writing code inside of a method, we will include the type definitions for any parameters or the return type.

## [​](#imported-file-context) Imported File Context

Because there are often many imports, we can’t include all of them. Instead, we look for symbols around your cursor that have matching imports and use that as context.

## [​](#recent-file-context) Recent File Context

We automatically consider recently opened or edited files and include snippets that are relevant to the current completion.

---

# Source: https://docs.continue.dev/features/autocomplete/how-it-works

## [​](#timing-optimization-for-autocomplete) Timing Optimization for Autocomplete

In order to display suggestions quickly, without sending too many requests, we do the following:

* Debouncing: If you are typing quickly, we won’t make a request on each keystroke. Instead, we wait until you have finished.
* Caching: If your cursor is in a position that we’ve already generated a completion for, this completion is reused. For example, if you backspace, we’ll be able to immediately show the suggestion you saw before.

## [​](#context-retrieval-from-your-codebase) Context Retrieval from Your Codebase

Continue uses a number of retrieval methods to find relevant snippets from your codebase to include in the prompt.

## [​](#filtering-and-post-processing-ai-suggestions) Filtering and Post-Processing AI Suggestions

Language models aren’t perfect, but can be made much closer by adjusting their output. We do extensive post-processing on responses before displaying a suggestion, including:

* Removing special tokens
* Stopping early when regenerating code to avoid long, irrelevant output
* Fixing indentation for proper formatting
* Occasionally discarding low-quality responses, such as those with excessive repetition

You can learn more about how it works in the [Autocomplete deep dive](/customization/models#autocomplete).

**Looking for AI that predicts your next changes or additions?** Check out
[Next Edit](/features/autocomplete/next-edit), an experimental feature that
proactively suggests code changes before you even start typing, going beyond
traditional autocomplete to anticipate entire code modifications.

---

# Source: https://docs.continue.dev/features/autocomplete/how-to-customize

Continue offers a handful of settings to customize autocomplete behavior. Visit the User Settings Page (Gear Icon) to manage these settings.
For a comprehensive guide on all configuration options and their impacts, see the [Autocomplete deep dive](/customize/deep-dives/autocomplete).

---

# Source: https://docs.continue.dev/features/autocomplete/model-setup

Setting up the right model for autocomplete is important for a smooth coding experience. Here are our top recommendations:

## [​](#model-recommendations) Model Recommendations

| Model role | Best open models | Best closed models | Notes |
| --- | --- | --- | --- |
| Autocomplete | [QwenCoder2.5 (1.5B)](https://hub.continue.dev/ollama/qwen2.5-coder-1.5b)  [QwenCoder2.5 (7B)](https://hub.continue.dev/ollama/qwen2.5-coder-7b) | [Codestral](https://hub.continue.dev/mistral/codestral)  [Mercury Coder](https://hub.continue.dev/inception/mercury-coder) | Closed models are slightly better than open models |

For a complete comparison of all models, see our [comprehensive model recommendations](/customization/models#recommended-models).

## [​](#next-edit-model) Next Edit Model

For proactive code prediction that anticipates your next edit, Continue supports specialized [Next Edit](/features/autocomplete/next-edit) models:
**Supported Next Edit model:**

* `mercury-coder-nextedit`: Primary model optimized for next edit prediction

Next Edit automatically activates when you have a compatible model configured for autocomplete and the appropriate access permissions.

## [​](#need-help%3F) Need Help?

If you’re not seeing any completions or need more detailed configuration options, check out our comprehensive [autocomplete deep dive guide](/customize/deep-dives/autocomplete).

## [​](#model-compatibility) Model Compatibility

To see a complete list of models and their capabilities, visit our [Model Capabilities guide](/customize/deep-dives/model-capabilities).

---

# Source: https://docs.continue.dev/features/autocomplete/next-edit

Next Edit is currently an experimental feature. It requires
[Instinct](https://hub.continue.dev/continuedev/instinct) or [Mercury Coder
model](https://hub.continue.dev/inception/mercury-coder) configured in
your Continue autocomplete settings and is not yet available for JetBrains
use.

## [​](#what-is-next-edit%3F) What is Next Edit?

Next Edit is an advanced AI-powered code prediction feature that anticipates what changes you’ll make next in your code. Unlike traditional autocomplete that reacts to your typing, Next Edit proactively analyzes your recent edits and coding patterns to suggest entire code modifications before you even start typing.
Think of it as having an AI pair programmer that understands your coding flow and suggests the logical next step in your development process.

## [​](#how-next-edit-works) How Next Edit Works

### [​](#the-prediction-process) The Prediction Process

1. **Context Analysis**: Captures your current cursor position and recent edit history
2. **Pattern Recognition**: Analyzes your coding patterns and the surrounding code context
3. **Next Step Prediction**: Uses specialized AI models to predict what you’ll likely change next
4. **Visual Presentation**: Shows predictions as diff overlays rather than simple text completions
5. **Interactive Review**: Lets you accept (Tab) or reject (Esc) the suggested changes
6. **Jump to Next Edit Location**: Lets you jump (Tab) to the next edit location or reject (Esc)

### [​](#intelligent-triggering) Intelligent Triggering

Next Edit activates automatically when:

* You finish making a code change
* The AI detects a logical continuation point
* Specialized next-edit models are available
* The current context suggests a predictable next step

## [​](#next-edit-vs-traditional-autocomplete) Next Edit vs Traditional Autocomplete

Prediction Scope

**Autocomplete**: Completes the current line or statement you’re typing**Next Edit**: Predicts entire code modifications across multiple lines

User Interaction

**Autocomplete**: Shows ghost text at your cursor position**Next Edit**: Displays diff overlays showing before/after changes, while also displaying ghost text if the change is purely additive.

Timing

**Autocomplete**: Reactive - responds to what you’re currently typing**Next Edit**: Proactive - anticipates what you’ll do next

Context Awareness

**Autocomplete**: Focuses on immediate code completion**Next Edit**: Analyzes recent edit patterns and broader code context

## [​](#how-to-use-next-edit) How to Use Next Edit

### [​](#prerequisites) Prerequisites

Next Edit requires:

* Compatible AI models (Mercury Coder or Instinct)
* VS Code (JetBrains support coming soon)
* **API Keys**: Organizations can add API keys to [org secrets](/hub/secrets/secret-types) for team-wide access. Individual users need to provide their own API keys in their [model configuration](/customize/model-providers/overview)

To use Next Edit, you must have the Instinct or Mercury Coder model configured
in your Continue autocomplete model settings. This model is specifically
designed for next edit predictions. Once it’s been loaded, you must reload VS
Code to activate it.![Next Edit Model Setup](https://mintcdn.com/continue-docs/H06NsCwr_R6qnbUW/images/features/autocomplete/images/instinct-autocomplete.png?fit=max&auto=format&n=H06NsCwr_R6qnbUW&q=85&s=33a421072c34adc8762187ff8d69cc80)

### [​](#using-next-edit-predictions) Using Next Edit Predictions

1

Make a Code Change

Edit your code normally. Next Edit will analyze your change patterns.

2

Review Predictions

When Next Edit activates, you’ll see a diff overlay showing predicted changes
in an editable region.

3

Accept or Reject

* **Tab**: Accept the prediction and apply changes - **Esc**: Reject the
  prediction and continue coding normally

4

Continue Coding

If accepted, your cursor moves to the last changed line. If rejected, your
workflow continues uninterrupted.

## [​](#what-are-the-model-requirements-for-next-edit%3F) What are the Model Requirements for Next Edit?

### [​](#specialized-models) Specialized Models

Next Edit requires AI models specifically trained for code prediction:

* **Mercury Coder**: Primary model optimized for next edit prediction
* **Instinct**: The leading open Next Edit model, trained by Continue

### [​](#automatic-detection) Automatic Detection

Continue automatically enables Next Edit when:

1. Your configured autocomplete model supports next edit capabilities
2. You have development team access permissions
3. The current code context suggests predictable next steps

## [​](#best-practices) Best Practices

## Trust the Process

Let Next Edit observe your coding patterns for a few editing sessions before expecting highly accurate predictions.

## Review Carefully

Always review suggested changes before accepting, especially for complex logic
modifications.

## Provide Feedback

Have feedback? We want to hear it. **[Add your thoughts to our feedback
discussions](https://github.com/continuedev/continue/discussions/categories/feedback)**
to help us improve.

## Combine with Other Features

Use Next Edit alongside Continue’s Chat and Agent modes for comprehensive AI-assisted development.

---

*Next Edit represents Continue’s vision for proactive AI coding assistance that anticipates developer needs rather than just reacting to input. As this feature evolves, it will become a powerful tool for accelerating development workflows and reducing repetitive coding tasks.*

---

# Source: https://docs.continue.dev/features/autocomplete/quick-start

## [​](#how-to-enable-and-use-continue-autocomplete) How to Enable and Use Continue Autocomplete

Autocomplete provides inline code suggestions as you type. To enable it, simply click the “Continue” button in the status bar at the bottom right of your IDE or ensure the “Enable Tab Autocomplete” option is checked in your IDE settings.

## [​](#keyboard-shortcuts-for-autocomplete) Keyboard Shortcuts for Autocomplete

### [​](#accept-a-full-suggestion) Accept a Full Suggestion

Accept a full suggestion by pressing `Tab`

### [​](#reject-a-full-suggestion) Reject a Full Suggestion

Reject a full suggestion with `Esc`

### [​](#partially-accept-a-suggestion) Partially Accept a Suggestion

For more granular control, use `cmd/ctrl` + `→` to accept parts of the suggestion word-by-word.

### [​](#force-a-suggestion-vs-code) Force a Suggestion (VS Code)

If you want to trigger a suggestion immediately without waiting, or if you’ve dismissed a suggestion and want a new one, you can force it by using the keyboard shortcut **`cmd/ctrl` + `alt` + `space`**.

---

# Source: https://docs.continue.dev/features/chat/context-selection

## [​](#how-to-use-text-input) How to Use Text Input

Typing a question or instructions into the input box is the only required context.

## [​](#how-to-include-highlighted-code) How to Include Highlighted Code

The highlighted code you’ve selected by pressing cmd/ctrl + L (VS Code) or cmd/ctrl + J (JetBrains) will be included in your prompt.

## [​](#how-to-include-the-active-file) How to Include the Active File

You can include the currently open file as context by pressing opt/alt + enter when you send your request.

## [​](#how-to-include-a-specific-file) How to Include a Specific File

You can include a specific file in your current workspace by typing ‘@Files’ and selecting the file.

## [​](#codebase-search) Codebase Search

For better codebase awareness, see our [guide on making agents aware of codebases and documentation](/guides/codebase-documentation-awareness).

## [​](#how-to-include-documentation-sites) How to Include Documentation Sites

For better documentation awareness, see our [guide on making agents aware of codebases and documentation](/guides/codebase-documentation-awareness).

## [​](#how-to-include-terminal-contents) How to Include Terminal Contents

You can include the contents of the terminal in your IDE by typing ‘@Terminal’.

## [​](#how-to-include-git-diff) How to Include Git Diff

You can include all of the changes you’ve made to your current branch by typing ‘@Git Diff’.

## [​](#how-to-use-other-context-providers) How to Use Other Context Providers

You can see a full list of built-in context providers [here](/customize/deep-dives/custom-providers).

---

# Source: https://docs.continue.dev/features/chat/how-it-works

## [​](#how-chat-core-functionality-works) How Chat Core Functionality Works

When you start a chat conversation, Continue:

1. **Gathers Context**: Uses any selected code sections and @-mentioned context
2. **Constructs Prompt**: Combines your input with relevant context
3. **Sends to Model**: Prompts the configured AI model for a response
4. **Streams Response**: Returns the AI response in real-time to the sidebar

## [​](#how-context-management-works) How Context Management Works

### [​](#what-context-is-automatically-included) What Context Is Automatically Included

* Selected code in your editor
* Current file context when relevant
* Previous conversation history in the session

### [​](#how-to-add-manual-context) How to Add Manual Context

* `@Files` - Reference specific files

## [​](#how-response-handling-works) How Response Handling Works

Each code section in the AI response includes action buttons:

* **Apply to current file** - Replace selected code
* **Insert at cursor** - Add code at cursor position
* **Copy** - Copy code to clipboard

## [​](#how-session-management-works) How Session Management Works

* Use `Cmd/Ctrl + L` (VS Code) or `Cmd/Ctrl + J` (JetBrains) to start a new session
* Clears all previous context for a fresh start
* Helpful for switching between different tasks

## [​](#what-advanced-features-are-available) What Advanced Features Are Available

### [​](#how-to-use-prompt-inspection) How to Use Prompt Inspection

View the exact prompt sent to the AI model in the [prompt logs](/troubleshooting) for debugging and optimization.

### [​](#context) Context

Learn more about how you can bring in context:

* [Codebase Context](/guides/codebase-documentation-awareness)
* [Documentation Context](/guides/codebase-documentation-awareness)
* [Built-in Context Providers](/customize/deep-dives/custom-providers)

---

*Chat is designed to feel like a natural conversation while maintaining full transparency about what context is being used.*

---

# Source: https://docs.continue.dev/features/chat/how-to-customize

## [​](#how-to-customize-chat) How to Customize Chat

There are a number of different ways to customize Chat:

* Add [rules](/customization/rules) to give the model persistent instructions through the system prompt
* Create [prompts](/customization/prompts) to kickoff workflows with instructions you repeat often

---

# Source: https://docs.continue.dev/features/chat/model-setup

The model you use for for Chat mode will be:

* used with Edit mode by default but can be switched
* always used with Agent mode if the model supports tool calling

## [​](#model-recommendations) Model Recommendations

| Model role | Best open models | Best closed models | Notes |
| --- | --- | --- | --- |
| Chat Edit | [Qwen3 Coder (480B)](https://hub.continue.dev/openrouter/qwen3-coder)  [Qwen3 Coder (30B)](https://hub.continue.dev/ollama/qwen3-coder-30b)  [gpt-oss (120B)](https://hub.continue.dev/openrouter/gpt-oss-120b)  [gpt-oss (20B)](https://hub.continue.dev/ollama/gpt-oss-20b) | [Claude Opus 4.1](https://hub.continue.dev/anthropic/claude-4-1-opus)  [Claude Sonnet 4](https://hub.continue.dev/anthropic/claude-4-sonnet)  [GPT-5](https://hub.continue.dev/openai/gpt-5)  [Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) | Closed and open models have pretty similar performance |

For a comprehensive comparison of all available models by role, see our [model recommendations table](/customization/models#recommended-models).

For model recommendations, please refer to our [Model Recommendations page](/customization/models).

---

# Source: https://docs.continue.dev/features/chat/quick-start

Chat makes it easy to ask for help from an AI without leaving your IDE. Get explanations, generate code, and iterate on solutions conversationally.

## [​](#how-to-use-chat-basic-usage) How to Use Chat - Basic Usage

### [​](#how-to-start-a-conversation) How to Start a Conversation

Type your question or request in the chat input and press Enter.
**Examples:**

* “Explain this function”
* “How do I handle errors in this code?”
* “Generate a test for this component”

### [​](#how-to-include-code-context) How to Include Code Context

Select code in your editor, then use the keyboard shortcut to include it in your chat:

* VS Code
* JetBrains

Press `Cmd/Ctrl + L` to send selected code to chat
Press `Cmd/Ctrl + J` to send selected code to chat

### [​](#how-to-use-%40-for-additional-context) How to Use @ for Additional Context

Type `@` to include specific context:

* `@Files` - Reference specific files
* `@Terminal` - Include terminal output

## [​](#how-to-work-with-responses) How to Work with Responses

When the AI provides code in its response, you’ll see action buttons:

* **Apply to current file** - Replace your selected code
* **Insert at cursor** - Add code at your cursor position
* **Copy** - Copy code to clipboard

## [​](#what-are-the-pro-tips-for-chat) What Are the Pro Tips for Chat

### [​](#start-fresh) Start Fresh

Press `Cmd/Ctrl + L` (VS Code) or `Cmd/Ctrl + J` (JetBrains) in an empty chat to start a new session.

### [​](#be-specific) Be Specific

Include details about:

* What you’re trying to accomplish
* Any constraints or requirements
* Your preferred coding style or patterns

### [​](#iterate) Iterate

If the first response isn’t perfect:

* Ask follow-up questions
* Request modifications
* Provide additional context

## [​](#what-are-common-use-cases-for-chat) What Are Common Use Cases for Chat

### [​](#code-explanation) Code Explanation

Select confusing code and ask “What does this code do?”

### [​](#bug-fixing) Bug Fixing

Include error messages and ask “How do I fix this error?”

### [​](#code-generation) Code Generation

Describe what you want: “Create a React component that displays a user profile”

### [​](#refactoring) Refactoring

Select code and ask “How can I make this more efficient?”


---

*Chat is designed for quick interactions and iterative problem-solving. Don’t hesitate to ask follow-up questions!*

---

# Source: https://docs.continue.dev/features/edit/context-selection

## [​](#how-to-use-text-input) How to Use Text Input

Typing a question or instructions into the input box is the only required context.

## [​](#what-context-is-included-in-edit-mode) What Context is Included in Edit Mode

The **entire contents** of the current file are included in the prompt for context. The model will only attempt to edit the highlighted/specified ranges.

---

# Source: https://docs.continue.dev/features/edit/how-it-works

## [​](#how-edit-functionality-works) How Edit Functionality Works

When you start an edit session, Continue:

1. **Gathers Context**: Uses the highlighted code and the current file contents
2. **Prompts the Model**: Sends the gathered context and your input instructions to the model
3. **Applies Changes**: The model response is then streamed directly back to the highlighted range in your code, where we apply a diff formatting to show the proposed changes.

If you accept the diff, we remove the previously highlighted lines, and if you reject the diff, we remove the proposed changes.

**Looking for AI that predicts your next edit?** Check out [Next Edit](/features/autocomplete/next-edit), an experimental feature that proactively suggests code changes before you even start typing, going beyond traditional autocomplete to anticipate entire code modifications.

If you would like to view the exact prompt that is sent to the model during an edit, you can [find it in the prompt logs](/troubleshooting#check-the-logs).

---

# Source: https://docs.continue.dev/features/edit/how-to-customize

## [​](#how-to-set-active-edit%2Fapply-model) How to Set Active Edit/Apply Model

You can configure particular models from your Agent to be used for Edit and Apply requests.

1. Click the 3 dots above the main input
2. Click the cube icon to expand the “Models” section
3. Use the dropdowns to select models for Edit and Apply

![Edit model selection](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/edit-model.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=4f7ea21f627f36e82255676a06f6c272)
Learn more about the [Edit role](/customize/model-roles/edit) and [Apply role](/customize/model-roles/apply).

---

# Source: https://docs.continue.dev/features/edit/model-setup

The model you set up for Chat mode will be used for Edit mode by default.

## [​](#recommendations) Recommendations

| Model role | Best open models | Best closed models | Notes |
| --- | --- | --- | --- |
| Chat Edit | [Qwen3 Coder (480B)](https://hub.continue.dev/openrouter/qwen3-coder)  [Qwen3 Coder (30B)](https://hub.continue.dev/ollama/qwen3-coder-30b)  [gpt-oss (120B)](https://hub.continue.dev/openrouter/gpt-oss-120b)  [gpt-oss (20B)](https://hub.continue.dev/ollama/gpt-oss-20b) | [Claude Opus 4.1](https://hub.continue.dev/anthropic/claude-4-1-opus)  [Claude Sonnet 4](https://hub.continue.dev/anthropic/claude-4-sonnet)  [GPT-5](https://hub.continue.dev/openai/gpt-5)  [Gemini 2.5 Pro](https://hub.continue.dev/google/gemini-2.5-pro) | Closed and open models have pretty similar performance |

See our [comprehensive model recommendations](/customization/models#recommended-models) for the best models for each role, including Edit and Apply.

## [​](#how-to-set-up-an-apply-model) How to Set Up an Apply Model

We also recommend setting up an Apply model for the best Edit experience.
For recommended Apply models, please refer to our [Model Recommendations page](/customization/models).

## [​](#how-to-determine-model-compatibility) How to Determine Model Compatibility

For a complete overview of which models support various features, see our [Model Capabilities guide](/customize/deep-dives/model-capabilities).

---

# Source: https://docs.continue.dev/features/edit/quick-start

## [​](#how-to-continue-edit) How to Continue Edit

Edit is a convenient way to make quick changes to specific code and files. Select code, describe your code changes, and a diff will be streamed inline to your file which you can accept or reject.
Edit is recommended for small, targeted changes, such as

* Writing comments
* Generating unit tests
* Refactoring functions or methods

## [​](#how-to-activate-edit) How to Activate Edit

Highlight the block of code you would like to modify and press `Cmd+I` (Mac) or `Ctrl+I` (Windows/Linux) to activate Edit mode. You can also press `Cmd/Ctrl+I` with no code highlighted, which will default to inserting code at the current cursor location.
Once you’ve activated Edit, you’re ready to provide instructions.

### [​](#how-to-provide-instructions) How to Provide Instructions

Describe the changes you would like the model to make to your highlighted code. For edits, a good prompt should be relatively short and concise. For longer, more complex tasks, we recommend using [Chat](/features/chat/quick-start).

### [​](#how-to-accept-or-reject-changes) How to Accept or Reject Changes

Proposed changes appear as inline diffs within your highlighted text.
You can navigate through each proposed change, accepting or rejecting them using `Cmd+Opt+Y` (Mac) or `Ctrl+Alt+Y` (Windows/Linux) to accept, or `Cmd+Opt+N` (Mac) or `Ctrl+Alt+N` (Windows/Linux) to reject.
You can also accept or reject all changes at once using `Cmd+Shift+Enter` (Mac) or `Ctrl+Shift+Enter` (Windows/Linux) to accept, or `Cmd+Shift+Delete` (Mac) or `Ctrl+Shift+Backspace` (Windows/Linux) to reject.
If you want to request a new suggestion for the same highlighted code section, you can use `Cmd+I` (Mac) or `Ctrl+I` (Windows/Linux) to re-prompt the model.

## [​](#how-to-use-edit-in-jetbrains) How to Use Edit in Jetbrains

In Jetbrains, Edit is implemented as an inline popup. See the header GIF example.

---

# Source: https://docs.continue.dev/getting-started/install

* VS Code
* JetBrains

1

Install from Marketplace

Click `Install` on the [Continue extension page in the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Continue.continue)

2

Install in VS Code

This will open the Continue extension page in VS Code, where you will need to
click `Install` again

3

Move to Right Sidebar

The Continue logo will appear on the left sidebar. For a better experience, move Continue to the right sidebar![move-to-right-sidebar](https://mintcdn.com/continue-docs/bpNErLbBON28HbZ-/images/move-to-right-sidebar-b2d315296198e41046fc174d8178f30a.gif?s=a5919de5d6f91db72b8251b1f05e01fd)

4

Sign In

[Sign in to the hub](https://auth.continue.dev/) to get started with your first agent

If you have any problems, see the [troubleshooting guide](/troubleshooting) or
ask for help in [our Discord](https://discord.gg/NWtdYexhMs)

## [​](#signing-in) Signing in

Click “Get started” to sign in to the hub and start using agents.
![Hub Onboarding in the Extension](https://mintcdn.com/continue-docs/tt1KAgjxyDBw6wmj/images/getting-started/images/hub-onboarding-card-81abd457b6d131c4b0aa89a5a6d647d3.png?fit=max&auto=format&n=tt1KAgjxyDBw6wmj&q=85&s=a9fea6d27a14d97c73a21b12d692399a)

---

# Source: https://docs.continue.dev/getting-started/overview

## [​](#features) Features

* Agent
* Chat
* Plan
* Edit
* Autocomplete

[Agent](/features/agent/quick-start) equips the Chat model with the tools needed to handle a wide range of coding tasks![agent](https://mintcdn.com/continue-docs/6EWp3-Bet9bo6Nsz/images/agent-9ef792cfc196a3b5faa984fb072c4400.gif?s=08eb200c6aa31c15d6876757842d60e6)

Learn more about [Agent](/features/agent/quick-start)

## [​](#ai-coding-agents) AI Coding Agents

Continue offers flexible AI assistants that enhance your development workflow. You can choose between cloud-managed **Hub Agents** for easy setup and synchronization, or **Local Agents** for complete control and privacy. Learn more about [understanding and configuring agents](/guides/understanding-agents).

---

# Source: https://docs.continue.dev/getting-started/quick-start

Welcome to Continue! This interactive tutorial will guide you through all four core features using practical examples. Follow along step-by-step to learn more about Continue’s capabilities.

**Prerequisites**: Make sure you have [installed
Continue](/getting-started/install) and [signed
in](https://auth.continue.dev/) to get started.

---

## [​](#%F0%9F%94%84-autocomplete) 🔄 Autocomplete

**What it does**: Provides intelligent inline code suggestions as you type, powered by AI.

1

Create a Test File

Create a new file called `tutorial.js` (or use any language you prefer) in your IDE

2

Try Autocomplete

Copy this starter code and place your cursor at the end of the comment:

Copy

Ask AI

```
// TODO: Implement a sorting algorithm function
function sortingAlgorithm(arr) {
  // Place cursor here and press Enter
}
```

Press **Enter** and watch Continue suggest code completions. Press **Tab** to accept suggestions.

3

See the Magic

Continue will intelligently suggest function implementations based on the context and comment.

Autocomplete works best when you provide clear function names, comments, or
type annotations that give context about your intent.

---

## [​](#%E2%9C%8F%EF%B8%8F-edit) ✏️ Edit

**What it does**: Make quick, targeted changes to specific code sections using natural language instructions.

1

Add Sample Code

Paste this bubble sort implementation in your file:

Copy

Ask AI

```
function sortingAlgorithm(x) {
  for (let i = 0; i < x.length; i++) {
    for (let j = 0; j < x.length - 1; j++) {
      if (x[j] > x[j + 1]) {
        let temp = x[j];
        x[j] = x[j + 1];
        x[j + 1] = temp;
      }
    }
  }
  return x;
}
```

2

Highlight the Function

**Highlight** the entire function in your editor

3

Open Edit Mode

Press **Cmd/Ctrl + I** to open Edit mode

4

Give Instructions

Type: `"make this more readable and add TypeScript types"`

5

Watch the Magic

Watch Continue refactor your code automatically!

6

Review Changes

Continue will show you a diff of the proposed changes. Accept or reject individual changes as needed.

Edit is perfect for refactoring, adding documentation, fixing bugs, or
converting between languages/frameworks.

---

## [​](#%F0%9F%92%AC-chat) 💬 Chat

**What it does**: Interactive AI assistant that can analyze code, answer questions, and provide guidance without leaving your IDE.

1

Add Another Function

Add this second sorting function to your file:

Copy

Ask AI

```
function sortingAlgorithm2(x) {
  for (let i = 0; i < x.length; i++) {
    for (let j = 0; j < x.length - 1; j++) {
      if (x[j] > x[j + 1]) {
        let temp = x[j];
        x[j] = x[j + 1];
        x[j + 1] = temp;
      }
    }
  }
  return x;
}
```

2

Start a Conversation

1. **Highlight** the function
2. Use the keyboard shortcuts below to add it to Chat.
3. Ask: `"What sorting algorithm is this and how can I optimize it?"`

3

Explore Further

Try these follow-up questions:

* `"Show me how to implement quicksort instead"`
* `"What's the time complexity of this algorithm?"`
* `"Can you write unit tests for this function?"`

### [​](#chat-keyboard-shortcuts) Chat Keyboard Shortcuts

* VS Code
* JetBrains IDEs

**Cmd/Ctrl + L**  
New Chat / New Chat With Selected Code / Close Continue Sidebar If Chat Already In Focus**Cmd/Ctrl + Shift + L**  
Focus Current Chat / Add Selected Code To Current Chat / Close Continue Sidebar If Chat Already In Focus

Use Chat for code reviews, debugging help, learning new concepts, or
brainstorming solutions to complex problems.

---

## [​](#%F0%9F%A4%96-agent) 🤖 Agent

**What it does**: An autonomous coding assistant that can read files, make changes, run commands, and handle complex multi-step tasks.

1

Switch to Agent Mode

1. Open the Continue panel
2. Click the **dropdown** in the bottom left of the input box
3. Select **“Agent”** mode

2

Give Agent a Complex Task

Try this prompt: `"Write comprehensive unit tests for the sorting functions in this file. Create the tests in a new file using Jest, and make sure to test edge cases like empty arrays and single elements."`

3

Watch Agent Work

Agent will:

* ✅ Analyze your existing code
* ✅ Create a new test file
* ✅ Write comprehensive tests
* ✅ Handle setup and imports
* ✅ Explain what it’s doing at each step

Agent has powerful capabilities including file creation and modification.
Always review Agent’s changes before accepting them.

---

## [​](#%F0%9F%9A%80-next-steps) 🚀 Next Steps

Congratulations! You’ve experienced all four core Continue features. Here’s what to explore next:

[## Customize Your Setup

Configure models, add context providers, and personalize your workflow](/customize/overview)[## Advanced Features

Dive deeper into Agent capabilities and advanced use cases](/features/agent/quick-start)[## Model Providers

Connect your preferred AI models and providers](/customize/model-providers/overview)[## Join Community

Get help and share experiences with other Continue users](https://discord.gg/NWtdYexhMs)

---

## [​](#%F0%9F%93%9A-feature-deep-dives) 📚 Feature Deep Dives

Ready to master specific features? Check out these detailed guides:

Autocomplete Deep Dive

Learn about [configuring autocomplete
models](/customize/model-roles/autocomplete), [fine-tuning
suggestions](/customize/deep-dives/autocomplete), and [troubleshooting
common issues](/troubleshooting).

Chat & Agent Best Practices

Discover [effective prompting techniques](/customize/deep-dives/prompts), [hub
v. local agents](/guides/understanding-agents), and [custom slash
commands](/customize/deep-dives/prompts).

Enterprise & Teams

Explore [Hub Agents](/hub/agents/intro), [organization
management](/hub/governance/creating-an-org), and [sharing
configurations](/hub/sharing).

**Need help?** Check our [troubleshooting guide](/troubleshooting) or ask a
question in our [community
discussions](https://github.com/continuedev/continue/discussions).

---

# Source: https://docs.continue.dev/troubleshooting

1. [Check the logs](#check-the-logs)
2. [Try the latest pre-release](#download-the-latest-pre-release)
3. [Download an older version](#download-an-older-version)
4. [Resolve keyboard shortcut issues](#keyboard-shortcuts-not-resolving)
5. [Check FAQs for common issues](/faqs)

## [​](#check-the-logs) Check the logs

To solve many problems, the first step is reading the logs to find the relevant error message. To do this, follow these steps:

### [​](#vs-code) VS Code

#### [​](#console-logs) Console logs

In order to view debug logs, which contain extra information, click the
dropdown at the top that says “Default levels” and select “Verbose”.

1. `cmd` + `shift` + `P` for MacOS or `ctrl`
   * `shift` + `P` for Windows
2. Search for and then select “Developer: Toggle Developer Tools”
3. This will open the [Chrome DevTools window](https://developer.chrome.com/docs/devtools/)
4. Select the `Console` tab
5. Read the console logs

#### [​](#prompt-logs-continue-console) Prompt Logs (Continue Console)

To view prompt logs/analytics, you can enable the Continue Console.

1. Open VS Code settings (`cmd/ctrl` + `,`)
2. Search for the setting “Continue: Enable Console” and enable it
3. Reload the window
4. Open the Continue Console by using the command palette (`cmd/ctrl` + `shift` + `P`) and searching for “Continue: Focus on Continue Console View”

![Continue Console](https://mintcdn.com/continue-docs/fwCiH4jYqddOFwab/images/images/continue-console-d387a10c2918c117c6c253a3b5f18c22.png?fit=max&auto=format&n=fwCiH4jYqddOFwab&q=85&s=69bcf1d9b347794dfed943c22e7a9ae8)

### [​](#jetbrains) JetBrains

Open `~/.continue/logs/core.log` to view the logs for the Continue plugin. The most recent logs are found at the bottom of the file.
Some JetBrains-related logs may also be found by clicking “Help” > “Show Log in Explorer/Finder”.

## [​](#download-the-latest-pre-release) Download the latest pre-release

### [​](#vs-code-2) VS Code

We are constantly making fixes and improvements to Continue, but the latest changes remain in a “pre-release” version for roughly a week so that we can test their stability. If you are experiencing issues, you can try the pre-release by going to the Continue extension page in VS Code and selecting “Switch to Pre-Release” as shown below.
![Pre-Release](https://mintcdn.com/continue-docs/fwCiH4jYqddOFwab/images/images/prerelease-9bed93e846914165d30a3b227a680d9b.png?fit=max&auto=format&n=fwCiH4jYqddOFwab&q=85&s=f7ede66db2d00d26b1153b4d4be330ae)

### [​](#jetbrains-2) JetBrains

On JetBrains, the “pre-release” happens through their Early Access Program (EAP) channel. To download the latest EAP version, enable the EAP channel:

1. Open JetBrains settings (`cmd/ctrl` + `,`) and go to “Plugins”
2. Click the gear icon at the top
3. Select “Manage Plugin Repositories…”
4. Add “<https://plugins.jetbrains.com/plugins/eap/list>” to the list
5. You’ll now always be able to download the latest EAP version from the marketplace

## [​](#download-an-older-version) Download an Older Version

If you’ve tried everything, reported an error, know that a previous version was working for you, and are waiting to hear back, you can try downloading an older version of the extension.
For VS Code, All versions are hosted on the Open VSX Registry [here](https://open-vsx.org/extension/Continue/continue). Once you’ve downloaded the extension, which will be a .vsix file, you can install it manually by following the instructions [here](https://code.visualstudio.com/docs/editor/extension-gallery#_install-from-a-vsix).
You can find older versions of the JetBrains extension on their [marketplace](https://plugins.jetbrains.com/plugin/22707-continue), which will walk you through installing from disk.

## [​](#keyboard-shortcuts-not-resolving) Keyboard shortcuts not resolving

If your keyboard shortcuts are not resolving, you may have other commands that are taking precedence over the Continue shortcuts. You can see if this is the case, and change your shortcut mappings, in the configuration of your IDE.

* [VSCode keyboard shortcuts docs](https://code.visualstudio.com/docs/getstarted/keybindings)
* [IntelliJ keyboard shortcut docs](https://www.jetbrains.com/help/idea/configuring-keyboard-and-mouse-shortcuts.html)

## [​](#still-having-trouble%3F) Still having trouble?

You can also join our Discord community [here](https://discord.gg/vapESyrFmJ) for additional support and discussions. Alternatively, you can create a GitHub issue [here](https://github.com/continuedev/continue/issues/new?assignees=&labels=bug&projects=&template=bug-report-%F0%9F%90%9B.md&title=), providing details of your problem, and we’ll be able to help you out more quickly.