# IT Asset Inventory Dashboard

## Objective
A centralized **Python-based dashboard** to track and manage organizational IT assets (devices, software, and licenses) in real time.  
Built with **PostgreSQL + ETL scripts + Streamlit + Plotly** for visualization.

---

## Features
- Import asset data from multiple sources:
  - CSV / Excel
  - Active Directory / LDAP
  - Network scans (Nmap)
- Searchable, filterable inventory of devices, software, and licenses
- Asset lifecycle tracking (procurement → in use → decommissioned)
- License expiration alerts and notifications
- Interactive dashboard with charts (device distribution, OS, license status, hardware age)

---

## Project Structure

```bash
it-asset-inventory-dashboard/
│
├── db/                  # Database schema
│   └── schema.sql
│
├── etl/                 # Data ingestion scripts
│   ├── etl_csv.py
│   ├── etl_ldap.py
│   ├── etl_nmap.py
│   └── utils/
│       └── db.py
│
├── data/                # Sample datasets
│   ├── sample_assets.csv
│   ├── sample_licenses.csv
│   └── sample_software.csv
│
├── dashboard/           # Visualization (Streamlit + Plotly)
│   ├── app.py
│   └── charts.py
│
├── alerts/              # Notification scripts
│   └── license_alerts.py
│
├── requirements.txt     # Python dependencies
└── README.md
```
---

## Setup Instructions

1. **Install Python 3.8+**
   - Recommended: use a virtual environment (`python -m venv venv && source venv/bin/activate`)

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
````

3. **Create the database (PostgreSQL)**

   ```bash
   createdb asset_inventory
   psql -d asset_inventory -f db/schema.sql
   ```

4. **Import data using ETL scripts**

   ```bash
   python etl/etl_csv.py
   python etl/etl_ldap.py
   python etl/etl_nmap.py
   ```

5. **Launch dashboard**

   ```bash
   streamlit run dashboard/app.py
   ```

6. **Run alerts for license expiration**

   ```bash
   python alerts/license_alerts.py
   ```

---

## Database

* Normalized schema with tables for `devices`, `users`, `licenses`, `software_catalog`, and `audit_log`.
* See [`db/schema.sql`](db/schema.sql) for details.

---

## Data Samples

* Example CSVs are provided in [`data/`](data/) to test ETL pipelines before connecting real sources.

---

## Extending

* **ETL** → add connectors for SCCM, Lansweeper, or other inventory tools.
* **Dashboard** → add more Plotly charts in `dashboard/charts.py`.
* **Alerts** → integrate with Slack, Teams, or email for notifications.
* **Deployment** → package with Docker or deploy Streamlit app to cloud/on-prem.

---

## License

MIT License

Copyright (c) 2025 Rayvel Taruc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---


