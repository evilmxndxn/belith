import React, { useState } from "react";
import { ingestFile } from "../services/apiClient";

interface Props {
  onEntities: (entities: any[]) => void;
}

export const FileUpload: React.FC<Props> = ({ onEntities }) => {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setBusy(true);
    setError(null);
    try {
      const entities = await ingestFile(file);
      onEntities(entities);
    } catch (err: any) {
      setError(err.message || "Upload failed");
    } finally {
      setBusy(false);
    }
  };

  return (
    <div style={{ padding: 16 }}>
      <label style={{ fontSize: 13, color: "var(--muted)" }}>
        Upload data lists (CSV, JSON, TXT). BELITH will auto-detect and normalize content.
      </label>
      <div style={{ marginTop: 8 }}>
        <input type="file" onChange={handleChange} disabled={busy} />
      </div>
      {busy && <div style={{ fontSize: 12, color: "var(--muted)" }}>Processing file…</div>}
      {error && (
        <div style={{ fontSize: 12, color: "var(--danger)", marginTop: 4 }}>
          {error} — <span title="BELITH avoids logging file contents to protect OPSEC.">What does this mean?</span>
        </div>
      )}
    </div>
  );
};
