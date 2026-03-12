# mcp-server-excel

Automate Microsoft Excel through natural language via MCP server and CLI.

## Features

- **Power Query & M** — Create, view, import, export, update, and delete queries
- **Power Pivot & DAX** — Manage DAX measures, relationships, and data models
- **VBA Macros** — Execute and manage VBA code
- **PivotTables** — Create and modify PivotTables
- **Charts & Formatting** — Create and customize charts
- **Range Operations** — Read and write data to cell ranges
- **Tables** — Create and manage Excel structured tables
- **Workbook Sessions** — Manage Excel file sessions and lifecycle

## Installation

```bash
# Install MCP Server
dotnet tool install --global Sbroenne.ExcelMcp.McpServer

# Install CLI
dotnet tool install --global Sbroenne.ExcelMcp.CLI

# Auto-configure for Claude Code
npx add-mcp "mcp-excel" --name excel-mcp
```

## Requirements

- Windows OS
- .NET runtime
- Microsoft Excel

## Skills

- **excel-cli** — Automate Excel workbooks via the `excelcli` command-line tool

## Links

- [Excel MCP Server](https://excelmcpserver.dev/)
- [GitHub](https://github.com/sbroenne/mcp-server-excel)

## Contributors

- sbroenne
