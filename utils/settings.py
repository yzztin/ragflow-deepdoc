import logging
import os


# LIGHTEN = int(os.environ.get("LIGHTEN", "0"))
LIGHTEN = int(os.environ.get("LIGHTEN", "1"))
PARALLEL_DEVICES = 0


try:
    import torch.cuda

    PARALLEL_DEVICES = torch.cuda.device_count()
    logging.info(f"found {PARALLEL_DEVICES} gpus")
except Exception:
    logging.info("can't import package 'torch'")