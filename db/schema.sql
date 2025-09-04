-- IT Asset Inventory Dashboard Database Schema
-- Devices Table
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    asset_tag VARCHAR(50) UNIQUE,
    device_type VARCHAR(50),
    model VARCHAR(100),
    os VARCHAR(50),
    location VARCHAR(100),
    department VARCHAR(100),
    owner VARCHAR(100),
    purchase_date DATE,
    status VARCHAR(50),
    decommission_date DATE
);

-- Software Table
CREATE TABLE software (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    version VARCHAR(50),
    vendor VARCHAR(100)
);

-- Licenses Table
CREATE TABLE licenses (
    id SERIAL PRIMARY KEY,
    software_id INTEGER REFERENCES software(id),
    license_key VARCHAR(100),
    expiration_date DATE,
    renewal_status VARCHAR(50),
    assigned_user VARCHAR(100)
);

-- Audit Log Table
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    asset_id INTEGER,
    action VARCHAR(100),
    changed_by VARCHAR(100),
    change_date TIMESTAMP
);
