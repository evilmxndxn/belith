import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import "../styles/theme.css";
import "../animations/transitions.css";
import { EntityList } from "../components/EntityList";
import { FileUpload } from "../components/FileUpload";
import { ingestEntities } from "../services/apiClient";

interface Entity {
  id: string;
  entity_type: string;
  canonical_value: string;
  confidence: { value: number };
  source: { name: string; type: string };
}

const App: React.FC = () => {
  const [entities, setEntities] = useState<Entity[]>([]);
  const [selected, setSelected] = useState<Entity | null>(null);
  const [input, setInput] = useState("");

  const handleInvestigate = async () => {
    if (!input.trim()) return;
    const usernameEntity = {
      entity_type: "username",
      canonical_value: input.trim(),
      source: { name: "manual", type: "file" },
      confidence: { value: 0.5 },
      metadata: {},
      relationships: []
    };
    const res = await ingestEntities([usernameEntity]);
    setEntities(res);
  };

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "320px 1fr 320px",
        height: "100vh",
        background: "radial-gradient(circle at top, #151b2b 0, #05070a 55%)"
      }}
    >
      <div style={{ borderRight: "1px solid var(--border)", display: "flex", flexDirection: "column" }}>
        <div style={{ padding: 16, borderBottom: "1px solid var(--border)" }}>
          <h1 style={{ margin: 0, fontSize: 18 }}>BELITH</h1>
          <p style={{ margin: "4px 0 0", fontSize: 12, color: "var(--muted)" }}>
            Behavioral Event Logging Intelligence Threat Handler
          </p>
        </div>
        <div style={{ padding: 16 }}>
          <label style={{ fontSize: 13, color: "var(--muted)" }}>
            Investigate a username
            <span title="BELITH will query OSINT identity tools like WhatsMyName and Sherlock.">
              {" "}
              What does this mean?
            </span>
          </label>
          <div style={{ marginTop: 8, display: "flex", gap: 8 }}>
            <input
              style={{
                flex: 1,
                padding: 8,
                borderRadius: 6,
                border: "1px solid var(--border)",
                background: "var(--bg-alt)",
                color: "var(--fg)"
              }}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="e.g. cyber_owen"
            />
            <button
              onClick={handleInvestigate}
              style={{
                padding: "8px 12px",
                borderRadius: 6,
                border: "none",
                background: "var(--accent)",
                color: "white",
                cursor: "pointer"
              }}
            >
              Go
            </button>
          </div>
        </div>
        <FileUpload onEntities={setEntities} />
      </div>
      <div style={{ borderRight: "1px solid var(--border)" }}>
        <EntityList entities={entities} onSelect={setSelected} />
      </div>
      <div style={{ padding: 16 }}>
        {selected ? (
          <div className="fade-in">
            <h2 style={{ marginTop: 0, fontSize: 16 }}>Entity details</h2>
            <p style={{ fontSize: 13, color: "var(--muted)" }}>
              BELITH aggregates intelligence from multiple tools and APIs into a single entity profile.
            </p>
            <pre
              style={{
                background: "var(--bg-alt)",
                borderRadius: 8,
                padding: 12,
                border: "1px solid var(--border)",
                fontSize: 12,
                maxHeight: "80vh",
                overflow: "auto"
              }}
            >
              {JSON.stringify(selected, null, 2)}
            </pre>
          </div>
        ) : (
          <div style={{ fontSize: 13, color: "var(--muted)" }}>
            Select an entity to see its fused intelligence profile. Tooltips and “What does this mean?” popovers explain
            technical concepts in plain language.
          </div>
        )}
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(<App />);
