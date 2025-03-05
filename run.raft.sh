#!/usr/bin/env bash
python raft/raft.py \
  --output ./dist/gpt-4o-mini \
  --system-prompt-key llama_vi \
  --completion_model gpt-4o-mini \
  --workers 1 \
  --questions 3 \
  --p 0.9
