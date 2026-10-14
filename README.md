# Simple Calculator App

## Fungsi Aplikasi
Aplikasi kalkulator sederhana berbasis CLI yang mendukung operasi 
penjumlahan, pengurangan, perkalian, dan pembagian, dilengkapi 
validasi input.

## Teknologi
- Bahasa: Python 3.11
- Testing: Pytest
- CI/CD: GitHub Actions
- SAST: SonarCloud

## Cara Menjalankan
\`\`\`bash
pip install -r requirements.txt
python -m app.main
\`\`\`

Menjalankan test:
\`\`\`bash
pytest tests/
\`\`\`

## Overview Pipeline CI/CD
Pipeline ini otomatis berjalan setiap push atau pull request ke branch 
`main`, terdiri dari dua job:
1. **build** — install dependencies dan menjalankan unit test
2. **sast-scan** — menjalankan analisis SAST menggunakan SonarCloud, 
   dengan Quality Gate sebagai pipeline blocker jika kode tidak 
   memenuhi standar kualitas/keamanan.
