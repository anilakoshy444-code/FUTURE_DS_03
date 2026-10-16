import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Create output folder
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv("bank_marketing.csv", sep=None, engine="python")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Remove duplicate records
df = df.drop_duplicates().copy()

# Clean text columns
for col in df.select_dtypes(include=["str", "object"]).columns:
    df[col] = df[col].str.strip().str.lower()

# Check required columns
required_columns = [
    "age",
    "job",
    "education",
    "contact",
    "campaign",
    "y"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}. "
        "Check the dataset format."
    )

# Remove rows without a subscription outcome
df = df.dropna(subset=["y"]).copy()

# Convert subscription outcome into consistent categories
df["y"] = df["y"].replace({
    "yes": "yes",
    "no": "no"
})

# Keep valid subscription outcomes
df = df[df["y"].isin(["yes", "no"])].copy()

# Save cleaned dataset
df.to_csv("cleaned_bank_marketing.csv", index=False)

# Create conversion indicator
df["converted"] = (df["y"] == "yes").astype(int)

# Calculate overall KPIs
total_customers = len(df)
subscribed = int(df["converted"].sum())
not_subscribed = total_customers - subscribed

conversion_rate = (
    subscribed / total_customers * 100
    if total_customers > 0 else 0
)

print("\n========== MARKETING CAMPAIGN ANALYSIS ==========")

print("Total customers contacted:", total_customers)
print("Customers subscribed:", subscribed)
print("Customers not subscribed:", not_subscribed)
print(f"Overall conversion rate: {conversion_rate:.2f}%")

# Create conversion summary
summary = pd.DataFrame({
    "Metric": [
        "Total Customers Contacted",
        "Customers Subscribed",
        "Customers Not Subscribed",
        "Conversion Rate (%)"
    ],
    "Value": [
        total_customers,
        subscribed,
        not_subscribed,
        round(conversion_rate, 2)
    ]
})

summary.to_csv(
    output_dir / "conversion_summary.csv",
    index=False
)

# Function to calculate conversion by group
def conversion_by_group(data, column):
    result = data.groupby(column, dropna=False).agg(
        total_customers=("converted", "size"),
        subscribed=("converted", "sum")
    )

    result["conversion_rate"] = (
        result["subscribed"] /
        result["total_customers"] * 100
    )

    return result.sort_values(
        "conversion_rate",
        ascending=False
    )


# 1. Conversion by job
job_results = conversion_by_group(df, "job")

print("\n========== CONVERSION BY JOB ==========")
print(job_results.round(2))

# Plot job conversion rates
job_results["conversion_rate"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Conversion Rate by Job")
plt.xlabel("Job")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(output_dir / "conversion_by_job.png")
plt.close()


# 2. Conversion by education
education_results = conversion_by_group(df, "education")

print("\n========== CONVERSION BY EDUCATION ==========")
print(education_results.round(2))

education_results["conversion_rate"].plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Conversion Rate by Education")
plt.xlabel("Education")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(output_dir / "conversion_by_education.png")
plt.close()


# 3. Conversion by contact method
contact_results = conversion_by_group(df, "contact")

print("\n========== CONVERSION BY CONTACT METHOD ==========")
print(contact_results.round(2))

contact_results["conversion_rate"].plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Conversion Rate by Contact Method")
plt.xlabel("Contact Method")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(output_dir / "conversion_by_contact.png")
plt.close()


# 4. Conversion by number of campaign contacts
df["campaign"] = pd.to_numeric(
    df["campaign"],
    errors="coerce"
)

campaign_data = df.dropna(subset=["campaign"]).copy()

# Group contact counts to make the chart easier to read
campaign_data["contact_group"] = pd.cut(
    campaign_data["campaign"],
    bins=[0, 1, 2, 3, 5, float("inf")],
    labels=[
        "1 contact",
        "2 contacts",
        "3 contacts",
        "4-5 contacts",
        "6+ contacts"
    ]
)

campaign_results = conversion_by_group(
    campaign_data.dropna(subset=["contact_group"]),
    "contact_group"
)

print("\n========== CONVERSION BY CAMPAIGN CONTACTS ==========")
print(campaign_results.round(2))

campaign_results["conversion_rate"].plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Conversion Rate by Number of Campaign Contacts")
plt.xlabel("Number of Contacts")
plt.ylabel("Conversion Rate (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(
    output_dir / "conversion_by_campaign_contacts.png"
)
plt.close()


# 5. Create a simple conversion funnel
funnel_labels = [
    "Customers Contacted",
    "Customers Subscribed"
]

funnel_values = [
    total_customers,
    subscribed
]

plt.figure(figsize=(8, 5))

plt.barh(
    funnel_labels,
    funnel_values
)

plt.title("Bank Marketing Conversion Funnel")
plt.xlabel("Number of Customers")
plt.tight_layout()
plt.savefig(output_dir / "conversion_funnel.png")
plt.close()


# 6. Create a simple KPI dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# KPI cards
axes[0, 0].axis("off")
axes[0, 0].text(
    0.5, 0.6,
    f"{total_customers:,}",
    fontsize=24,
    ha="center"
)
axes[0, 0].set_title("Total Customers Contacted")

axes[0, 1].axis("off")
axes[0, 1].text(
    0.5, 0.6,
    f"{subscribed:,}",
    fontsize=24,
    ha="center"
)
axes[0, 1].set_title("Customers Subscribed")

axes[1, 0].axis("off")
axes[1, 0].text(
    0.5, 0.6,
    f"{conversion_rate:.2f}%",
    fontsize=24,
    ha="center"
)
axes[1, 0].set_title("Overall Conversion Rate")

# Conversion by contact method
contact_results["conversion_rate"].plot(
    kind="bar",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Conversion by Contact Method")
axes[1, 1].set_xlabel("Contact Method")
axes[1, 1].set_ylabel("Conversion Rate (%)")
axes[1, 1].tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.savefig(
    output_dir / "campaign_dashboard.png",
    dpi=150
)
plt.close()

print("\nAnalysis completed successfully!")
print("Cleaned dataset: cleaned_bank_marketing.csv")
print("Charts and summary: outputs folder")
