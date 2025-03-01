python raft/raft.py \
  --output ./dist/gen2 \
  --system-prompt-key llama_vi \
  --completion_model meta-llama/Llama-3.3-70B-Instruct-Turbo-Free \
  --workers 1 \
  --questions 3 \
  --p 0.9
