# -*- coding: utf-8 -*-
"""
generate_analytics.py — Reproducible analytics for the research paper:
"Institutional Inclusive-Language Guidelines as Machine-Consumable Skill
Libraries for LLM Agents".

Computes corpus/skill metrics, writes CSV datasets to ../data, and renders all
paper figures to ../figures. Run from anywhere; paths are resolved relative to
this file.

Usage:  python generate_analytics.py
"""
import csv
import os
import re
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))   # repo root
SKILLS = os.path.join(ROOT, "skills")
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
FIGS = os.path.abspath(os.path.join(HERE, "..", "figures"))
os.makedirs(DATA, exist_ok=True)
os.makedirs(FIGS, exist_ok=True)

plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 150, "font.size": 9,
    "axes.titlesize": 10, "axes.titleweight": "bold",
})

TIER_COLORS = {
    "core": "#4C72B0", "gender": "#DD8452", "identity-domains": "#55A868",
    "communication": "#C44E52", "workflows": "#8172B3", "meta": "#937860",
}

# --------------------------------------------------------------------------
# 1. Skill inventory + per-skill metrics
# --------------------------------------------------------------------------
SKILL_FILES = []  # (tier, skill_id, path)
for dirpath, _dirs, files in os.walk(SKILLS):
    for f in files:
        if f == "SKILL.md":
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, SKILLS).replace("\\", "/")
            tier = rel.split("/")[0]
            sid = re.search(r"^skill:\s*(.+)$",
                            open(p, encoding="utf-8").read(), re.M).group(1).strip()
            SKILL_FILES.append((tier, sid, p))
SKILL_FILES.sort(key=lambda t: t[1])

def table_rows(text):
    n = 0
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and not re.match(r"^\|[\s:\-|]+\|?\s*$", s) \
                and not s.lower().startswith("| avoid") and not s.lower().startswith("| term"):
        # header rows start with '| Avoid' or '| Term'
            n += 1
    return max(n - sum(1 for line in text.splitlines()
                       if line.strip().lower().startswith(("| avoid", "| term"))), 0)

def data_rows(text):
    """Count markdown table body rows (exclude separator + header rows)."""
    n = 0
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        if re.match(r"^\|[\s:\-|]+\|?\s*$", s):      # separator row
            continue
        first = re.split(r"\|", s)[1].strip().lower()
        if first in ("avoid", "term", "skill id", "document", "level", "id",
                     "situation", "antecedent", "order", "finding #"):
            continue
        n += 1
    return n

metrics = []
for tier, sid, path in SKILL_FILES:
    txt = open(path, encoding="utf-8").read()
    rules = len(re.findall(r"\*\*R\d+\s*[\u2014\-]", txt))
    grefs = len(set(re.findall(r"\bG(\d+)\b", txt)))
    srcs = len(re.findall(r"^sources:\s*\[(.+?)\]", txt, re.M | re.S)) and \
        len(re.split(r",", re.search(r"^sources:\s*\[(.+?)\]", txt, re.M | re.S).group(1)))
    metrics.append({
        "skill_id": sid, "tier": tier,
        "size_kb": round(os.path.getsize(path) / 1024, 2),
        "lines": txt.count("\n") + 1,
        "rules": rules,
        "table_rows": data_rows(txt),
        "guardrail_refs": grefs,
        "n_sources": srcs,
    })

# reference tables (non-SKILL.md knowledge assets)
ref_path = os.path.join(SKILLS, "gender", "gender-inclusive-rewriting",
                        "references", "substitution-tables.md")
ref_txt = open(ref_path, encoding="utf-8").read()

