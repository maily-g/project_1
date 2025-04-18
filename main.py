import whisper 
import os
import pandas as pd


def process_audio_files():
	model = whisper.load_model("small")
	audio_file_path = "/Users/jmontag/Desktop/bcog200/final_project/audio"
	output_path = "/Users/jmontag/Desktop/bcog200/final_project"
	audio_files = os.listdir(audio_file_path)

	for audio_file in audio_files:
		if audio_file.endswith('.wav') or audio_file.endswith('.mp3'):
			print(f'Processing {audio_file}')
			audio_path = os.path.join(audio_file_path, audio_file)
			result = model.transcribe(audio_path, fp16=False)

			#Lists timestamps for each utterance
			segments = result.get("segments", [])
			rows = [{
			"start": round(seg["start"], 2),
			"end": round(seg["end"], 2),
			"utterance": seg["text"].strip()
			} for seg in segments]

			#Saves files as a csv
			df = pd.DataFrame(rows)
			filename = os.path.splitext(audio_file)[0]
			csv_output_path = os.path.join(output_path, f'{filename}_transcript.csv')
			df.to_csv(csv_output_path, index=False)
			print(f'Saved transcript to {csv_output_path}')

def load_expert_files():

def word_count(utterance):
	return len(str(utterance).split())

def unique_words(utterance):
    return len(set(str(utterance).split()))

def levenshtein_distance():

def process_csv_files():
	
def word_error():

def main():
	process_audio_files()

if __name__ == "__main__":
    main()
