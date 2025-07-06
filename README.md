# 🧠 CiviSight - Civic Insight Engine – Full Product Roadmap

**Civisight** is an AI-powered platform that brings radical transparency and insight into the public sphere by making political information easily accessible, analyzable, and interactive.

We help citizens, journalists, researchers, and public servants explore:
- **Who politicians are**
- **What they say**
- **How they behave across time**
- **What they stand for (and how it shifts)**

Instead of endless Googling and fragmented sources, Civisight creates **a single intelligent interface** where users can:
- Look up any public politician
- See their latest media appearances
- View aggregated news sentiment
- Explore topic-based political leanings
- Eventually: *interact with a grounded AI clone* based on their own words



## 🌍 Why It Matters

Today, the relationship between citizens and public figures is obscured by:
- Information overload
- Biased media framing
- Lack of centralized access to political discourse

🧩 *Civisight solves this* by combining:
- Automated data collection (scraping, news, video, transcripts)
- Advanced AI/NLP analysis (sentiment, ideology, persona modeling)
- Conversational AI (retrieval-augmented dialogue with political “clones”)

Our goal is to **empower informed participation**, help citizens **cut through media noise**, and give public institutions **tools to monitor discourse responsibly**.


## 💼 Use Cases

| Audience             | Use Case                                                   |
|----------------------|------------------------------------------------------------|
| 🗞️ **Journalists**       | Searchable, timestamped quotes across topics               |
| 🎓 **Researchers**       | Analyze political leaning shifts over time                 |
| 🏛️ **Public Institutions** | Measure impact of speeches, debates, narratives            |
| 👩‍💻 **Citizens**          | Understand political stances before elections              |
| 🧠 **Educators**          | Show civic behavior in interactive and engaging ways       |


## 🚀 Key Features (Phase by Phase)

### 📇 Politician Profile Lookup  
Auto-generated, up-to-date profiles including bio, party, location, topics of interest, and key quotes.

### 📰 News + Sentiment Dashboard  
Aggregates the latest news per politician and applies NLP to classify tone (positive, neutral, negative).

### 🎙️ Speech Transcription & Analysis  
Pulls videos from YouTube, transcribes them with Whisper, and detects key themes, names, and opinions.

### 🧠 Political Leaning Detection  
Classifies left-center-right position on topics like climate, economy, immigration — based on public statements, not assumptions.

### 💬 Conversational AI Clone *(Future Phase)*  
Users will be able to interact with a “political AI clone” that answers questions based on real data, with citations.


## 📊 Example Output

> **Mark Rutte**  
> Topics: Immigration, Fiscal Policy, EU  
> Leaning: Center-right  
> Last 10 News Articles: 60% neutral, 30% negative, 10% positive  
> Last Statement: “We must preserve Dutch values while protecting vulnerable groups.”  
> Sentiment Score: +0.14 (mildly positive)  
> Key Quote on Climate: “Economic growth must not be at odds with our environmental duties.”  
> [Transcript] [Timeline] [View AI Chat]


## 🧱 Tech Stack

| Component          | Technology                          |
|--------------------|--------------------------------------|
| Backend API        | FastAPI (Python)                     |
| Frontend UI        | Streamlit / Next.js                  |
| NLP                | Hugging Face Transformers, spaCy     |
| Transcription      | Whisper (OpenAI)                     |
| Storage            | SQLite → PostgreSQL → FAISS (vector DB) |
| Deployment         | GitHub Actions, Render, HuggingFace Spaces |

---

## ⚡ Mission

> **To empower citizens and institutions with intelligent, real-time, and truthful insight into the words and actions of those in power.**

Civisight is designed as an open civic tool to democratize political awareness, not only to inform but to engage, question, and connect.


# Roadmap 

## 🔹 Phase 0 – Product Framing & Architecture Design

**🧭 Goal:**  
Define scope, system architecture, and core features.

**📦 Deliverables:**
- Feature map (core, stretch)
- System architecture diagram
- Pitch deck (internal/external)
- Tech feasibility mapping

**⏳ Timeframe:** 2–3 days

**💼 Business Value:**
- Internal clarity for stakeholders
- Foundation for pitching or partnerships
- Demonstrates scalability and real impact

**👀 Technical Notes:**
- Diagram tools: Lucidchart, Miro, Figma
- Data sources: Parlement.com, Wikipedia, NewsAPI, YouTube, etc.



## 🔹 Phase 1 – MVP (Manual Data + Basic UI)

**🧭 Goal:**  
Deliver a working prototype with profiles, news, and AI analysis.

**📦 Deliverables:**
- Hardcoded JSON/SQLite politician list (5–10)
- News fetcher with sentiment scoring
- Political leaning estimator (zero-shot)
- Streamlit or Next.js UI

**⏳ Timeframe:** 5–7 days

**💼 Business Value:**
- Quick proof of concept
- Demonstrates practical use to municipalities
- Opens doors to civic/public engagement

**👀 Technical Notes:**
- Backend: FastAPI
- NLP: Hugging Face `transformers`, `textblob`
- News: NewsAPI or GNews



