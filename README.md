# FUTURE_DS_03 — Marketing Funnel & Conversion Performance Analysis

## Internship
Future Interns — Data Science & Analytics Internship

## Task
Task 3: Marketing Funnel & Conversion Performance Analysis

## Project Overview
This project analyzes bank marketing campaign data to understand customer subscription behavior, measure conversion performance, and identify opportunities to improve marketing campaigns.

Python was used to clean the dataset, calculate key performance indicators, compare customer segments, and create visualizations.

## Business Objectives
- Calculate the overall campaign conversion rate.
- Identify customer groups with higher subscription rates.
- Compare conversion rates by contact method.
- Analyze conversion by job category and campaign contact frequency.
- Evaluate monthly campaign performance.
- Study the relationship between previous campaign outcomes and current subscriptions.
- Provide data-driven marketing recommendations.

## Dataset
Dataset filename: `bank_marketing.csv`

The dataset contains 45,211 campaign records and 17 original columns, including customer demographics, contact information, campaign details, and subscription outcome.

The `y` column indicates whether a customer subscribed to the bank's term deposit.

Note: The dataset does not include separate website visitor and lead counts. Therefore, this project measures campaign-to-subscription conversion rather than a complete website visitor-to-lead-to-customer funnel.

## Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- VS Code
- GitHub

## Data Cleaning
- Standardized column names.
- Cleaned whitespace in text columns.
- Removed duplicate records.
- Checked missing values.
- Created a numerical conversion indicator.
- Exported a cleaned CSV dataset.

## Key Performance Indicators
- Total campaign records: 45,211
- Successful subscriptions: 5,289
- Unsuccessful subscriptions: 39,922
- Overall conversion rate: 11.70%
- Non-conversion rate: 88.30%

## Key Findings
1. The overall subscription conversion rate was 11.70%.
2. Cellular contact had an observed conversion rate of 14.92%.
3. The student job category had an observed conversion rate of 28.68%.
4. Customers contacted once had a conversion rate of 14.60%, compared with 11.20% for customers contacted twice.
5. Customers with a previous successful campaign outcome had an observed conversion rate of 64.73%.
6. Conversion rates varied across months and customer groups.

These findings describe associations in the dataset and do not establish that a particular contact method or campaign strategy caused higher conversions. Group sizes should be considered when interpreting rates.

## Recommendations
- Investigate the cellular contact channel to understand its performance and suitability for future campaigns.
- Evaluate student and retired customer segments while considering their group sizes and business relevance.
- Review repeated-contact strategies and test whether better contact timing can improve conversion.
- Consider previous campaign outcomes when prioritizing customer follow-ups.
- Investigate monthly differences before planning future campaigns.
- Conduct controlled campaign experiments to validate whether proposed changes improve conversion.

## Project Files
- `bank_marketing.csv` — original dataset.
- `cleaned_bank_marketing.csv` — cleaned dataset.
- `task3_analysis.py` — Python analysis script.
- `outputs/` — generated charts and CSV summaries.
- `requirements.txt` — required Python libraries.

## Conclusion
This project demonstrates how data analysis can measure marketing campaign conversion, reveal customer-group patterns, and support evidence-based recommendations.

The results provide a starting point for further campaign testing and performance improvement.

## Author
Data Science & Analytics Intern — Future Interns
