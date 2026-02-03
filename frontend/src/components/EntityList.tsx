import React from "react";
import { ConfidenceBadge } from "./ConfidenceBadge";

interface Entity {
  id: string;
  entity_type: string;
  canonical_value: string;
  confidence: { value: number };
  source: { name: string; type: string };
}

interface Props {
  entities: Entity[];
  onSelect: (e: Entity) => void;
}

export const EntityList: React.FC<Props> = ({ entities, onSelect }) => {
  return (
    <div style={{ padding: 16, overflowY: "auto", maxHeight: "100%" }}>
      {entities.map((e) => (
        <div
          key={e.id}
          className="fade-in"
          style={{
            padding: 12,
            marginBottom: 8,
            borderRadius: 8,
            background: "var(--bg-alt)",
            border: "1px solid var(--border)",
            cursor: "pointer"
          }}
          onClick={() => onSelect(e)}
        >
          <div style={{ fontSize: 13, color: "var(--muted)" }}>{e.entity_type.toUpperCase()}</div>
          <div style={{ fontSize: 15, fontWeight: 500 }}>{e.canonical_value}</div>
          <div style={{ display: "flex", justifyContent: "space-between", marginTop: 4 }}>
            <span style={{ fontSize: 12, color: "var(--muted)" }}>Source: {e.source.name}</span>
            <ConfidenceBadge value={e.confidence.value} />
          </div>
        </div>
      ))}
    </div>
  );
};
