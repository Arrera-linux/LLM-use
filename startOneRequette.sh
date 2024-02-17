#!/bin/bash
reponseFR = ". Repond en français"
echo "Entrez question a Llama :"
read -r promts

allPromts = "$promts+$reponseFR"

./main -m models/llama-2-7b-chat.Q4_K_S.gguf -p $allPromts -n 400 -e