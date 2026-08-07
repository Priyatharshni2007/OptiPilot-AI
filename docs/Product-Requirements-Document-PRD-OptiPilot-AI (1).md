# Product Requirements Document (PRD): OptiPilot AI

**Project Name:** OptiPilot AI  
**Tagline:** Find • Prioritize • Simulate • Automate  
**Version:** 1.0  
**Date:** August 2026  
**Prepared by:** Priyatharshni R M  
**Status:** Production-Ready / National Finale Submission  

---

## 1. Executive Summary
**OptiPilot AI** is an Agentic Business Process Intelligence Platform designed to help organizations discover, analyze, and prioritize automation opportunities before investing in digital transformation. 

Unlike conventional automation platforms that require manual process identification, OptiPilot AI acts as an intelligent business consultant. It leverages the **Process Intelligence Engine (PIE)**—a multi-stage reasoning engine—to analyze workflow documents, identify inefficiencies, predict ROI, and generate explainable recommendations. The goal is to ensure organizations automate the *right* tasks at the *right* time for maximum impact.

---

## 2. Problem Statement
Organizations generate vast amounts of operational data (SOPs, meeting notes, logs), yet identifying high-impact automation opportunities remains a manual, expensive, and error-prone process. 
*   **Suboptimal Investment:** Businesses often automate low-impact tasks while overlooking critical bottlenecks.
*   **Resource Gap:** SMEs lack access to expensive business consultants to perform process audits.
*   **Execution vs. Strategy:** Existing tools focus on *executing* automation rather than *identifying* where it delivers the most value.

---

## 3. Goals & Objectives
*   **Analyze:** Use AI reasoning to interpret complex business workflows.
*   **Detect:** Identify repetitive tasks, inefficiencies, and hidden bottlenecks.
*   **Predict:** Estimate time savings, cost reduction, and ROI.
*   **Prioritize:** Rank initiatives based on feasibility and business value.
*   **Simulate:** Model "Before vs. After" scenarios to visualize impact.
*   **Advise:** Provide explainable, executive-ready reports for strategic decision-making.

---

## 4. Target Users / Stakeholders
### Primary Users
*   **SMEs:** Business Owners and Operations Managers.
*   **Digital Transformation Teams:** Leads responsible for automation roadmaps.
*   **Consultants:** Process improvement specialists.

### Secondary & Future Users
*   **Enterprise:** Business Analysts and Operations Executives.
*   **Industry Specific:** Healthcare, Manufacturing, and Government organizations requiring large-scale workflow monitoring.

---

## 5. Functional Requirements
| ID | Requirement | Priority |
|:---|:---|:---|
| **FR-01** | Multi-format document upload (PDF, DOCX, TXT, CSV). | High |
| **FR-02** | Automated workflow extraction from unstructured documents. | High |
| **FR-03** | PIE-driven identification of repetitive tasks and bottlenecks. | High |
| **FR-04** | Calculation of an "Automation Opportunity Score." | High |
| **FR-05** | ROI Prediction (Time, Cost, Productivity metrics). | High |
| **FR-06** | Generation of Explainable AI recommendations (Reasoning logs). | High |
| **FR-07** | "Simulation Mode" for Before vs. After performance modeling. | High |
| **FR-08** | Interactive Dashboard displaying "Business Health Score." | Medium |
| **FR-09** | Executive Decision Mode for concise management summaries. | High |
| **FR-10** | Exportable professional PDF reports (Executive Roadmap). | Medium |

---

## 6. Non-Functional Requirements
*   **Performance:** Analysis of typical workflows must complete within 10–15 seconds.
*   **Scalability:** Architecture must support migration from MVP to enterprise-scale cloud deployments.
*   **Security:** Zero-retention processing options for highly confidential business data.
*   **Usability:** Intuitive interface requiring zero technical expertise in AI or Process Mining.
*   **Reliability:** Consistent recommendation logic; graceful handling of incomplete/corrupt inputs.
*   **Explainability:** Every recommendation must include a human-readable "Why" based on the CRISPE framework.

---

## 7. System Architecture Overview
The system follows a layered, agentic approach:
1.  **Ingestion Layer:** Handles document uploads and initial parsing.
2.  **Orchestration Layer:** The **Master Orchestrator (Google ADK)** uses a **Decision Graph Router** to delegate tasks.
3.  **Specialized Agent Swarm:** 
    *   **Business Twin AI:** Maps current processes.
    *   **PIE AI:** Analyzes inefficiencies.
    *   **Simulation AI:** Models future states.
    *   **TrustLens AI:** Ensures compliance and bias monitoring.
