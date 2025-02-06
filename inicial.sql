CREATE TABLE mecons (
    id SERIAL PRIMARY KEY,
    serial_number TEXT NOT NULL,
    volume DECIMAL(10,2) NOT NULL,
    uom TEXT DEFAULT 'm3',
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de prueba
INSERT INTO mecons (serial_number, volume, timestamp) VALUES 
('1001', 150.75, '2024-02-01 08:00:00'),
('1001', 152.30, '2024-02-02 08:00:00'),
('1002', 98.45, '2024-02-01 10:30:00'),
('1002', 101.25, '2024-02-02 10:30:00'),
('1003', 200.50, '2024-02-01 12:00:00'),
('1003', 205.75, '2024-02-02 12:00:00');

commit;
