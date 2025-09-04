# License expiration alerts
import pandas as pd
from datetime import datetime, timedelta

def check_license_alerts(license_file):
    df = pd.read_csv(license_file)
    today = datetime.today().date()
    alerts = []
    for _, row in df.iterrows():
        exp_date = pd.to_datetime(row['expiration_date']).date()
        if exp_date < today:
            alerts.append(f"License for {row['assigned_user']} expired on {exp_date}")
        elif exp_date <= today + timedelta(days=30):
            alerts.append(f"License for {row['assigned_user']} expiring soon: {exp_date}")
    return alerts

if __name__ == "__main__":
    alerts = check_license_alerts('../data/sample_licenses.csv')
    for alert in alerts:
        print(alert)