## 🔹 Phase 2 – Auto-Generated Politician Profiles (Scraping)

**🧭 Goal:**  
Automate profile creation via scraping and enrichment.

**📦 Deliverables:**
- Scraper for Wikipedia or Parlement.com
- Profile generator: name, party, bio, age, etc.
- Photo and metadata crawler
- Scheduler (daily/weekly updates)

**⏳ Timeframe:** 1–2 weeks

**💼 Business Value:**
- Reduces manual input
- Enables scale to national/international coverage
- Feeds analytics and trending dashboards

**👀 Technical Notes:**
- Tech: `BeautifulSoup`, `Playwright`, `Selenium`
- Auto-run: `cron`, `apscheduler`, GitHub Actions



## 🔹 Phase 3 – YouTube Video Transcription & Speaker Identification

**🧭 Goal:**  
Pull political videos, transcribe them, and identify speakers.

**📦 Deliverables:**
- YouTube fetcher via `yt-dlp` or API
- OpenAI Whisper for transcription
- Title/description + transcript NER
- (Optional) Speaker voiceprint classification

**⏳ Timeframe:** 2–3 weeks

**💼 Business Value:**
- Enables speech analysis and media accountability
- Helps journalists access searchable transcripts
- Boosts civic transparency

**👀 Speaker Identification Options:**
- A. Channel source mapping
- B. NER on video title/description
- C. NER on transcript
- D. Voiceprint matching (e.g. Resemblyzer)
- E. Face recognition (optional)



## 🔹 Phase 4 – NLP Enrichment + Persona Builder

**🧭 Goal:**  
Analyze and cluster speech + content into themes, tone, ideology.

**📦 Deliverables:**
- Quote extractor + topic classifier
- Sentiment trend charting
- Leaning estimator via NLP
- JSON-based persona objects

**⏳ Timeframe:** 3–4 weeks

**💼 Business Value:**
- Creates a live evolving profile per politician
- Useful for civic dashboards and public reports
- Enables interactive user-facing insights

**👀 Technical Notes:**
- NLP: `zero-shot-classification`, `spaCy`, transformers
- Store enriched profile in DB (Postgres or NoSQL)



## 🔹 Phase 5 – Conversational Persona Chatbot

**🧭 Goal:**  
Simulate politician interaction via RAG-based AI clone.

**📦 Deliverables:**
- Vector DB (FAISS, Pinecone) for quotes/sources
- RAG architecture with LLM backend
- System prompt tuning for style + facts
- Chat frontend (Streamlit or web)

**⏳ Timeframe:** 2–4 weeks

**💼 Business Value:**
- Viral UX feature
- Civic education tool
- Potential for public installations or press campaigns

**👀 Technical Notes:**
- LLM: OpenAI GPT, LLaMA 3, Mixtral
- Guardrails: System prompt limits hallucination
- Data source display with every answer


## 🔹 Phase 6 – Hosting, Automation, and Monitoring

**🧭 Goal:**  
Deploy and automate the platform to be self-sustaining.

**📦 Deliverables:**
- Scheduled fetchers + processors
- Hosted backend + frontend (Render, Vercel, Streamlit Cloud)
- Logging, admin panel (optional)

**⏳ Timeframe:** 1–2 weeks

**💼 Business Value:**
- Product-grade platform
- Enables scale + maintainability
- Supports public rollout or handoff to institutions

**👀 Technical Notes:**
- Use `cron` or `apscheduler`
- Logging via Python or external tools
- DB: PostgreSQL, Firebase, or Supabase (for easy setup)


## 🔐 Ongoing – Ethics, Privacy, and Legal Framework

**🧭 Goal:**  
Ensure safe, transparent, and respectful AI usage.

**📦 Deliverables:**
- Disclaimer + transparency framework
- GDPR-compliant practices
- Ethical AI audit log
- User feedback mechanism

**⏳ Timeframe:** Parallel to dev (2–3 syncs)

**💼 Business Value:**
- Critical for trust and funding
- Keeps project on ethical high ground
- Encourages municipal and educational partnerships


## 📊 Summary Table

| Phase | Name                           | Timeframe     | Value                                 |
|-------|--------------------------------|---------------|----------------------------------------|
| 0     | Vision & Architecture          | 2–3 days      | Alignment + pitch foundation           |
| 1     | MVP (Manual + UI)              | 5–7 days      | Functional demo                        |
| 2     | Scraper + Profile Automation   | 1–2 weeks     | Scalable profiles                      |
| 3     | Video Transcripts + Identity   | 2–3 weeks     | Transcripts + speaker recognition      |
| 4     | NLP & Persona Builder          | 3–4 weeks     | Insight dashboards + analytics         |
| 5     | Chatbot Clone (LLM)            | 2–4 weeks     | Interactive UX + PR                    |
| 6     | Automation & Hosting           | 1–2 weeks     | Deployment + auto updates              |
| 7     | Ethics & Legal Layer           | Parallel/Ongoing | Responsible innovation                |