import pandas as pd
import os
import sqlite3

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def run_pipeline_logic():
    print('>>> DEAP pipeline start')

    raw_csv = os.path.join(BASE_DIR, 'data', 'raw', 'pharmacy_sales.csv')
    if not os.path.exists(raw_csv):
        raise FileNotFoundError(f'Raw CSV not found at {raw_csv}')

    df = pd.read_csv(raw_csv)
    # normalize
    df.columns = df.columns.str.strip().str.lower()
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['drug_name'] = df['drug_name'].str.title()
    df['drug_class'] = df['drug_class'].str.title()
    df['quantity_sold'] = pd.to_numeric(df['quantity_sold'], errors='coerce').fillna(0).astype(int)
    df['dose_mg'] = pd.to_numeric(df['dose_mg'], errors='coerce').fillna(0).astype(int)

    def approx_ddd(dc):
        dc = str(dc).lower()
        if 'pen' in dc: return 1000
        if 'fluoro' in dc: return 500
        if 'macro' in dc: return 500
        if 'nitro' in dc: return 800
        return 500

    df['ddd_mg'] = df['drug_class'].apply(approx_ddd)
    df['days_therapy_equiv'] = (df['dose_mg'] * df['quantity_sold']) / df['ddd_mg']

    # Save processed CSV
    processed_dir = os.path.join(BASE_DIR, 'data', 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    processed_path = os.path.join(processed_dir, 'pharmacy_sales_processed.csv')
    df.to_csv(processed_path, index=False)

    # Load into sqlite for demo
    db_path = os.path.join(BASE_DIR, 'data', 'deap.db')
    conn = sqlite3.connect(db_path)
    df.to_sql('staging_pharmacy_sales', conn, if_exists='replace', index=False)

    # Build analytics mart
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS mart_antibiotic_usage;')
    cur.execute('''CREATE TABLE mart_antibiotic_usage AS
                   SELECT date(date) as date, drug_class,
                          COUNT(*) as transactions,
                          SUM(quantity_sold) as total_quantity,
                          SUM(days_therapy_equiv) as total_days_therapy,
                          AVG(patient_age) as avg_age
                   FROM staging_pharmacy_sales
                   GROUP BY date, drug_class;''')
    conn.commit()
    conn.close()

    print('>>> DEAP pipeline completed')
    return True
