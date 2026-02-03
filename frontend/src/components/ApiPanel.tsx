import { useState } from 'react';
import { ApiAdapter, EnrichmentResponse } from '../services/api';
import '../styles/panel.css';

interface ApiPanelProps {
  panel: ApiAdapter;
  onRun: (input: string) => Promise<EnrichmentResponse>;
  globalLoading: boolean;
}

export default function ApiPanel({ panel, onRun, globalLoading }: ApiPanelProps) {
  const [inputValue, setInputValue] = useState('');
  const [response, setResponse] = useState<EnrichmentResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleRun = async () => {
    if (!inputValue && panel.name !== 'certstream') {
      setError('Input required.');
      return;
    }
    setError(null);
    setLoading(true);
    try {
      const result = await onRun(inputValue || 'listen');
      setResponse(result);
    } catch (err) {
      setError('Failed to enrich. Check backend connectivity and API keys.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`panel-card ${panel.enabled === false ? 'disabled' : ''}`}>
      <div className="panel-header">
        <div>
          <h2>{panel.label}</h2>
          <p>{panel.inputLabel}</p>
        </div>
        <div className="pill-stack">
          <span className="pill subtle">{panel.type?.toUpperCase() || 'API'}</span>
          <span className={panel.requiresKey ? 'pill alert' : 'pill'}>
            {panel.requiresKey ? 'API Key' : 'No Key'}
          </span>
        </div>
      </div>
      <div className="panel-input">
        <input
          value={inputValue}
          onChange={(event) => setInputValue(event.target.value)}
          placeholder={panel.inputLabel}
        />
        <button onClick={handleRun} disabled={loading || globalLoading}>
          {loading ? 'Running…' : 'Run'}
        </button>
      </div>
      {error && <p className="panel-error">{error}</p>}
      {response && (
        <div className="panel-results">
          <p className="panel-section">Entities</p>
          <div className="chip-row">
            {response.entities.length ? (
              response.entities.map((entity) => (
                <span key={entity.id} className="entity-chip">
                  {entity.type}: {entity.value}
                </span>
              ))
            ) : (
              <span className="empty">No entities returned.</span>
            )}
          </div>
          <p className="panel-section">Relationships</p>
          <div className="chip-row">
            {response.relationships.length ? (
              response.relationships.map((rel) => (
                <span key={rel.id} className="entity-chip">
                  {rel.relationship_type}
                </span>
              ))
            ) : (
              <span className="empty">No relationships returned.</span>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
