import csv
import json

with open("qa_reports/qa_log.json") as f:
    qa_logs = json.load(f)


def export_qa_to_csv(qa_logs, filename="qa_dataset.csv"):
    rows = []

    # qa_logs is a dictionary: {"clip_001": {...}, "clip_002": {...}}
    for clip_id, log in qa_logs.items():
        row = {
            "clip_id": clip_id,
            "checked_by": log["checked_by"],
            "notes": log["notes"],
            "issues_found": len(log["issues_found"])
        }
        rows.append(row)

    fieldnames = rows[0].keys()

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows)} logs to {filename}")


def export_flattened_qa(qa_logs, filename="qa_flat.csv"):
    rows = []

    for clip_id, log in qa_logs.items():
        issues = log["issues_found"]

        # If there are issues, flatten each one into its own row
        if issues:
            for issue in issues:
                rows.append({
                    "clip_id": clip_id,
                    "checked_by": log["checked_by"],
                    "type": issue.get("type", "unknown"),
                    "severity": issue.get("severity", "unknown"),
                    "description": issue.get("description", "none"),
                    "impact": issue.get("impact", "none"),
                    "notes": log["notes"]
                })
        else:
            # No issues → create a single "clean" row
            rows.append({
                "clip_id": clip_id,
                "checked_by": log["checked_by"],
                "type": "none",
                "severity": "none",
                "description": "no issues",
                "impact": "none",
                "notes": log["notes"]
            })

    fieldnames = rows[0].keys()

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported flattened QA to {filename}")

export_qa_to_csv(qa_logs)
export_flattened_qa(qa_logs)
