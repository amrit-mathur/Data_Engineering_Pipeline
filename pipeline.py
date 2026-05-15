import subprocess
import logging
from pathlib import Path
log_path = Path("data/logs")
log_path.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=log_path / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s "
)
print("Pipeline started...")
logging.info("Pipeline started")
print("Running Bronze layer...")
logging.info("Running Bronze layer")
subprocess.run(["python", "src/extract/fetch_products.py"])
print("Running Silver layer...")
logging.info("Running Silver layer")
subprocess.run(["python", "src/transform/clean_products.py"])
print("Running Gold layer...")
logging.info("Running Gold layer")
subprocess.run(["python", "src/load/create_mart.py"])
print("Pipeline completed successfully")
logging.info("Pipeline completed successfully")