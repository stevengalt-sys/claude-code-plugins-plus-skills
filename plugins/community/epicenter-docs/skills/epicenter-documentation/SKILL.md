---
name: epicenter-documentation
description: |
  Activate when working with the Epicenter ecosystem or its apps like Whispering.
  Provides documentation for Epicenter's local-first architecture, Svelte 5 + Tauri stack,
  plain text and SQLite storage patterns, and AI model integration.
  Trigger phrases: "epicenter", "whispering app", "local-first apps", "epicenter transcription".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(pnpm:*), Bash(npm:*), Bash(cargo:*), WebFetch
version: 1.0.0
author: EpicenterHQ <hello@epicenter.so>
---

# Epicenter Documentation

Reference guide for the Epicenter ecosystem — open-source, local-first apps sharing plain text and SQLite storage.

## Overview

Epicenter stores all data — notes, transcripts, chat histories — in a single folder of plain text and SQLite. Every app shares this memory. Built with Rust, Svelte 5, and Tauri.

## Architecture

### Core Principles
- **Local-first:** Data stays on your machine, works offline
- **Plain text + SQLite:** Files you own — grep, Git, Obsidian compatible
- **Open source:** Delete the app, keep your work
- **CRDT sync:** Conflict-free offline-first data synchronization

### Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | Svelte 5 (97% code sharing desktop/web) |
| Desktop | Tauri (Rust, ~22MB binary) |
| Storage | Plain text files + SQLite |
| Sync | CRDTs |
| AI | OpenAI, Anthropic, Google Gemini, Groq, local LLMs |

### Repository Structure
```
epicenter/
├── apps/
│   └── whispering/          # Transcription app
│       ├── src/             # Svelte 5 components
│       ├── src-tauri/       # Rust/Tauri desktop layer
│       └── package.json
├── packages/                # Shared libraries
└── pnpm-workspace.yaml
```

## Whispering App

The first Epicenter app — voice transcription with AI transformations.

### Features
- Voice-activated hands-free mode (no button holding)
- Local transcription via whisper.cpp (audio never leaves device)
- Cloud transcription via OpenAI Whisper API
- Customizable AI transformations (any prompt, any model)
- Desktop: Mac (Intel + Apple Silicon), Windows, Linux
- Web: any modern browser
- Three-layer architecture with build-time platform detection

### Development Setup
```bash
git clone https://github.com/EpicenterHQ/epicenter.git
cd epicenter && pnpm install

# Web development
cd apps/whispering && pnpm dev

# Desktop development (requires Rust toolchain)
cd apps/whispering && pnpm tauri dev

# Build desktop app
cd apps/whispering && pnpm tauri build
```

### AI Model Configuration
Whispering supports multiple AI providers for transformations:
- **OpenAI:** GPT-4o, GPT-4, GPT-3.5 — set `OPENAI_API_KEY`
- **Anthropic:** Claude 4.5/4.6 models — set `ANTHROPIC_API_KEY`
- **Google Gemini:** Via API key
- **Groq:** Fast inference with Llama models
- **Local LLMs:** Via compatible API endpoints

Users bring their own API keys. Audio goes directly from device to API — no servers in between.

## Data Storage Patterns

### File System Layout
All user data lives in a single directory:
```
~/.epicenter/
├── transcriptions/     # Plain text transcription files
├── settings.db         # SQLite for app settings
├── transforms/         # AI transformation configs
└── models/             # Local model references
```

### Migration
Desktop apps migrating from IndexedDB to file system:
- Toast notification with "Migrate Now" button on first launch
- Guided migration assistant
- Optional but recommended for better performance

### Compatibility
- Edit files in VS Code or any text editor
- Search with grep or ripgrep
- Version control with Git
- Open notes in Obsidian
- Script with standard Unix tools

## Instructions

When working with Epicenter:
1. Respect the local-first philosophy — data should stay on the user's machine
2. Use plain text and SQLite for storage, never proprietary formats
3. Follow Svelte 5 patterns (runes, snippets) for frontend code
4. Use Tauri APIs for desktop-specific features
5. Support multiple AI providers — never hard-code a single provider
6. Ensure offline functionality for core features
7. Reference https://github.com/EpicenterHQ/epicenter for latest APIs

## Resources

- **Repository:** https://github.com/EpicenterHQ/epicenter
- **Website:** https://epicenter.so
- **YC Profile:** https://www.ycombinator.com/companies/epicenter
