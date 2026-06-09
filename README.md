# Hichem Benali

**Building bounded, reviewable, proof-driven AI systems.**

I design and build systems where LLMs are used as reasoning engines inside explicit governance boundaries, not as uncontrolled decision-makers.

My current work focuses on **ACE / Asso Capital Engine**: a private systems lab for multi-agent delegation, state monitoring, receipts, human approval gates, and fail-closed execution.

The public work is intentionally narrower: proof surfaces, receipt standards, SOPs, and documentation that can be inspected without exposing private runtime authority.

New here? Open [`VISUAL_OVERVIEW.md`](VISUAL_OVERVIEW.md) for a one-screen repo map.

Current profile status: [`PUBLIC_PROFILE_SURFACE_V0`](STATUS.md).

The core thesis is simple:

> Autonomy without governance is not intelligence. It is liability.

---

## Pourquoi je construis ça

Je ne suis pas arrivé à ces sujets par mode.

Je suis arrivé là parce que j’ai longtemps senti un décalage entre ce que je voyais dans ma tête et ce que les systèmes autour de moi permettaient vraiment de faire.

Quand on ne reçoit pas naturellement les codes, les méthodes et les filets de sécurité, on apprend vite une chose : le flou coûte cher. Une consigne mal posée, une responsabilité pas claire, une décision prise trop vite, une preuve qu’on ne garde pas, et tout repose ensuite sur la mémoire, l’intuition ou la bonne volonté des gens.

J’ai fini par comprendre que ce problème n’était pas seulement personnel. C’est aussi le problème des agents IA.

Un agent peut produire vite. Il peut donner l’impression de comprendre. Il peut proposer, rédiger, exécuter, résumer, convaincre. Mais s’il n’a pas de cadre, pas de limite, pas de trace, pas de refus possible, alors ce n’est pas de l’intelligence opérationnelle. C’est du risque qui parle bien.

ACE / Asso vient de là.

Je construis une manière de travailler où l’agent ne remplace pas l’humain, ne prend pas l’autorité, ne transforme pas une proposition en action, et ne cache pas son travail derrière une phrase propre.

Chaque action doit avoir un mandat. Chaque décision sensible doit avoir un gate. Chaque claim doit pouvoir revenir à une preuve. Chaque système doit savoir s’arrêter quand le cadre manque.

Ce n’est pas une recherche d’autonomie magique.

C’est une recherche de puissance contrôlée : garder la vitesse, garder l’ambition, mais retirer le brouillard.

Je construis ACE / Asso parce que je veux des systèmes capables d’aider vraiment, sans voler la responsabilité humaine, sans maquiller l’incertitude, et sans confondre mouvement avec autorisation.

---

## What I build

I work on practical infrastructure for agentic systems that need to stay bounded, auditable, and reversible:

- **bounded autonomy**: agents operate inside explicit envelopes;
- **branch-as-envelope workflows**: every agentic branch has a mandate, boundary, handoff, and rollback path;
- **receipt-based execution**: claims are not trusted without evidence;
- **human-in-the-loop gates**: sensitive actions require explicit approval;
- **fail-closed systems**: unknown states stop instead of improvising;
- **agent evaluation harnesses**: behavior should be testable, not merely impressive.

The goal is not to make agents act freely.

The goal is to make agentic systems **governable, auditable, reversible, and useful**.

---

## Current focus

### ACE / Asso Capital Engine

ACE / Asso is my private systems lab for governed autonomous execution.

It explores how specialized agents can coordinate work across branches, produce artifacts, leave receipts, surface system state in a control room, and prepare public-safe proof outputs without turning LLMs into uncontrolled authorities.

The canonical execution repo is currently private while the safety, runtime, and proof boundaries are being stabilized.

Public-facing extracts and reusable patterns are published through the repos below.

---

## Public artifacts

### [asso-lab](https://github.com/monkidy/asso-lab)

Public observer surface for ACE doctrine and receipts. It shows bounded briefs with code-generated, inspectable receipts: status, hash, sources, timestamp, and signature fields.

It also hosts the canonical [ACE Visual Charter V1](https://github.com/monkidy/asso-lab/blob/main/docs/brand/ACE_VISUAL_CHARTER_V1.md), the fleet's dual-mode visual doctrine.

### [ace-agent-governance-receipt-standard](https://github.com/monkidy/ace-agent-governance-receipt-standard)

A small, practical standard for keeping AI agents bounded, traceable, and revocable through mandate, proposal, action receipt, and refusal receipt patterns. Apache-2.0.

### [ai-ops-sop-pack](https://github.com/monkidy/ai-ops-sop-pack)

SOPs and templates for AI-assisted engineering operations: PR review, handoff discipline, crash recovery, stop conditions, and evidence-before-readiness review. CC BY 4.0.

### [monkidy](https://github.com/monkidy/monkidy)

This GitHub profile README. Public orientation surface for the work above.

---

## Technical areas

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

## Operating doctrine

> Power without governance is a liability.  
> Real autonomy requires boundaries, receipts, and revocation.

Core principles:

- **Fail-closed by default**: unknown states stop instead of improvising.
- **Receipts over claims**: no status is trusted without evidence.
- **Outbox is not send**: drafts and publication are separate gates.
- **Branches are envelopes**: every agentic work branch needs a mandate, boundary, handoff, and rollback path.
- **Human authority stays explicit**: LLMs reason, systems verify, humans authorize sensitive action.

---

## What this profile does not claim

This profile does not claim:

- production readiness;
- formal verification;
- live runtime safety;
- client adoption;
- revenue;
- autonomous permission-to-act;
- private implementation safety.

Private work becomes public only when it can be made safe, documented, and verifiable.

---

## Current proof work

The next public-facing layer is focused on making agent governance testable:

- action-class classification;
- draft vs send boundaries;
- claim vs receipt discipline;
- handoff completeness;
- branch-as-envelope validation;
- public proof cards;
- local, deterministic eval fixtures before any model-scored runner.

---

## Contact

Open to conversations around AI-agent governance, reliability, auditability, and bounded workflows.

- LinkedIn: [Hichem Benali](https://www.linkedin.com/in/hichem-benali-ace/)
- GitHub: [@monkidy](https://github.com/monkidy)
- Public observer surface: [asso-lab](https://github.com/monkidy/asso-lab)
- Public SOPs: [ai-ops-sop-pack](https://github.com/monkidy/ai-ops-sop-pack)
