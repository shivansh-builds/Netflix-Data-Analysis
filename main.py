from __future__ import annotations

import sys
from pathlib import Path

from src.analysis import generate_eda_summary
from src.config import (
    CHARTS_DIR,
    PROCESSED_DATA_PATH,
    RAW_DATA_PATH,
    REPORTS_DIR,
    TABLES_DIR,
    configure_logging,
)
from src.loader import load_raw_dataset, save_validation_summary, validate_dataset
from src.preprocessing import preprocess_dataset
from src.report_generator import generate_business_report
from src.sql_analysis import execute_sql_workflow
from src.statistics import compute_statistics_summary
from src.utils import ensure_directory
from src.visualization import generate_visualization_suite


def run_pipeline() -> None:
    logger = configure_logging()
    logger.info("Starting Netflix data analysis pipeline")

    project_root = Path(__file__).resolve().parent
    ensure_directory(project_root / "data" / "raw")
    ensure_directory(project_root / "data" / "processed")
    ensure_directory(CHARTS_DIR)
    ensure_directory(REPORTS_DIR)
    ensure_directory(TABLES_DIR)

    raw_df = load_raw_dataset(RAW_DATA_PATH)
    validation_summary = validate_dataset(raw_df)
    save_validation_summary(
        validation_summary,
        REPORTS_DIR / "data_quality_summary.csv",
    )
    logger.info("Validation complete: %s rows, %s columns", *validation_summary["shape"])

    processed_df = preprocess_dataset(raw_df)
    processed_df.to_csv(PROCESSED_DATA_PATH, index=False)
    logger.info("Cleaned dataset saved to %s", PROCESSED_DATA_PATH)

    sql_outputs = execute_sql_workflow(processed_df)
    logger.info("SQL workflow created %s SQL outputs", len(sql_outputs))

    stats_summary = compute_statistics_summary(processed_df)
    eda_summary = generate_eda_summary(processed_df)
    chart_paths = generate_visualization_suite(processed_df, CHARTS_DIR)
    logger.info("Generated %s charts", len(chart_paths))

    report_path = generate_business_report(
        processed_df=processed_df,
        validation_summary=validation_summary,
        stats_summary=stats_summary,
        eda_summary=eda_summary,
        chart_paths=chart_paths,
        output_path=REPORTS_DIR / "business_insights_report.md",
    )
    logger.info("Business report saved to %s", report_path)

    logger.info("Netflix analysis pipeline completed successfully.")


if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as exc:  # pragma: no cover - CLI safety
        print(f"Pipeline failed: {exc}", file=sys.stderr)
        raise
