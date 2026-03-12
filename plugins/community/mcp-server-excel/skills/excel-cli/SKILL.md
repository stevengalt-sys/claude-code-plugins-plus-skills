---
name: excel-cli
description: |
  Automate Microsoft Excel via the excelcli command-line tool and MCP server.
  Use when user wants to create, read, write, or manipulate Excel workbooks,
  worksheets, ranges, tables, charts, PivotTables, Power Query, DAX measures,
  or VBA macros. Trigger with phrases like "open this spreadsheet", "create an
  Excel chart", "add a pivot table", "write data to Excel", "run a VBA macro",
  "create a Power Query", or "use excelcli". Requires Windows with .NET runtime.
allowed-tools: Read, Write, Edit, Bash(excelcli:*), Bash(dotnet:*), Bash(npx:*), Glob, Grep
version: 1.0.0
author: sbroenne
license: MIT
---

# Excel CLI

## Overview

Excel MCP Server and CLI enables AI-powered automation of Microsoft Excel through natural language. It uses Excel's native COM API for zero file-corruption risk and provides 23 tool schemas covering Power Query, Power Pivot/DAX, VBA, PivotTables, charts, ranges, tables, and workbook session management.

## Prerequisites

- Windows OS (uses COM automation)
- .NET runtime installed
- Microsoft Excel installed
- MCP Server: `dotnet tool install --global Sbroenne.ExcelMcp.McpServer`
- CLI tool: `dotnet tool install --global Sbroenne.ExcelMcp.CLI`
- Close all Excel files before starting (exclusive workbook access required)

## Instructions

### Installation

Install the MCP server and CLI as global .NET tools:

```bash
dotnet tool install --global Sbroenne.ExcelMcp.McpServer
dotnet tool install --global Sbroenne.ExcelMcp.CLI
```

Auto-configure for Claude Code and other agents:

```bash
npx add-mcp "mcp-excel" --name excel-mcp
```

### Session Workflow

All Excel operations require a session. Always open a session first and close it when done.

```bash
# Open a workbook session (returns a session ID)
excelcli -q session open myfile.xlsx

# Perform operations using the session ID
excelcli -q sheet list --session <session-id>
excelcli -q range read --session <session-id> --sheet Sheet1 --range A1:D10

# Close and save when finished
excelcli -q session close --session <session-id> --save
```

### Available Resources

| Resource  | Description                              |
|-----------|------------------------------------------|
| `session` | Open, close, and manage workbook sessions |
| `sheet`   | List, create, delete, rename worksheets  |
| `table`   | Create and manage Excel tables           |
| `range`   | Read and write cell ranges and formulas  |
| `chart`   | Create and customize charts              |
| `pivot`   | Create and modify PivotTables            |
| `query`   | Power Query operations (M language)      |
| `measure` | DAX measure operations                   |
| `vba`     | Execute VBA macros                       |

### Key Flags

- `-q` — Quiet mode: suppress banner, output JSON only (use for scripting)
- `--help` — Available at any command level for usage details
- `--output-format json` — Wrap output in `{ success, data, timestamp }`

## Output

Default: **data-only** (raw output for token efficiency).
Use `-q` flag for clean JSON output suitable for parsing.
Use `--output-format json` for structured `{ success, data, timestamp }` wrapping.

## Error Handling

- If `excelcli` is not found, install it: `dotnet tool install --global Sbroenne.ExcelMcp.CLI`
- If session fails to open, ensure all Excel instances are closed first
- If COM errors occur, verify Excel is installed and accessible
- Use `excelcli --help` or `excelcli <resource> --help` for command-specific guidance

## Examples

### Create a workbook and write data

```bash
excelcli -q session open newfile.xlsx
excelcli -q range write --session <id> --sheet Sheet1 --range A1 --value "Name,Age,City"
excelcli -q session close --session <id> --save
```

### Create a chart from data

```bash
excelcli -q session open data.xlsx
excelcli -q chart create --session <id> --sheet Sheet1 --range A1:B10 --type bar
excelcli -q session close --session <id> --save
```

### Run a VBA macro

```bash
excelcli -q session open macros.xlsm
excelcli -q vba run --session <id> --macro "MyMacro"
excelcli -q session close --session <id> --save
```

## Resources

- [Excel MCP Server](https://excelmcpserver.dev/)
- [GitHub Repository](https://github.com/sbroenne/mcp-server-excel)
- [Installation Guide](https://excelmcpserver.dev/installation/)
- [MCP Protocol Reference](https://modelcontextprotocol.io/)
