import csv
import statistics

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def parse_condition(condition):
    if '>' in condition:
        col, val = condition.split('>')
        return col.strip(), '>', val.strip()
    elif '<' in condition:
        col, val = condition.split('<')
        return col.strip(), '<', val.strip()
    elif '=' in condition:
        col, val = condition.split('=')
        return col.strip(), '=', val.strip()
    else:
        raise ValueError("Invalid condition format")

def filter_data(data, condition):
    col, op, val = parse_condition(condition)
    filtered = []
    for row in data:
        cell = row[col]
        try:
            cell_val = float(cell)
            val = float(val)
        except ValueError:
            cell_val = cell

        if (op == '=' and cell_val == val) or            (op == '>' and cell_val > val) or            (op == '<' and cell_val < val):
            filtered.append(row)
    return filtered

def aggregate_data(data, agg):
    col, op = agg.split('=')
    col = col.strip()
    op = op.strip().lower()

    try:
        values = [float(row[col]) for row in data]
    except ValueError:
        raise ValueError(f"Cannot aggregate non-numeric column '{col}'")

    if op == 'avg':
        return {'avg': round(statistics.mean(values), 2)}
    elif op == 'min':
        return {'min': min(values)}
    elif op == 'max':
        return {'max': max(values)}
    else:
        raise ValueError("Unsupported aggregation operation")
