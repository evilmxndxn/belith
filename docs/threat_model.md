# BELITH Threat Model

## Assets
- API keys stored in environment variables.
- Aggregated threat intelligence entities and relationships.
- Uploaded files in `data/uploads`.

## Trust Boundaries
- External API providers (VirusTotal, Shodan, etc.).
- User-supplied inputs and uploaded files.
- Tool and API outputs before normalization.

## Threats & Mitigations
- **API key leakage**: keys are loaded from env and never logged.
- **Malicious input**: inputs are treated as data and normalized; no direct tool execution in UI.
- **API abuse**: rate limits are configured per adapter.
- **Untrusted output**: adapters parse and normalize output deterministically.

## Residual Risk
- External data sources can be unavailable or rate limited. BELITH reports failures through adapter responses and does not block other enrichment paths.
