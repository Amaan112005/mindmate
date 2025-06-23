#!/bin/bash
# Script to download and extract Vosk small English model

MODEL_URL="https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
MODEL_DIR="model"

echo "Downloading Vosk model..."
curl -L -o vosk-model.zip $MODEL_URL

echo "Extracting model..."
unzip vosk-model.zip -d temp_model

echo "Moving model to $MODEL_DIR directory..."
rm -rf $MODEL_DIR
mv temp_model/vosk-model-small-en-us-0.15 $MODEL_DIR

echo "Cleaning up..."
rm -rf temp_model
rm vosk-model.zip

echo "Vosk model downloaded and set up in $MODEL_DIR directory."
