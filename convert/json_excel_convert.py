import pandas as pd
import json
import ast

def excel_to_json(excel_path, json_path):
    df = pd.read_excel(excel_path)

    records = []
    for _, row in df.iterrows():
        item = {}

        for col, val in row.items():
            if pd.isna(val):
                continue

            # Convert stringified list/dict to real object
            if isinstance(val, str):
                val = val.strip()
                if (val.startswith("[") and val.endswith("]")) or \
                   (val.startswith("{") and val.endswith("}")):
                    try:
                        val = ast.literal_eval(val)
                    except Exception:
                        pass

            item[col] = val

        records.append(item)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=4)

    print("JSON created successfully:", json_path)

excel_to_json("mouse.xlsx", "mouse.json")    
