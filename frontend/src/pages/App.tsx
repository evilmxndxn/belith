import { useEffect, useMemo, useState } from 'react';
import ApiPanel from '../components/ApiPanel';
import { ApiAdapter, CatalogItem, fetchCatalog, runEnrichment } from '../services/api';
import '../styles/app.css';

const baseInputs: Record<string, string> = {
  api: 'Indicator or query input',
  tool: 'Target input (host, file, or username)',
};

const requiresKey = new Set([
  'virustotal',
  'shodan',
  'alienvault_otx',
  'greynoise',
  'whoisxml',
  'abuseipdb',
  'phishtank',
]);

const toLabel = (name: string) => {
  const trimmed = name.startsWith('api_') ? name.replace(/^api_/, '') : name;
  return trimmed
    .split('_')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
};

export default function App() {
  const [catalog, setCatalog] = useState<CatalogItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [filter, setFilter] = useState('');

  useEffect(() => {
    fetchCatalog()
      .then((items) => setCatalog(items))
      .catch(() => setCatalog([]));
  }, []);

  const panels = useMemo<ApiAdapter[]>(() => {
    return catalog.map((item) => ({
      name: item.name,
      label: toLabel(item.name),
      inputLabel: baseInputs[item.type] || 'Input',
      requiresKey: requiresKey.has(item.name),
      type: item.type,
    }));
  }, [catalog]);

  const filteredPanels = panels.filter((panel) =>
    panel.label.toLowerCase().includes(filter.trim().toLowerCase())
  );

  return (
    <div className="app-shell">
      <header className="app-header">
        <div>
          <p className="app-kicker">BELITH</p>
          <h1>Behavioral Event Logging Intelligence Threat Handler</h1>
          <p className="app-subtitle">
            Unified enrichment, normalization, and fusion for threat intelligence entities.
          </p>
        </div>
        <div className="status-pill">OPSEC: Passive</div>
      </header>

      <section className="toolbar">
        <input
          className="search"
          placeholder="Filter adapters..."
          value={filter}
          onChange={(event) => setFilter(event.target.value)}
        />
        <span className="counter">{filteredPanels.length} adapters</span>
      </section>

      <section className="panel-grid">
        {filteredPanels.map((panel) => (
          <ApiPanel
            key={panel.name}
            panel={panel}
            onRun={async (input) => {
              setLoading(true);
              try {
                return await runEnrichment(panel.name, input);
              } finally {
                setLoading(false);
              }
            }}
            globalLoading={loading}
          />
        ))}
      </section>
    </div>
  );
}
