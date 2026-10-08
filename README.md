# ShelfSense — Predictive Shelf Life Engine for Food Exporters

> **Developed by S. M. Mahmud Iqbal**  
> *Food Engineering & Preservation Research | Neo-Brutalist Web Engine*

[![Live Demo](https://img.shields.io/badge/Live%20Demo-shelfsense--lemon.vercel.app-ffe17c?style=for-the-badge&logo=vercel&logoColor=black)](https://shelfsense-lemon.vercel.app)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-171e19?style=for-the-badge&logo=github)](https://github.com/SMMahmudIqbal/shelfsense)
[![License](https://img.shields.io/badge/License-MIT-b7c6c2?style=for-the-badge)](LICENSE)

---

## 📌 Executive Summary

Developing nations lose **30% to 40% of packaged perishable foods** at overseas ports and customs due to unexpected spoilage, microbial proliferation, and barrier failure during maritime transit. Traditional shelf-life validation requires **6 to 12 months** of real-time stability testing or expensive commercial accelerated studies ($1,500 – $3,500 per SKU).

**ShelfSense** is an open food engineering web application that instantly simulates product degradation trajectories using validated **Arrhenius kinetics**, **water activity ($A_w$) thresholds**, **equilibrium pH limits**, and **packaging gas transmission rates**.

---

## ⚡ Key Capabilities

### 1. 🧪 Arrhenius Kinetic Shelf Stability Engine
- **Water Activity ($A_w$):** Models exponential microbial inhibition and moisture sorption stress across critical boundaries (0.50 – 0.99).
- **Acidification Thresholds:** Validates against the international acidified food cutoff (pH $\le$ 4.60) to prevent *Clostridium botulinum* spore germination.
- **Thermal Acceleration ($Q_{10}$ Factor):** Simulates sea-lane ambient heat spikes (25°C baseline up to 45°C equatorial cargo holds).
- **Packaging Gas Barrier Matrix:** Incorporates oxygen transmission rates (OTR) and water vapor transmission rates (WVTR) across:
  - Multi-layer Retort Pouches (Alu-foil laminate)
  - Hermetic Glass Jars (Lug closures)
  - Lacquered Tin Cans
  - High-barrier & Standard PET Bottles
  - Modified Atmosphere Packaging (MAP)

### 2. ⚖️ Formula A vs. Formula B Scenario Comparator
- Side-by-side formulation playground comparing baseline recipes against optimized reformulations.
- Dual-trajectory SVG decay curves plotted simultaneously.
- Dynamic **Days Gained** and percentage shelf-life extension callouts.

### 3. 📄 One-Click Official Export Stability Certificate (PDF Generator)
- Generates an export compliance certificate with a unique verification serial (e.g., `CERT-SS-2026-8849`).
- Features a **Hazard Evaluation Table** (*Clostridium botulinum*, *Staphylococcus aureus*, lipid oxidation).
- Print-optimized (`@media print`) layout ready for overseas buyers, customs brokers, BSTI, and FDA compliance filings.
- Digital sign-off and certification block by **S. M. Mahmud Iqbal**.

### 4. 📦 Packaging Cost vs. Spoilage Savings Calculator (FCL Model)
- Full Container Load (20ft FCL) batch financial modeling.
- Quantifies packaging upgrade investment vs. cargo write-off risk elimination.
- Calculates **Protected Cargo Profit** and **Net Return on Investment (ROI %)**.

---

## 🎨 Design System: Neo-Brutalism

ShelfSense is built with a high-contrast **Neo-Brutalist aesthetic**:

- **Palette:**
  - **Primary:** `#ffe17c` (Yellow) with a `32px x 32px` radial dot grid (10% opacity)
  - **Background:** `#171e19` (Charcoal)
  - **Accent:** `#b7c6c2` (Sage)
  - **UI Surfaces:** `#ffffff` (White)
  - **Text & Borders:** `#000000` (Pitch Black, `2px solid #000000`)
- **Typography:**
  - **Headings:** *Cabinet Grotesk* (Extrabold 800, tight tracking `-0.05em`)
  - **Body Text:** *Satoshi* (Medium 500 & Bold 700)
- **Hard Shadows:**
  - Standard elements: `box-shadow: 4px 4px 0px 0px #000000;`
  - Large containers: `box-shadow: 8px 8px 0px 0px #000000;`
- **Micro-Interactions:**
  - Buttons feature physical press physics: `transform: translate(4px, 4px); box-shadow: 0px 0px 0px 0px #000000;` on hover.

---

## 🔬 Mathematical & Food Engineering Formulation

The core simulation couples the Arrhenius rate equation with moisture sorption kinetics:

$$k = A \cdot \exp\left(-\frac{E_a}{R \cdot T}\right)$$

Simplified via the reaction acceleration coefficient $Q_{10} = 2.0$:

$$\text{Shelf Life} = \text{BaseDays}_{\text{pkg}} \times f(A_w) \times f(\text{pH}) \times Q_{10}^{-\frac{T - 25}{10}} \times \text{Buffer}_{\text{market}}$$

Where:
- $f(A_w) = 0.25 + 0.75 \cdot \left[1 - \left(\frac{A_w - 0.50}{0.50}\right)^{1.85}\right]$
- $f(\text{pH}) = 1.25 - (\text{pH} - 2.0) \cdot 0.05$ (for $\text{pH} < 4.60$)
- $f(\text{pH}) = 1.00 - (\text{pH} - 4.60) \cdot 0.16$ (for $\text{pH} \ge 4.60$)

---

## 🚀 Getting Started

### Local Setup
No build tools or heavy dependencies required. Just clone and open in any modern browser:

```bash
git clone https://github.com/SMMahmudIqbal/shelfsense.git
cd shelfsense
# Open index.html directly
start index.html # On Windows
```

### Live Deployment
Deploy with zero configuration to Vercel:

```bash
npm install -g vercel
vercel --prod
```

---

## 👤 Author & Attribution

**Developed by S. M. Mahmud Iqbal**  
- GitHub: [@SMMahmudIqbal](https://github.com/SMMahmudIqbal)  
- Focus: Food Process Engineering, Preservation Science & Applied AI Systems  

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
