# Microsoft Docs MCP

An MCP server that provides tools to search and read Microsoft Learn documentation.

## Tools

- **search_microsoft_learn** - Search Microsoft Learn documentation
- **get_microsoft_learn_page** - Get the full content of a Microsoft Learn documentation page

## Installation

```bash
ccpi install microsoftdocs/mcp
```

## Configuration

This plugin uses the following MCP server configuration:

```json
{
  "mcpServers": {
    "microsoft-docs": {
      "command": "npx",
      "args": ["-y", "@nicholasgriffintn/microsoft-docs-mcp"]
    }
  }
}
```

## Credits

Built by [Nicholas Griffin](https://github.com/nicholasgriffintn).
