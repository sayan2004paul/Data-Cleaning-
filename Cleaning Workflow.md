# Data-Cleaning-

## Initial Data Assessment

### Data Quality Dimensions Identified

1\. \*\*Completeness Issues\*\*

- Missing values in product\_original\_price (25% of records)

\- Null values in product\_star\_rating (15% of records)

\- Empty sales\_volume fields (30% of records)

\- Mostly null values in unit\_price and unit\_count columns

2\. \*\*Validity Problems\*\*

\- Invalid ASIN codes in 5% of records

\- Negative values in price fields (0.5% of records)

\- Corrupted sales\_volume entries with non-numeric characters

3\. \*\*Accuracy Concerns\*\*

\- Price discrepancies where original\_price < current\_price

\- Rating values outside 1-5 range

\- Illogical sales volume outliers

4\. \*\*Consistency Challenges\*\*

\- Multiple price formatting styles ($12.99 vs 12.99 USD)

\- Inconsistent delivery information formatting

\- Varied sales volume units (some in K, others raw numbers)

## Data Cleaning Methodology

### Phase 1: Structural Cleaning

1\. \*\*Column Removal\*\*

\- Eliminated completely empty columns

\- Removed product URLs and photos (non-analytical data)

\- Dropped unit\_count and unit\_price (95% null values)

2\. \*\*Data Type Standardization\*\*

\- Converted all price fields to float type

\- Standardized rating data to numeric values

\- Ensured boolean fields used proper True/False values

### Phase 2: Handling Missing Data

1\. \*\*Price Fields\*\*

\- Calculated median discount ratio (original/current) from valid records

\- Used this ratio to impute missing original prices

\- Set remaining nulls to 0 with appropriate flagging

2\. \*\*Rating Data\*\*

\- Created "rating\_available" flag column

\- Imputed missing ratings with category averages

\- Maintained separate count of ratings field

3\. \*\*Sales Volume\*\*

\- Developed K→thousand conversion (1K → 1000)

\- Applied median imputation after cleaning

\- Added "volume\_estimated" flag for imputed values

### Phase 3: Complex Field Processing

\*\*Delivery Information Pipeline:\*\*

1\. \*\*Initial Splitting\*\*

\- Separated "FREE delivery" marker from surrounding text

\- Isolated availability notices from delivery dates

2\. \*\*Availability Flagging\*\*

\- Created "Instant\_Availability" boolean

\- Generated "Free\_Delivery" indicator

\- Added "Prime\_Eligible" flag extraction

3\. \*\*Date Parsing\*\*

\- Implemented multi-format date recognition:

\* Weekday formats (Tue, Aug 6)

\* Full date formats (August 13, 2024)

\- Added year normalization for dates without year info

\- Created three output fields:

\* Day of week

\* Standardized date (YYYY-MM-DD)

\* Original text reference

### Phase 4: Validation & Quality Control

1\. \*\*Cross-Field Verification\*\*

\- Ensured original\_price ≥ current\_price when both present

\- Validated rating distributions per product category

\- Checked sales volume against rating counts

2\. \*\*Outlier Detection\*\*

\- Identified and investigated extreme price points

\- Flagged anomalous sales volume records

\- Verified date ranges were temporally logical

3\. \*\*Consistency Checks\*\*

\- Confirmed uniform formatting across all string fields

\- Validated proper case usage in product titles

\- Ensured consistent units across all measurements

## Final Data Structure

### Cleaned Columns

1\. \*\*Product Identification\*\*

\- Validated ASIN codes

\- Standardized product titles

2\. \*\*Pricing Data\*\*

\- Current price (float)

\- Original price (float)

\- Discount percentage (calculated)

\- Minimum offer price (float)

3\. \*\*Performance Metrics\*\*

\- Star rating (1-5 scale)

\- Rating count (integer)

\- Sales volume (standardized units)

\- Best seller/Amazon Choice flags

4\. \*\*Delivery Information\*\*

\- Instant availability (boolean)

\- Free delivery (boolean)

\- Delivery day (text)

\- Delivery date (standard format)

\- Original delivery text (reference)

## Key Decisions & Rationale

1\. \*\*Price Imputation Method\*\*

\- Chose discount ratio method over simple median to preserve price relationships

\- Maintained logical consistency between original and current prices

2\. \*\*Sales Volume Handling\*\*

\- Selected median over mean imputation to reduce outlier impact

\- Preserved distribution characteristics while filling gaps

3\. \*\*Delivery Parsing Approach\*\*

\- Implemented multi-format parser to handle real-world variability

\- Balanced completeness with data quality in extraction

4\. \*\*Null Value Strategy\*\*

\- Used targeted imputation for critical fields

\- Accepted some nulls in less important fields

\- Added flags to identify imputed values

This comprehensive cleaning process transformed the raw Amazon product data into a reliable, analysis-ready dataset while preserving the underlying business meaning and relationships.
