# Microsoft Docs MCP

Official Microsoft Learn MCP server that provides real-time, trusted Microsoft documentation and code samples. No API keys, logins, or sign-ups required.

## Tools

- **microsoft_docs_search** - Search through Microsoft's latest official documentation
- **microsoft_docs_fetch** - Fetch a complete documentation article by URL or path
- **microsoft_code_sample_search** - Search through Microsoft code samples with language-specific filtering

## Installation

```bash
ccpi install microsoftdocs/mcp
```

Or manually add the MCP server:

```bash
claude mcp add microsoft-learn --transport http --url https://learn.microsoft.com/api/mcp
```

## Configuration

This plugin uses a remote MCP server (no local process required):

```json
{
  "mcpServers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    }
  }
}
```

## Credits

Built by [Microsoft](https://github.com/MicrosoftDocs/mcp).
