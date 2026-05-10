---
tags:
  - incomplete
date: 2026-04-02
teacher: Ms. Zainab
---
# Emerging Technologies 5

# Dataset Sources

- [Federal Reserve Economic Data | FRED | St. Louis Fed](https://fred.stlouisfed.org/)
- [Our World in Data](https://ourworldindata.org/)
- [Your Gateway to NASA Earth Observation Data | NASA Earthdata](https://www.earthdata.nasa.gov/)
- [PDS: Data Search](https://pds.nasa.gov/datasearch/data-search/)
- [How-To Videos | Tableau Public](https://public.tableau.com/app/learn/how-to-videos)
- [Find Open Datasets for AI and Research | Kaggle](https://www.kaggle.com/datasets)
# Topics 2 Pick
- [History of Technology Timeline | Evolution, Digital, Medical, Information, Education, & Communication | Britannica](https://www.britannica.com/story/history-of-technology-timeline)
- [SEA-ME-WE 3 - Wikipedia](https://en.wikipedia.org/wiki/SEA-ME-WE_3)
- [Optical fiber - Wikipedia](https://en.wikipedia.org/wiki/Optical_fiber)
- [Dubai Fountain, The Dancing Water Fountain – UAE - Traveldigg.com](https://traveldigg.com/dubai-fountain/)

- [x] [Computational capacity of the fastest supercomputers](https://ourworldindata.org/grapher/supercomputer-power-flops)
- [x] [Historical price of computer memory and storage](https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage)
- [x] [Adoption of communication technologies per 100 people, World](https://ourworldindata.org/grapher/ict-adoption-per-100-people)
- [x] [Computation used to train notable artificial intelligence systems, by domain](https://ourworldindata.org/grapher/artificial-intelligence-training-computation?time=1950-07-02..2026-02-17)
- [x] [Artificial intelligence: Performance on knowledge tests vs. training computation](https://ourworldindata.org/grapher/ai-performance-knowledge-tests-vs-training-computation)

- Technology
	- Mobiles
	- Computers
- Global Waste
	- Plastic Waste
	- Food Waste
- Education
	- Online Learning
	- Traditional Learning
- Internet
	- Social Media
	- Games
# Dialogflow Agent

```mermaid
flowchart TB

    %% =========================
    %% INTENTS (VERTICAL GROUP)
    %% =========================

    subgraph INTENTS[Intents]
    
        direction TB

        B["Default Intent"]
        C["Fallback Intent"]

        D["Sell Intent\nexpects @sell_item"]
        
            D1["Sell PC Intent\nexpects @pc"]
            D1A["Fulfillment Action:\nFetch PC Price"]
            D1 --> D1A

            D2["Sell Component Intent\nexpects @component"]
            D2A["Fulfillment Action:\nFetch Component Price"]
            D2 --> D2A

        D --> D1
        D --> D2

        E["Order Intent\nexpects @order_item"]
        
            E1["Buy PC Intent\nexpects @pc"]
            E1A["Fulfillment Action:\nFetch PC Product"]
            E1 --> E1A

            E2["Buy Component Intent\nexpects @component"]
            E2A["Fulfillment Action:\nFetch Component Product"]
            E2 --> E2A

        E --> E1
        E --> E2

    end

    %% =========================
    %% ENTITIES (VERTICAL GROUP)
    %% =========================

    subgraph ENTITIES[Entities]
    
        direction TB

        G["PC"]

            G1["Gaming PC"]
            G2["Home PC"]
            G3["Old PC"]
            G4["Office PC"]

            G --> G1
            G --> G2
            G --> G3
            G --> G4

        H["Components"]

            H1["RAM"]
            H2["SSD"]
            H3["CPU"]
            H4["GPU"]

            H --> H1
            H --> H2
            H --> H3
            H --> H4

        I["Sell Items"]

            I1["PC"]
            I2["Component"]

            I --> I1
            I --> I2

  

        J["Order Items"]

            J1["PC"]
            J2["Component"]

            J --> J1
            J --> J2

    end

    %% CONNECT INTENTS TO ENTITIES BLOCK
    INTENTS --> ENTITIES
```
# Outline Structure

**I. Introduction**
**II. Data Visualization**
	A. Main Context
		1. Dataset 1
		2. Dataset 2
		3. Dataset 3
		4. Dataset 4
		5. Dataset 5
	B. Key Decisions
	C. Critical Reflection
**III. Dialogflow Agent**
	A. Main Context
	B. Key Decisions
	C. Critical Reflection

----------------------------------------------------------------
# Editor's Notes