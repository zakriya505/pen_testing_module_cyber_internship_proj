import json
import sqlite3

DB_PATH = 'cves.db'
JSON_PATH = "nvdcve-2.0-2013.json"

def import_cves():
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cves (cve_id TEXT PRIMARY KEY, description TEXT)')
    count = 0
    for item in data['vulnerabilities']:
        cve_id = item['cve']['id']
        # Get the English description
        desc = next((d['value'] for d in item['cve']['descriptions'] if d['lang'] == 'en'), '')
        try:
            cur.execute('INSERT OR IGNORE INTO cves (cve_id, description) VALUES (?, ?)', (cve_id, desc))
            count += 1
            if count >= 2000:
                break
        except Exception as e:
            print(f'Error inserting {cve_id}: {e}')
    conn.commit()
    conn.close()
    print(f'Import complete. {count} CVEs added.')

if __name__ == '__main__':
    import_cves()