# Hichem Benali

**Building governed autonomous systems, bounded agent workflows, and proof-driven AI infrastructure.**

I design and build systems where LLMs are used as reasoning engines inside explicit governance boundaries — not as uncontrolled decision-makers.

My current work focuses on **ACE / Asso Execution Engine**: a governed autonomous operating layer for multi-agent delegation, state monitoring, receipts, human approval gates, and fail-closed execution.

The core thesis is simple:

> Autonomy without governance is not intelligence. It is liability.

---

## What I Build

I work on practical infrastructure for agentic systems that need to stay bounded, auditable, and reversible:

- **bounded autonomy** — agents act inside explicit envelopes;
- **branch-as-envelope workflows** — every agentic branch has a mandate, boundary, handoff, and rollback path;
- **receipt-based execution** — claims are not trusted without evidence;
- **human-in-the-loop gates** — sensitive actions require explicit approval;
- **fail-closed systems** — unknown states stop instead of improvising;
- **agent evaluation harnesses** — behavior should be testable, not merely impressive.

The goal is not to make agents act freely.

The goal is to make agentic systems **governable, auditable, reversible, and useful**.

---

## Current Focus

### ACE / Asso Execution Bridge

ACE / Asso is my private systems lab for governed autonomous execution.

It explores how specialized agents can coordinate work across branches, produce artifacts, leave receipts, surface system state in a control room, and prepare public-safe proof outputs without turning LLMs into uncontrolled authorities.

The canonical execution repo is currently private while the safety, runtime, and proof boundaries are being stabilized.

Public-facing extracts and reusable patterns will be published through the repos below.

---

## Public Artifacts

### [ai-ops-sop-pack](https://github.com/monkidy/ai-ops-sop-pack)

SOPs and templates for bounded AI-agent operations: PR review, handoff discipline, crash recovery, stop conditions, and audit-friendly workflows.

This is the most directly reusable public artifact today.

### [asso-lab](https://github.com/monkidy/asso-lab)

Public lab surface for ACE / Asso doctrine, bounded agent governance, and proof-driven operating patterns.

This repo is intended to expose safe public notes without leaking the private execution core.

### [ACE-LAB-GATEWAY](https://github.com/monkidy/ACE-LAB-GATEWAY)

Gateway surface for controlled public interfaces, lab notes, and future proof cards around governed autonomous systems.

### [monkidy](https://github.com/monkidy/monkidy)

This GitHub profile README. It acts as the public identity and authority surface for the work above.

---

## Technical Areas

**Systems Architecture**  
Multi-agent orchestration, bounded autonomy, state buses, execution gates, agent envelopes.

**Core Stack**  
Python, TypeScript, Node.js, GitHub Actions, local-first automation.

**AI Infrastructure**  
LLM routing, local inference experiments, agent evaluation harnesses, prompt-to-receipt workflows.

**Security & Governance**  
No-send defaults, explicit approval boundaries, audit trails, rollback-first design.

**Market Telemetry Research**  
Risk-aware telemetry, signal pipelines, and supervised execution research.

---

## Operating Doctrine

> Power without governance is a liability.  
> Real autonomy requires boundaries, receipts, and revocation.

Core principles:

- **Fail-closed by default** — unknown states stop instead of improvising.
- **Receipts over claims** — no status is trusted without evidence.
- **Outbox is not send** — drafts and publication are separate gates.
- **Branches are envelopes** — every agentic work branch needs a mandate, boundary, handoff, and rollback path.
- **Human authority stays explicit** — LLMs reason, systems verify, humans authorize sensitive action.

---

## Current Proof Work

The next public-facing layer is focused on making agent governance testable:

- action-class classification;
- draft vs send boundaries;
- claim vs receipt discipline;
- handoff completeness;
- branch-as-envelope validation;
- public proof cards;
- local, deterministic eval fixtures before any model-scored runner.

Private work becomes public only when it can be made safe, documented, and verifiable.

---

## Contact

- GitHub: [@monkidy](https://github.com/monkidy)
- Public SOPs: [ai-ops-sop-pack](https://github.com/monkidy/ai-ops-sop-pack)
- Public lab: [asso-lab](https://github.com/monkidy/asso-lab)
