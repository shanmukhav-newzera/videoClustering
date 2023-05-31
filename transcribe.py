import json
import boto3
import time

# Create a Transcribe client
transcribe_client = boto3.client('transcribe', region_name='ap-south-1')

# Specify the audio file and transcription settings
job_name = "sample_job9jhb00uhuufsdeygdf" #change job name 
output_bucket = "prod-newzera-multimedia"
output_key = "transcriptions/outputs/output.json"
language_code = "en-US"

# Upload the audio file to an S3 bucket
s3_client = boto3.client('s3', region_name='ap-south-1')
audio_file = "kapil1Audio.wav"
s3_key = "transcriptions/inputs/input_audio.wav"
s3_bucket = "prod-newzera-multimedia"
s3_client.upload_file(audio_file, s3_bucket, s3_key)

# Start the transcription job
job_uri = f"s3://{s3_bucket}/{s3_key}"
response = transcribe_client.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='wav',
    OutputBucketName=output_bucket,
    OutputKey=output_key,
    LanguageCode=language_code
)

# # Wait for the transcription job to complete
# time.sleep(10)
# print(transcribe_client.waiter_names)
# waiter = transcribe_client.get_waiter('transcription_job_completed')

# time.sleep(10)


# waiter.wait(
#     TranscriptionJobName=job_name
# )

max_tries = 60
while max_tries > 0:
    max_tries -= 1
    job = transcribe_client.get_transcription_job(
          TranscriptionJobName=job_name)
    job_status = job['TranscriptionJob']['TranscriptionJobStatus']
    if job_status in ['COMPLETED', 'FAILED']:
        print(f"Job {job_name} is {job_status}.")
        if job_status == 'COMPLETED':
            print(
                    f"Download the transcript from\n"
                    f"\t{job['TranscriptionJob']['Transcript']['TranscriptFileUri']}.")
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)

# Download the transcription results
output_location = f"s3://{output_bucket}/{output_key}"
transcription_response = s3_client.get_object(
    Bucket=output_bucket, Key=output_key)
transcription_json = transcription_response['Body'].read().decode('utf-8')

# Extract the text from the transcription results
transcription = json.loads(transcription_json)
transcript_text = transcription['results']['transcripts'][0]['transcript']
print(transcript_text)

# Save the text to a file
output_text_file = "kapil1Output.txt"
with open(output_text_file, 'w') as file:
    file.write(transcript_text)

print("Transcription saved to:", output_text_file)
