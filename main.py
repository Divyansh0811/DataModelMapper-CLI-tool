import click
import pandas as pd

@click.group()
def cli():
  """DataModelMapper CLI for converting CSV datasets"""
  pass


@cli.command(name='create')
@click.argument('csv_file', type=click.Path(exists=True))
@click.option('--model', type=click.Choice(['openai-gpt', 'google-bert', 'meta-llama'], case_sensitive=False), required=True, help='Select the Model type for conversion')
def create(csv_file, model):
  """Create a dataset for fine-tuning the specified model from the given CSV file"""
  df = pd.read_csv(csv_file)

  click.echo(f"Creating data set for the model: {model}")
  
  click.echo("Input Dataframe")
  click.echo(df)
