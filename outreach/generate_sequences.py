"""
ShelfSense Automated B2B Outreach Toolkit
Developed by S. M. Mahmud Iqbal
Food Process Engineering & Export Stability Systems

This script personalizes multi-stage B2B cold email sequences targeting
Food Quality Assurance (QA) Managers, R&D Directors, and Export Leads.
"""

import csv
import json
import os

TEMPLATES = {
    "step_1": {
        "subject": "Quick shelf stability question for {{company_name}}'s {{product_name}} export line",
        "body": """Dear {{first_name}},

I noticed {{company_name}} has been expanding overseas distribution of your {{product_name}} lineup into {{target_market}}.

As a food engineering researcher specializing in preservation kinetics, I developed ShelfSense (https://shelfsense-lemon.vercel.app) — a predictive stability engine that models water activity (Aw), equilibrium pH, and Arrhenius temperature stress during 30-day maritime shipping.

Under typical 30–35°C equatorial cargo hold transit, moisture vapor transfer across standard packaging often reduces effective shelf life by 25–40%, leading to costly destination port rejections.

I would love to run a complimentary, 1-page Shelf Stability Certificate for one of {{company_name}}'s export SKUs so your QA team can review the kinetic decay trajectory before your next shipment.

Would you be open to reviewing a sample evaluation if I send it over?

Best regards,

S. M. Mahmud Iqbal
Food Process & Preservation Engineering
ShelfSense — https://shelfsense-lemon.vercel.app
Developed by S. M. Mahmud Iqbal"""
    },
    "step_2": {
        "subject": "Re: Quick shelf stability question for {{company_name}}'s {{product_name}} export line",
        "body": """Hi {{first_name}},

Following up on my note regarding {{company_name}}'s export packaging stability.

For products like {{product_name}}, factory QA teams often face a tough trade-off: spending $2,500+ and waiting 4 months for commercial accelerated lab testing (ASLT), or risking cargo rejection at {{target_market}} customs.

With ShelfSense, we model:
1. Clostridium botulinum and fungal barrier limits (pH <= 4.60 & Aw <= 0.85).
2. Packaging gas barrier transmission (PET vs. Retort Pouches vs. Glass Jars).
3. Container ROI: protecting $30,000–$50,000 in perishable export cargo with a minor packaging adjustment.

You can inspect our live simulator here:
https://shelfsense-lemon.vercel.app

If you reply with your flagship product's basic parameters (Aw, pH, and current packaging), I will personally generate an official verified stability dossier for your team at no charge.

Warm regards,

S. M. Mahmud Iqbal
Food Process & Preservation Engineering
ShelfSense | Developed by S. M. Mahmud Iqbal"""
    },
    "step_3": {
        "subject": "Container ROI breakdown for {{company_name}} (packaging vs. spoilage risk)",
        "body": """Hi {{first_name}},

One quick economic insight we frequently share with food processors in {{target_market}} corridors:

On a standard 20ft container (approx. 24,000 units valued at $40,000):
- Upgrading from basic PET to multi-layer barrier costs roughly $0.12/unit (~$2,880 total).
- However, it eliminates an estimated 24% port spoilage and quarantine risk (~$9,600 in protected cargo).
- That delivers a 233% net return on packaging investment.

We built this directly into our interactive packaging calculator on ShelfSense:
https://shelfsense-lemon.vercel.app

Would you have 10 minutes next Tuesday for a brief call to see how this applies to {{company_name}}'s product catalog?

Best,

S. M. Mahmud Iqbal
Food Process & Preservation Engineering
ShelfSense — Developed by S. M. Mahmud Iqbal"""
    },
    "step_4": {
        "subject": "Closing the loop — {{company_name}} export stability review",
        "body": """Hi {{first_name}},

I assume export shelf-life modeling isn't a top priority for {{company_name}} right now, so I will pause my follow-ups.

If your QA or export team ever needs rapid Arrhenius stability validation or buyer-ready stability certificates for foreign customs, feel free to bookmark our engine:

https://shelfsense-lemon.vercel.app

Wishing {{company_name}} continued success with your export operations!

Sincerely,

S. M. Mahmud Iqbal
Food Process & Preservation Engineering
Developed by S. M. Mahmud Iqbal"""
    }
}

def render_email(template_str, prospect):
    rendered = template_str
    for key, value in prospect.items():
        placeholder = "{{" + key + "}}"
        rendered = rendered.replace(placeholder, str(value))
    return rendered

def generate_campaign_batch(csv_filepath, output_dir="outreach_campaign"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csv_filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        prospects = list(reader)

    print(f"Loaded {len(prospects)} prospects from {csv_filepath}")

    for idx, prospect in enumerate(prospects, start=1):
        clean_name = prospect.get("first_name", f"prospect_{idx}").strip().replace(" ", "_")
        company = prospect.get("company_name", "company").strip().replace(" ", "_")
        prospect_file = os.path.join(output_dir, f"{idx:02d}_{clean_name}_{company}.txt")

        with open(prospect_file, mode="w", encoding="utf-8") as out:
            out.write("=" * 70 + "\n")
            out.write(f"PROSPECT: {prospect.get('first_name')} {prospect.get('last_name')} | {prospect.get('company_name')}\n")
            out.write(f"EMAIL: {prospect.get('email')} | TARGET MARKET: {prospect.get('target_market')}\n")
            out.write("=" * 70 + "\n\n")

            for step_key, step_data in TEMPLATES.items():
                step_title = step_key.replace("_", " ").upper()
                rendered_subject = render_email(step_data["subject"], prospect)
                rendered_body = render_email(step_data["body"], prospect)

                out.write(f"--- [{step_title}] ---\n")
                out.write(f"SUBJECT: {rendered_subject}\n\n")
                out.write(rendered_body + "\n\n")

    print(f"Personalized sequences successfully generated in '{output_dir}' directory!")

if __name__ == "__main__":
    sample_csv = "prospects.csv"
    if os.path.exists(sample_csv):
        generate_campaign_batch(sample_csv)
    else:
        print("Please ensure 'prospects.csv' is present.")
