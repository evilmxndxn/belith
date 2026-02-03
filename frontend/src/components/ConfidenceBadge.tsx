import React from "react";

interface Props {
  value: number;
}

export const ConfidenceBadge: React.FC<Props> = ({ value }) => {
  const pct = Math.round(value * 100);
  let color = "#4f8cff";
  if (value >= 0.8) color = "#4fff9a";
  else if (value <= 0.3) color = "#ff4f6b";

  return (
    <span
      title="How sure BELITH is about this entity, based on all sources."
      style={{
        padding: "2px 8px",
        borderRadius: 999,
        backgroundColor: "rgba(0,0,0,0.4)",
        border: `1px solid ${color}`,
        fontSize: 12
      }}
    >
      Confidence: <span style={{ color }}>{pct}%</span>
    </span>
  );
};
