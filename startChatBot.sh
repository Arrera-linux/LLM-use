#!/bin/bash
./main  -m models/llama-2-7b-chat.Q4_K_S.gguf --color --ctx_size 2048 -n -1 -ins -b 256 --top_k 10000 --temp 0.2 --repeat_penalty 1.1