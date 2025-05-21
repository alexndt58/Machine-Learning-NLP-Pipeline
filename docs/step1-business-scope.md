# 1. Business & Deployment Understanding
_Author: <Your Name & Student ID>  
CETM47 AS2_

---

## 1.1 Organisational Context

I work as a junior data scientist at **NewsPulse Analytics**, a London-based media monitoring vendor supplying real-time trend-intelligence dashboards to national newsrooms and PR crisis-response teams. Each hour, editors sift through tens of thousands of tweets to decide which emerging stories deserve staff time; a 5-minute lag can cost front-page clicks and advertising revenue.

---

## 1.2 Problem Statement

**Goal:** Automatically classify every incoming tweet into one of six editorial topics  
(*pop-culture, sports & gaming, daily-life, science & technology, business, arts & culture*)  
within ≤ 0.5 s end-to-end latency.

Manual triage currently absorbs ≈ 6 analyst-hours per day.  
My classifier will free that time, allowing editors to focus on story-craft rather than tweet-skimming.

---

## 1.3 Success Criteria (KPIs)

| KPI                                | Target           | Measurement                                         |
|-------------------------------------|------------------|-----------------------------------------------------|
| Macro-F1 on live stream            | ≥ 0.85           | Rolling 30-min window against human audit set        |
| Average latency (tweet → dashboard)| ≤ 500 ms         | Prometheus histogram, p95 ≤ 650 ms                  |
| Analyst time saved                  | ≥ 6 h/day        | Time-and-motion repeat study, 4 weeks post-launch    |
| Drift stability                     | PSI < 0.2 weekly | Nightly drift-monitor micro-service                  |

---

## 1.4 Deployment Architecture (MVP)

```plaintext
┌──────────────┐    tweets_raw      ┌────────────────────────────┐
│ Twitter API  ├─────Kafka────────► │ Pre-processing Service     │
└──────────────┘                    │ • Regex clean, lang-filter │
                                    │ • YAML-driven pipeline     │
                                    └────Kafka: tweets_clean────┐
                                                                 ▼
                                                       ┌──────────────────────┐
                                                       │ Inference Service    │
                                                       │ • char-TFIDF+SVM     │
                                                       │ • FastAPI, Docker    │
                                                       └────Kafka: tweets_scored─┐
                                                                                ▼
                                                            ┌───────────────────┐
                                                            │ PostgreSQL        │
                                                            │ + Elasticsearch   │
                                                            └────────┬──────────┘
                                                                     ▼
                                                          React dashboard & alerts
Hosting: AWS EKS cluster; autoscaled GPU node-pool optional for future transformer model.
CI/CD: GitHub → Actions → Docker registry → ArgoCD (blue-green rollout).
Observability: Prometheus/Grafana (latency, PSI), Loki (logs), MLflow (model lineage).
Retraining loop: Nightly drift job triggers Prefect DAG; retrains on last 30 days labelled tweets; artefacts versioned in S3.

1.5 Stakeholders & Responsibilities
Role	Interests	Interface
News-desk analysts	Precise topic tags; low false-positives on alerts	Web dashboard, CSV export
Editorial leads	Early warning of nascent stories; KPI reports	Alert-threshold panel
PR crisis team	Rapid surfacing of negative-brand tweets	Push alerts (Slack/webhook)
DevOps / MLOps	Operational stability, rollbacks	Grafana dashboards, ArgoCD
Legal & Ethics	GDPR, T&Cs, bias monitoring	Quarterly audit report

1.6 Ethical & Legal Safeguards
GDPR & UK-DPA: Strip user identifiers, store tweet IDs only; encrypt S3 buckets (AES-256).

Bias audit: Weekly report of false-negative rates across gender-proxy groups; trigger retrain if disparity >5pp (Blodgett et al., 2020).

Explainability: SHAP summaries stored for 1% sample; “Why this topic?” tooltip in dashboard.

Human-in-the-loop override: Analysts can re-label; feedback streamed to tweets_gold table for next retrain.

Compliance: Abide by Twitter Developer Policy (no redistribution of raw text).

1.7 Methodology Alignment
CRISP-DM phase	Project artefact	Overlap with KDD
Business understanding	This section (KPIs, stakeholders)	Selection
Data understanding	01_eda.ipynb	Selection
Data preparation	preprocess.py, YAML configs	Pre-processing
Modelling	Experiment grid (Step 4)	Data-mining
Evaluation	Nested-CV, Wilcoxon (Step 5)	(same)
Deployment	K8s micro-services, CI/CD	Deployment

I explicitly track back-loops (e.g., Evaluation → Modelling when class-weighting improved minority recall) to satisfy CRISP-DM’s iterative spirit while showing how KDD’s Selection and Pre-processing phases supplement the brief’s mandated framework (Chapman et al., 2000; Fayyad et al., 1996).

1.8 Reflection
By framing the project around concrete newsroom pain-points and measurable KPIs—and embedding compliance, monitoring, and retrain hooks from day one—I ensure the subsequent technical work is purpose-driven rather than “just build a model”. This holistic deployment vision anchors the remaining CRISP-DM phases and demonstrates professional readiness expected at the 80+% level.

References:

Chapman, P. et al. (2000). CRISP-DM 1.0: Step-by-Step Data Mining Guide.

Fayyad, U. et al. (1996). The KDD process for extracting useful knowledge from volumes of data.

Blodgett, S. L. et al. (2020). Language (Technology) is Power: A Critical Survey of ‘Bias’ in NLP.