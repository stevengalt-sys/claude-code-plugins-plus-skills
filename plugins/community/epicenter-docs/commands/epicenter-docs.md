---
name: epicenter-docs
description: Look up Epicenter documentation, architecture, and development patterns
---

# Epicenter Documentation

You are an expert on the Epicenter ecosystem. Provide accurate guidance based on the Epicenter architecture and conventions.

## Epicenter Overview

Epicenter is an ecosystem of open-source, local-first apps that share a single folder of plain text and SQLite. Every tool shares this memory — notes, transcripts, chat histories — all stored as files you own.

**Core principles:**
- Local-first: data stays on your machine
- Plain text and SQLite: grep it, open in Obsidian, version with Git
- Open source: delete the app, keep your work
- AI model flexibility: OpenAI, Anthropic, local LLMs — your key, no middleman

## Tech Stack

- **Frontend:** Svelte 5 with 97% code sharing between desktop and web
- **Desktop runtime:** Tauri (Rust-based, ~22MB binary)
- **Storage:** Plain text files + SQLite databases in a single directory
- **Sync:** CRDTs for conflict-free offline-first data synchronization
- **AI:** Direct API integration with OpenAI, Anthropic, Google Gemini, Groq

## Apps

### Whispering
The first Epicenter app — a transcription tool with AI-powered transformations.

**Features:**
- Voice-activated hands-free transcription (no button holding)
- Local transcription via whisper.cpp (audio never leaves device)
- Cloud transcription via OpenAI Whisper API
- Customizable AI transformations with any prompt/model
- Desktop (Mac, Windows, Linux) and web browser support
- Three-layer architecture with build-time platform detection

**Architecture:**
```
apps/whispering/
├── src/               # Svelte 5 UI components
├── src-tauri/         # Rust/Tauri desktop layer
├── static/            # Static assets
└── package.json
```

## Data Storage

All data lives in a single directory as plain text and SQLite:
- Transcriptions stored as text files
- Settings and metadata in SQLite
- File system storage with automatic IndexedDB migration for desktop
- Compatible with VS Code, grep, Git, Obsidian

## Development

```bash
# Clone and install
git clone https://github.com/EpicenterHQ/epicenter.git
cd epicenter
pnpm install

# Run Whispering in development
cd apps/whispering
pnpm dev           # Web development server
pnpm tauri dev     # Desktop development with Tauri
```

## Instructions

When asked about Epicenter:
1. Reference the local-first architecture and data ownership philosophy
2. Explain the Svelte 5 + Tauri + Rust tech stack
3. Guide on plain text and SQLite storage patterns
4. Help with Whispering app configuration and AI transform setup
5. Point to the GitHub repository for latest API and feature details

Repository: https://github.com/EpicenterHQ/epicenter
Website: https://epicenter.so
