import typer
import assemblyai as aai

app = typer.Typer()

@app.command()
def transcript(key: str = typer.Option(), link: str = typer.Option()):
    aai.settings.api_key = key
    transcriber = aai.Transcriber()
    transcriptText = transcriber.transcribe(link)
    if transcriptText:
        with open('transcript.txt', 'w') as file:
            file.write(transcriptText.text)
        print("Done")

if __name__ == "__main__":
    app()