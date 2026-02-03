# BELITH OPSEC Guidelines

## Defaults
- Passive reconnaissance first.
- API keys stored only in environment variables.
- Adapter clients enforce request timeouts.

## Adapter Controls
- Each adapter declares rate limits and OPSEC notes in `config.py`.
- No adapter calls another adapter.
- Tool execution is isolated and not triggered from the UI.

## UI Safety
- UI panels only call backend endpoints.
- Dangerous tools should be flagged in the UI before execution.
