# security-guidance

PreToolUse security reminder hook for Claude Code. Catches 12 common security anti-patterns in Edit/Write/MultiEdit operations BEFORE they happen — command injection (exec, os.system, subprocess shell=True), XSS (innerHTML, dangerouslySetInnerHTML, document.write), SQL injection (f-string queries, .format), unsafe deserialization (pickle, yaml.unsafe_load), code injection (eval, new Function), and GitHub Actions workflow injection. Session-state caching prevents duplicate warnings; 30-day auto-cleanup. Disable per-session with ENABLE_SECURITY_REMINDER=0. Ported from David Dworken at Anthropic.

## Skills

- `security-guidance`

## Author

Alireza Rezvani

## License

MIT
