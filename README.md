# Mini Autonomous Driving Dataset (Synthetic)

## Overview
This repository contains a small, hand‑crafted autonomous‑vehicle (AV) dataset designed for learning real-world data workflows used in self‑driving systems. It includes driving clips, frame‑level labels, lane line annotations, object detections, and QA audit logs modeled after professional AV data pipelines. A Python CSV export tool is included to demonstrate analytics‑ready data generation.

The goal of this dataset is to demonstrate:
- Scenario diversity (urban, rural, metropolitan)
- Clean metadata for each clip
- Tesla‑style structured labels (lane lines, objects, events)
- QA review logs with analytics‑ready CSV exports

---

## Dataset Structure

self_driving_dataset/
├── raw/
│   ├── clip_001/
│   │   └── metadata.json
│   ├── clip_002/
│   │   └── metadata.json
│   └── clip_003/
│       └── metadata.json
├── labels/
│   ├── clip_001_labels.json
│   ├── clip_002_labels.json
│   └── clip_003_labels.json
├── qa_reports/
│   └── qa_log
├── export_csv.py
└── README.md

