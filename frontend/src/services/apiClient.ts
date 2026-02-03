const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export async function ingestEntities(entities: any[]): Promise<any[]> {
  const res = await fetch(`${API_BASE}/entities/ingest`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${import.meta.env.VITE_API_TOKEN || "dev-token"}`
    },
    body: JSON.stringify(entities)
  });
  if (!res.ok) {
    throw new Error(`Ingest failed: ${res.status}`);
  }
  return res.json();
}

export async function ingestFile(file: File): Promise<any[]> {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${API_BASE}/files/ingest`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${import.meta.env.VITE_API_TOKEN || "dev-token"}`
    },
    body: form
  });
  if (!res.ok) {
    throw new Error(`File ingest failed: ${res.status}`);
  }
  return res.json();
}