with open(os.path.join(DATA, "skill_metrics.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(metrics[0].keys()))
    w.writeheader(); w.writerows(metrics)

# --------------------------------------------------------------------------
# 2. Source corpus dataset
# --------------------------------------------------------------------------
corpus = [
    ("EIGE-2019",     "European Institute for Gender Equality", 2019, 65,
     "Gender-sensitive communication toolkit: principles, 3-category taxonomy, solutions tables, checklists, worked audits"),
    ("EIGE-2024",     "European Institute for Gender Equality", 2024, 32,
     "Words Matter: gender-inclusive approach, intersectionality, communication formats incl. AI prompts"),
    ("UNW-EN",        "UN Women",                               None,  7,
     "Gender-inclusive language guidelines (EN): strategies A/B/C, checklist"),
    ("CAPE-2023",     "Canadian Association of Professional Employees", 2023, 7,
     "Inclusive writing techniques; singular they; legal-text meaning preservation; forms"),
    ("IBEC-2015",     "IBEC (HR Unit)",                         2015,  8,
     "Workplace gender-neutral language: titles, biased terms, correspondence"),
    ("INTELLECT-2022","Intellect Books",                        2022, 19,
     "Age, class, disability, ethnicity, LGBTQ+, religion term standards; editorial guardrails"),
]
with open(os.path.join(DATA, "source_corpus.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["source_key", "publisher", "year", "pages", "focus"])
    w.writerows(corpus)

# --------------------------------------------------------------------------
# 3. Traceability matrix (skill x source; 2=primary, 1=supporting, 0=none)
# --------------------------------------------------------------------------
TRACE = {
    "core.inclusive-language-core":      {"EIGE-2019": 2, "EIGE-2024": 2, "UNW-EN": 1},
    "gender.gender-inclusive-rewriting": {"UNW-EN": 2, "EIGE-2019": 1, "CAPE-2023": 1, "IBEC-2015": 1, "EIGE-2024": 1},
    "gender.pronoun-strategy":           {"EIGE-2019": 2, "CAPE-2023": 1, "UNW-EN": 1, "INTELLECT-2022": 1, "EIGE-2024": 1},
    "gender.stereotype-detection":       {"EIGE-2019": 2, "EIGE-2024": 1, "IBEC-2015": 1, "INTELLECT-2022": 1},
    "gender.address-and-titles":         {"IBEC-2015": 2, "EIGE-2019": 2, "CAPE-2023": 1, "UNW-EN": 1},
    "gender.formal-legal-texts":         {"CAPE-2023": 2, "EIGE-2019": 1, "UNW-EN": 1},
    "identity-domains.disability-language": {"INTELLECT-2022": 2, "EIGE-2024": 1},
    "identity-domains.ethnicity-language":  {"INTELLECT-2022": 2, "EIGE-2024": 1},
    "identity-domains.lgbtqia-language":    {"INTELLECT-2022": 2, "UNW-EN": 1, "EIGE-2024": 1},
    "identity-domains.age-language":        {"INTELLECT-2022": 2, "EIGE-2024": 1},
    "identity-domains.class-language":      {"INTELLECT-2022": 2, "EIGE-2024": 1},
    "identity-domains.religion-language":   {"INTELLECT-2022": 2},
    "communication.multimodal-inclusion":   {"EIGE-2024": 2, "EIGE-2019": 1},
    "communication.ai-content-generation":  {"EIGE-2024": 2, "EIGE-2019": 1},
    "workflows.document-audit":             {"EIGE-2019": 2, "UNW-EN": 1, "EIGE-2024": 1},
}
SRC_ORDER = ["EIGE-2019", "EIGE-2024", "UNW-EN", "CAPE-2023", "IBEC-2015", "INTELLECT-2022"]
mat = np.zeros((len(TRACE), len(SRC_ORDER)), dtype=int)
skill_order = list(TRACE.keys())
for i, sk in enumerate(skill_order):
    for j, sc in enumerate(SRC_ORDER):
        mat[i, j] = TRACE[sk].get(sc, 0)
with open(os.path.join(DATA, "traceability_matrix.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["skill_id"] + SRC_ORDER)
    for i, sk in enumerate(skill_order):
        w.writerow([sk] + mat[i].tolist())

# --------------------------------------------------------------------------
# 4. Creation log (from filesystem timestamps)
# --------------------------------------------------------------------------
artifacts = []
for dirpath, _d, files in os.walk(os.path.join(ROOT, "skills")):
    for f in files:
        p = os.path.join(dirpath, f)
        artifacts.append((os.path.getctime(p), os.path.relpath(p, ROOT)))
artifacts.append((os.path.getctime(os.path.join(ROOT, "README.md")), "README.md"))
artifacts.sort()
with open(os.path.join(DATA, "creation_log.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["created_at", "artifact"])
    for ts, rel in artifacts:
        w.writerow([datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"), rel.replace("\\", "/")])

# --------------------------------------------------------------------------
# 5. Mapping counts: substitution sections + identity-domain tables
# --------------------------------------------------------------------------
def section_rows(text):
    """Rows per '## N. Title' section of substitution-tables.md."""
    out, cur = [], None
    for line in text.splitlines():
        m = re.match(r"^##\s+(\d+)\.\s+(.+)$", line.strip())
        if m:
            if cur: out.append(cur)
            cur = [m.group(1) + ". " + m.group(2), 0]
        elif cur is not None:
            s = line.strip()
            if s.startswith("|") and not re.match(r"^\|[\s:\-|]+\|?\s*$", s) \
                    and not s.lower().startswith(("| avoid",)):
                cur[1] += 1
    if cur: out.append(cur)
    # each section has one header row ('| Avoid | Use |') -> subtract 1
    return [(t, max(c - 1, 0)) for t, c in out]

sub_sections = section_rows(ref_txt)
dom_counts = []
for tier, sid, path in SKILL_FILES:
    if tier == "identity-domains":
        dom_counts.append((sid.split(".", 1)[1], data_rows(open(path, encoding="utf-8").read())))
with open(os.path.join(DATA, "mapping_counts.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["dataset", "item", "avoid_prefer_mappings"])
    for t, c in sub_sections: w.writerow(["substitution-tables.md", t, c])
    for t, c in dom_counts:   w.writerow(["identity-domain skills", t, c])

TOTAL_MAPPINGS = sum(c for _, c in sub_sections) + sum(c for _, c in dom_counts)

# ==========================================================================
# FIGURES
# ==========================================================================
short = {m["skill_id"]: m["skill_id"].split(".", 1)[1] for m in metrics}

# ---- Fig 01: creation timeline -------------------------------------------
times = [datetime.fromtimestamp(ts) for ts, _ in artifacts]
cum = np.arange(1, len(artifacts) + 1)
fig, ax = plt.subplots(figsize=(8.6, 3.6))
ax.step([t.minute * 60 + t.second for t in times], cum, where="post",
        color="#4C72B0", lw=1.6)
ax.scatter([t.minute * 60 + t.second for t in times], cum, s=22,
           color="#4C72B0", zorder=3)
x0 = times[0].minute * 60 + times[0].second
ax.set_xticks(np.linspace(x0, times[-1].minute * 60 + times[-1].second, 7))
ax.set_xticklabels([t.strftime("%H:%M:%S") for t in
                    [datetime.combine(times[0].date(), times[0].time()) +
                     __import__("datetime").timedelta(seconds=s - x0)
                     for s in np.linspace(x0, times[-1].minute * 60 + times[-1].second, 7)]])
ax.annotate("meta layer\n(ARCHITECTURE,\nGUARDRAILS, SOURCES)",
            xy=(x0 + 40, 3), xytext=(18, 7.2), fontsize=7.5,
            arrowprops=dict(arrowstyle="->", lw=.8))
idx_lgb = next(i for i, (_, r) in enumerate(artifacts) if "lgbtqia" in r)
ax.annotate("reroute correction #1\n(lgbtqia/ethnicity)",
            xy=(times[idx_lgb].minute * 60 + times[idx_lgb].second, idx_lgb + 1),
            xytext=(-5, 30), textcoords="offset points", fontsize=7.5,
            arrowprops=dict(arrowstyle="->", lw=.8, color="#C44E52"), color="#C44E52")
idx_mm = next(i for i, (_, r) in enumerate(artifacts) if "multimodal" in r)
ax.annotate("reroute correction #2\n(class/multimodal)",
            xy=(times[idx_mm].minute * 60 + times[idx_mm].second, idx_mm + 1),
            xytext=(12, -34), textcoords="offset points", fontsize=7.5,
            arrowprops=dict(arrowstyle="->", lw=.8, color="#C44E52"), color="#C44E52")
ax.set_xlabel("wall-clock time (session 2026-08-21)")
ax.set_ylabel("cumulative artifacts created")
ax.set_title("Fig. 1 — Artifact creation timeline (single authoring session)")
ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(os.path.join(FIGS, "fig01_creation_timeline.png")); plt.close(fig)

# ---- Fig 02: rules per skill ---------------------------------------------
mm = sorted(metrics, key=lambda m: m["rules"])
fig, ax = plt.subplots(figsize=(8.6, 4.6))
ys = np.arange(len(mm))
ax.barh(ys, [m["rules"] for m in mm],
        color=[TIER_COLORS[m["tier"]] for m in mm])
ax.set_yticks(ys); ax.set_yticklabels([short[m["skill_id"]] for m in mm], fontsize=8)
for y, m in zip(ys, mm):
    ax.text(m["rules"] + .15, y, str(m["rules"]), va="center", fontsize=8)
ax.set_xlabel("number of imperative rules (R1..Rn)")
ax.set_title("Fig. 2 — Rule density per skill")
ax.legend(handles=[Patch(color=c, label=t) for t, c in TIER_COLORS.items()],
          fontsize=7, loc="lower right")
ax.grid(axis="x", alpha=.3)
fig.tight_layout(); fig.savefig(os.path.join(FIGS, "fig02_rules_per_skill.png")); plt.close(fig)

# ---- Fig 03: scatter size vs rules ---------------------------------------
fig, ax = plt.subplots(figsize=(7.6, 5.2))
for m in metrics:
    ax.scatter(m["size_kb"], m["rules"],
               s=28 + m["table_rows"] * 3.2,
               color=TIER_COLORS[m["tier"]], alpha=.85, edgecolor="k", linewidth=.4, zorder=3)
    dy = 8 if m["skill_id"] not in ("gender.pronoun-strategy",
                                    "identity-domains.religion-language") else -13
    ax.annotate(short[m["skill_id"]],
                (m["size_kb"], m["rules"]), textcoords="offset points",
                xytext=(0, dy), ha="center", fontsize=6.6)
xs = [m["size_kb"] for m in metrics]; ys = [m["rules"] for m in metrics]
z = np.polyfit(xs, ys, 1)
xr = np.linspace(min(xs) - .3, max(xs) + .3, 50)
ax.plot(xr, np.polyval(z, xr), "--", color="grey", lw=1,
        label=f"OLS fit: y = {z[0]:.1f}x + {z[1]:.1f}  (r = {np.corrcoef(xs, ys)[0,1]:.2f})")
ax.set_xlabel("SKILL.md size (KB)"); ax.set_ylabel("imperative rules (count)")
ax.set_title("Fig. 3 — Skill size vs. rule density\n(marker area = avoid->prefer mappings in file)")
ax.legend(fontsize=7.5); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(os.path.join(FIGS, "fig03_scatter_size_vs_rules.png")); plt.close(fig)

# ---- Fig 04: traceability heatmap ----------------------------------------
fig, ax = plt.subplots(figsize=(7.8, 6.4))
im = ax.imshow(mat, cmap="Blues", vmin=0, vmax=2, aspect="auto")
ax.set_xticks(range(len(SRC_ORDER)))
ax.set_xticklabels(SRC_ORDER, rotation=35, ha="right", fontsize=8)
ax.set_yticks(range(len(skill_order)))
ax.set_yticklabels([short[s] for s in skill_order], fontsize=7.5)
for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        v = mat[i, j]
        if v:
            ax.text(j, i, str(v), ha="center", va="center", fontsize=7.5,
                    color="white" if v == 2 else "black")
ax.set_title("Fig. 4 — Source-to-skill traceability matrix\n(2 = primary source, 1 = supporting, blank = none)")
fig.colorbar(im, ax=ax, shrink=.6, ticks=[0, 1, 2])
fig.tight_layout(); fig.savefig(os.path.join(FIGS, "fig04_heatmap_traceability.png")); plt.close(fig)

# ---- Fig 05: radar / spider chart of source coverage ----------------------
DIMS = ["Gender\nprinciples", "Rewriting\nmechanics", "Pronoun\nstrategy",
        "Bias detection /\ntaxonomy", "Titles &\naddress", "Legal-text\nsafety",
        "Disability", "Ethnicity", "LGBTQIA+", "Age", "Class", "Religion",
        "Multimodal", "AI-era\nrisks"]
COV = {
    "EIGE-2019":      [2, 2, 2, 2, 2, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    "EIGE-2024":      [2, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 2, 2],
    "UNW-EN":         [1, 2, 1, 1, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    "CAPE-2023":      [1, 2, 2, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    "IBEC-2015":      [1, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "INTELLECT-2022": [1, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0],
}
N = len(DIMS)
ang = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
ang += ang[:1]
fig, ax = plt.subplots(figsize=(7.4, 6.6), subplot_kw=dict(polar=True))
palette = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3", "#937860"]
for (label, vals), col in zip(COV.items(), palette):
    v = vals + vals[:1]
    ax.plot(ang, v, lw=1.4, color=col, label=label)
    ax.fill(ang, v, color=col, alpha=.06)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(DIMS, fontsize=7.2)
ax.set_yticks([1, 2]); ax.set_yticklabels(["supporting", "primary"], fontsize=7)
ax.set_ylim(0, 2.3)
ax.set_title("Fig. 5 — Thematic coverage profile of the six source guidelines\n(spider chart; coded 0 = absent, 1 = supporting, 2 = primary)", pad=26)
ax.legend(loc="upper right", bbox_to_anchor=(1.32, 1.12), fontsize=7.5)
fig.tight_layout(); fig.savefig(os.path.join(FIGS, "fig05_radar_source_coverage.png")); plt.close(fig)

# ---- Fig 06: artifact distribution by tier --------------------------------
tiers = ["meta", "core", "gender", "identity-domains", "communication", "workflows", "root"]
counts = {"meta": 3, "core": 1, "gender": 6, "identity-domains": 6,
          "communication": 2, "workflows": 1, "root": 1}
kb = {"meta": 0.0, "core": 0.0, "gender": 0.0, "identity-domains": 0.0,
      "communication": 0.0, "workflows": 0.0, "root": 0.0}
for ts, rel in artifacts:
    rel = rel.replace("\\", "/")
    if rel.startswith("skills/_meta"): k = "meta"
    elif rel.startswith("skills/core"): k = "core"
    elif rel.startswith("skills/gender"): k = "gender"
    elif rel.startswith("skills/identity-domains"): k = "identity-domains"
    elif rel.startswith("skills/communication"): k = "communication"
    elif rel.startswith("skills/workflows"): k = "workflows"
    else: k = "root"
    kb[k] += os.path.getsize(os.path.join(ROOT, rel)) / 1024
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.0))
vals = [counts[t] for t in tiers]
cols = [TIER_COLORS.get(t, "#999999") for t in tiers]
wedges, _ = ax1.pie(vals, colors=cols, startangle=90,
                    wedgeprops=dict(width=.42, edgecolor="w"))
ax1.legend(wedges, [f"{t} ({c})" for t, c in zip(tiers, vals)],
           fontsize=7, loc="center left", bbox_to_anchor=(.92, .5))
ax1.set_title(f"(a) Artifacts by tier (N={sum(vals)})")
bars = ax2.bar([t.replace("-", "\n") for t in tiers], [kb[t] for t in tiers], color=cols)
for b, t in zip(bars, tiers):
    ax2.text(b.get_x() + b.get_width() / 2, b.get_height() + .2, f"{kb[t]:.1f}",
             ha="center", fontsize=7.5)
ax2.set_ylabel("KB"); ax2.set_title("(b) Knowledge volume by tier")
ax2.tick_params(axis="x", labelsize=7); ax2.grid(axis="y", alpha=.3)
fig.suptitle("Fig. 6 — Library composition by architectural tier", fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, .93])
fig.savefig(os.path.join(FIGS, "fig06_tier_distribution.png")); plt.close(fig)

# ---- Fig 07: avoid->prefer mappings ---------------------------------------
fig, ax = plt.subplots(figsize=(9.2, 4.6))
items = [("SUB:" + t, c) for t, c in sub_sections] + [("DOM:" + t, c) for t, c in dom_counts]
items.sort(key=lambda x: -x[1])
lbl = [i[0] for i in items]; val = [i[1] for i in items]
col = ["#4C72B0" if l.startswith("SUB") else "#55A868" for l in lbl]
ax.bar(range(len(items)), val, color=col)
ax.set_xticks(range(len(items)))
ax.set_xticklabels([l.split(":", 1)[1][:26] for l in lbl], rotation=40,
                   ha="right", fontsize=6.8)
for i, v in enumerate(val):
    ax.text(i, v + .3, str(v), ha="center", fontsize=7)
ax.set_ylabel("avoid -> prefer mappings")
ax.set_title(f"Fig. 7 — Terminology mapping inventory (total = {TOTAL_MAPPINGS})\n"
             "blue = central substitution tables, green = identity-domain skill tables")
ax.legend(handles=[Patch(color="#4C72B0", label="substitution-tables.md sections"),
                   Patch(color="#55A868", label="identity-domain SKILL.md tables")],
          fontsize=7.5)
ax.grid(axis="y", alpha=.3)
fig.tight_layout(); fig.savefig(os.path.join(FIGS, "fig07_mappings_by_domain.png")); plt.close(fig)

# --------------------------------------------------------------------------
# Summary printout (used when drafting the paper)
# --------------------------------------------------------------------------
r = [m["rules"] for m in metrics]; k = [m["size_kb"] for m in metrics]
print("=== SUMMARY ===")
print(f"skills: {len(metrics)} | rules total {sum(r)} "
      f"(mean {np.mean(r):.1f}, sd {np.std(r, ddof=1):.1f}, min {min(r)}, max {max(r)})")
print(f"size KB total {sum(k):.1f} (mean {np.mean(k):.1f})")
print(f"table rows in SKILL.md files: {sum(m['table_rows'] for m in metrics)}")
print(f"substitution-tables.md rows: {data_rows(ref_txt)}")
print(f"TOTAL avoid->prefer mappings: {TOTAL_MAPPINGS}")
print(f"artifacts: {len(artifacts)} | corpus pages: {sum(c[3] for c in corpus)}")
print("figures written:", sorted(os.listdir(FIGS)))
