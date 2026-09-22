import pandas as pd
import os

file_path = r'H:\Project\Internet access\onedata.xlsx'
KEY_COLUMNS = ['YEAR', 'PROVINCE', 'CATEGORY', 'SUB CATEGORY']

def analyze_excel_data(file_path, key_columns):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        xls = pd.ExcelFile(file_path)
        dataframes = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return

    for sheet_name, df in dataframes.items():
        print(f"\n--- Sheet: {sheet_name} ---")
        
        print("Dtypes:")
        print(df.dtypes.to_string())

        print("\nUnique Values:")
        for col in key_columns:
            try:
                if col in df.columns:
                    target_col = col
                else:
                    matching_cols = [c for c in df.columns if c.upper() == col.upper()]
                    target_col = matching_cols[0] if matching_cols else None
                    
                if target_col:
                    unique_values = df[target_col].unique()
                    unique_count = df[target_col].nunique()
                    
                    print(f"  - {target_col} (Count: {unique_count})")
                    if unique_count > 20:
                         print(f"    Values (Top 20): {unique_values[:20]}...")
                    else:
                        print(f"    Values: {unique_values}")
                else:
                    print(f"  - Column '{col}' not found.")
            except Exception as e:
                print(f"  - Error processing '{col}': {e}")


if __name__ == "__main__":
    analyze_excel_data(file_path, KEY_COLUMNS)