4.  **Intelligence Core:** Powered by **Google Vertex AI**, utilizing **Gemini 1.5 Pro** for reasoning and **Gemma** for lightweight PII filtering.
5.  **Infrastructure:** Hosted on **GCP Cloud Run** with **BigQuery** for analytics and **Vector Search** for RAG-based context.

---

## 8. Tech Stack
| Component | Technology |
|:---|:---|
| **AI Models** | Google Gemini 1.5 Pro (Reasoning), Gemma (PII/Filtering) |
| **AI Development** | Google AI Studio, Google ADK (Agent Development Kit) |
| **Agent Runtime** | Antigravity Agent Runtime, LangGraph |
| **Backend** | Python, FastAPI |
| **Frontend** | Streamlit (MVP) / React & Next.js (Enterprise) |
| **Databases** | PostgreSQL (Workflow/Process/Sim/Trust DBs), SQLite (History) |
| **Cloud Infrastructure** | GCP Cloud Run, BigQuery, Pub/Sub, Vertex AI Vector Search |
| **Security** | OAuth2/OIDC, JWT, TLS 1.3, AES-256 |
| **Observability** | OpenTelemetry, Cloud Monitoring |

---

## 9. Data Requirements
*   **Data Models:** Structured schemas for Workflow Metadata, Process Bottlenecks, Simulation Results, and Trust Logs.
*   **Persistence:** 
    *   **Workflow DB:** Stores extracted process maps.
    *   **BigQuery:** Long-term analytical storage for cross-departmental trends.
    *   **Vector Store:** Semantic storage of SOPs for RAG-based reasoning.
*   **Data Flow:** Documents → Text Extraction → Vectorization → Agent Analysis → Relational Storage → Executive Reporting.

---

## 10. API Specifications
*   **A2A Communication:** Agents communicate via a Decision Graph Router using asynchronous messaging (Pub/Sub).
*   **Vertex AI Gateway:** Centralized API management for LLM requests.
*   **External Integrations (Phase 2/3):** ERP (SAP/Oracle), Slack, and Microsoft Teams via secure webhooks.

---

## 11. Security Requirements
*   **Authentication:** OAuth2/OpenID Connect for user access.
*   **Authorization:** Role-Based Access Control (RBAC) via JWT.
*   **Privacy:** GDPR-compliant data minimization and secure retention policies.
*   **Responsible AI:** **TrustLens AI** monitors for EEOC bias and ensures ethical automation recommendations.
*   **Encryption:** AES-256 at rest; TLS 1.3 in transit.

---

## 12. Deployment & Infrastructure
*   **Containerization:** All services deployed as Docker containers on **Cloud Run**.
*   **Orchestration:** Managed via Google Cloud's serverless ecosystem for auto-scaling.
*   **CI/CD:** Git-based deployment with automated testing for agent prompts.

---

## 13. Success Metrics
*   **Discovery Volume:** Number of automation opportunities identified per document.
*   **Efficiency:** Estimated % reduction in manual processing time.
*   **Financial Impact:** Predicted annual cost savings ($).
*   **Accuracy:** User validation of AI-identified bottlenecks.
*   **Adoption:** % of AI-generated reports resulting in executive approval for automation projects.

---

## 14. Timeline & Milestones
*   **Phase 1 (MVP):** Core PIE engine, document analysis, ROI prediction, and basic Simulation Mode.
*   **Phase 2 (Enterprise):** Multi-user support, department-level analytics, and initial API integrations.
*   **Phase 3 (Intelligent Platform):** Real-time workflow monitoring, ERP integration, and predictive operational intelligence.

---

## 15. Open Questions & Risks
*   **Data Sensitivity:** How to handle highly sensitive SOPs that cannot leave on-premise environments (Potential solution: Hybrid cloud/Gemma local deployment).
*   **Model Hallucination:** Ensuring ROI predictions remain grounded in realistic industry benchmarks.
*   **Integration Complexity:** The feasibility of real-time monitoring across legacy ERP systems in Phase 3.

---

## 16. Competitive Advantage
| Feature | Traditional Automation Tools | **OptiPilot AI** |
|:---|:---|:---|
| **Approach** | Execute predefined workflows | **Discovers what should be automated** |
| **Transparency** | Limited/Black-box | **Explainable Decision Intelligence** |
| **Forecasting** | No future simulation | **AI Simulation Mode (Before/After)** |
| **Prioritization** | Generic/Manual | **ROI-based automated ranking** |
| **Visualization** | Static reports | **AI Business Twin & Interactive Dashboards** |