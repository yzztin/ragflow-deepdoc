import os

import nltk
from huggingface_hub import snapshot_download

from utils.file_utils import get_project_base_directory


nltk.download("punkt_tab")
nltk.download("wordnet")

snapshot_download(
    repo_id="InfiniFlow/huqie",
    local_dir=os.path.join(get_project_base_directory(), "rag/res/huqie"),
    local_dir_use_symlinks=False,
)
snapshot_download(
    repo_id="InfiniFlow/deepdoc",
    local_dir=os.path.join(get_project_base_directory(), "rag/res/deepdoc"),
    local_dir_use_symlinks=False,
)
snapshot_download(
    repo_id="InfiniFlow/text_concat_xgb_v1.0",
    local_dir=os.path.join(get_project_base_directory(), "rag/res/deepdoc"),
    local_dir_use_symlinks=False,
)