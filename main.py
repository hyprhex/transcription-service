import typer
import assemblyai as aai

app = typer.Typer()
#how to use 
#python main.py --link (file link or path)
@app.command()
def transcript( link: str = typer.Option()):
    aai.settings.api_key = "YOUR_API_KEY"
    transcriber = aai.Transcriber()
    transcriptText = transcriber.transcribe(link)
    if transcriptText:
        with open(link+'.txt', 'w') as file:
            file.write(transcriptText.text)
        print("Done")

if __name__ == "__main__":
    app()
