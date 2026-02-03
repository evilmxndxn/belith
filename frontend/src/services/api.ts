export interface ApiAdapter {
  name: string;
  label: string;
  inputLabel: string;
  requiresKey: boolean;
  enabled?: boolean;
  type?: 'api' | 'tool';
}

export interface CatalogItem {
  name: string;
  type: 'api' | 'tool';
}

export interface Entity {
  id: string;
  type: string;
  value: string;
}

export interface Relationship {
  id: string;
  relationship_type: string;
}

export interface EnrichmentResponse {
  entities: Entity[];
  relationships: Relationship[];
  metadata: Record<string, unknown>;
}

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000';

export async function fetchAdapters(): Promise<string[]> {
  const response = await fetch(`${API_BASE}/adapters`);
  if (!response.ok) {
    return [];
  }
  const data = await response.json();
  return data.adapters || [];
}

export async function fetchCatalog(): Promise<CatalogItem[]> {
  const response = await fetch(`${API_BASE}/catalog`);
  if (!response.ok) {
    return [];
  }
  const data = await response.json();
  return data.items || [];
}

export async function runEnrichment(adapter: string, input: string): Promise<EnrichmentResponse> {
  const params = new URLSearchParams({ input_value: input });
  const response = await fetch(`${API_BASE}/adapters/${adapter}/enrich?${params.toString()}`, {
    method: 'POST',
  });
  if (!response.ok) {
    throw new Error('Failed to enrich');
  }
  return response.json();
}
